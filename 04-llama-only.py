import os
import base64
from pathlib import Path
from PIL import Image
from io import BytesIO
from together import Together


def image_to_base64(image_path):
    with Image.open(image_path) as img:
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode()


def analyze_image(image_path, query):
    img_base64 = image_to_base64(image_path)
    client = Together(api_key=os.getenv("TOGETHER_API_KEY"))
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "You are a data analyst. " + query},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{img_base64}"},
                    },
                ],
            }
        ],
        max_tokens=300,
        temperature=0.2,  # More focused on factual analysis
    )
    return response.choices[0].message.content


# Image to analyze
image_path = Path("output/ACCENTURE-Marker/_page_7_Figure_6.jpeg")

queries = [
    "What type of visualization is this and what are its key metrics?",
    "What are the main quantitative insights and trends shown in this data?",
    "Summarize the key message of this visualization in 2-3 concise bullet points.",
]

print("=== Quantitative Analysis ===")
for query in queries:
    print(f"\nQ: {query}")
    print(f"A: {analyze_image(image_path, query)}")
