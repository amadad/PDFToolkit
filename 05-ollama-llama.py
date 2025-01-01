import base64
from pathlib import Path
from ollama import Client


def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def analyze_image(image_path, query):
    client = Client(host="http://localhost:11434")

    # Convert image to base64
    image_b64 = image_to_base64(image_path)

    # Create message with image
    response = client.chat(
        model="llama3.2-vision:11b",
        messages=[{"role": "user", "content": query, "images": [image_b64]}],
    )

    return response["message"]["content"]


# Image path
image_path = "output/ACCENTURE-Marker/_page_7_Figure_6.jpeg"

# Analysis queries
queries = [
    "What charts or graphs do you see in this image?",
    "Describe any visual trends in the data shown",
    "What are the key visual elements that stand out?",
]

# Run analysis
for query in queries:
    print(f"\nQuery: {query}")
    print(f"Analysis: {analyze_image(image_path, query)}")
