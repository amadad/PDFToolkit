from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered
from openai import OpenAI
import base64
import os
from multiprocessing import freeze_support


def get_image_description(image_path):
    client = OpenAI()
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this image in detail"},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"},
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    return response.choices[0].message.content


def process_images(images, output_dir):
    """Extract and analyze all images, return a dict of filename -> description"""
    image_descriptions = {}
    print(f"Processing {len(images)} images...")

    for img_ref, img_data in images.items():
        img_path = os.path.join(output_dir, img_ref)
        os.makedirs(os.path.dirname(img_path), exist_ok=True)

        # Save image
        if isinstance(img_data, bytes):
            with open(img_path, "wb") as f:
                f.write(img_data)
        else:  # PIL Image
            img_data.save(img_path, "JPEG")

        # Get description
        description = get_image_description(img_path)
        image_descriptions[img_ref] = description
        print(f"Processed {img_ref}")

    return image_descriptions


def enhance_markdown(text, image_descriptions):
    """Insert image descriptions into markdown text"""
    print(f"\nEnhancing markdown with {len(image_descriptions)} descriptions")
    enhanced_text = text
    matches_found = 0

    for img_ref, description in image_descriptions.items():
        print(f"Looking for image: {img_ref}")
        # Handle both formats: with and without alt text
        img_markers = [
            f"![]({img_ref})",  # no alt text
            f"![{img_ref}]({img_ref})",  # with alt text
        ]
        found = False
        for marker in img_markers:
            if marker in enhanced_text:
                print(f"Found marker: {marker}")
                enhanced_text = enhanced_text.replace(
                    marker, f"{marker}\n\n*Image Description:* {description}\n"
                )
                matches_found += 1
                found = True
                break
        if not found:
            print(f"No match found for {img_ref}")

    print(f"Total matches found: {matches_found}")
    return enhanced_text


def main():
    input_pdf = "docs/ACCENTURE_Luxury_2025.pdf"
    output_dir = f"output/{os.path.splitext(os.path.basename(input_pdf))[0]}"
    os.makedirs(output_dir, exist_ok=True)

    # Extract content
    converter = PdfConverter(
        artifact_dict=create_model_dict(), config={"output_dir": output_dir}
    )
    rendered = converter(input_pdf)
    text, metadata, images = text_from_rendered(rendered)

    # Process all images first
    image_descriptions = process_images(images, output_dir)

    # Enhance markdown with descriptions
    enhanced_text = enhance_markdown(text, image_descriptions)

    # Save result
    with open(f"{output_dir}/enhanced_output.md", "w", encoding="utf-8") as f:
        f.write(enhanced_text)


if __name__ == "__main__":
    freeze_support()  # Needed for Windows
    main()
