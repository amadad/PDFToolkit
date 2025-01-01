# 🔍 PDFToolkit

### A Collection of PDF Analysis Tools

<p>
<img alt="Python Version" src="https://img.shields.io/badge/python-3.11-blue.svg" />
<img alt="License" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
</p>

-----

<p align="center">
 <a href="#-overview">Overview</a> •
 <a href="#-features">Features</a> •
 <a href="#-prerequisites">Prerequisites</a> •
 <a href="#-installation">Installation</a> •
 <a href="#-tools">Tools</a> •
 <a href="#-references">References</a>
</p>

-----

## 📖 Overview

PDFToolkit is a collection of Python tools for extracting and analyzing PDF content, with a focus on charts and visualizations. It provides multiple approaches from basic text extraction to advanced visual analysis using both local and cloud-based models.

## 🎛️ Features

- Extract text while preserving document layout
- Detect and analyze charts/visualizations
- Generate natural language descriptions of visuals
- Support for both local and API-based processing
- Multiple model options for different needs

## 📋 Prerequisites

- Python 3.11+
- PyTorch with MPS/CPU support
- OpenAI API key (for GPT-4 vision)
- Together API key (for Llama)
- Ollama (for local Llama)

## 🚀 Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/pdftoolkit.git
cd pdftoolkit
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your API keys
```

## 🛠️ Tools

### Document Parsing
- **01-docling.py** - IBM's docling for basic conversion
  ```python
  from docling.document_converter import DocumentConverter
  ```

- **02-marker.py** - Improved text extraction
  ```python
  # Extract text and images from PDFs
  from marker.converters.pdf import PdfConverter
  
  # Process workflow:
  # 1. Extract text/images from PDF
  # 2. Save images to disk
  # 3. Get GPT-4o descriptions
  # 4. Insert descriptions into markdown
  # 5. Save enhanced markdown with AI descriptions
  
  # Features:
  # - Preserves document layout
  # - Extracts embedded images
  # - Uses GPT-4o for image analysis
  # - Generates enhanced markdown with descriptions
  ```

- **03-megaparse.py** - Advanced parsing with UnstructuredParser
  ```python
  from megaparse import MegaParse
  ```

### Visual Analysis
- **04-colqwen-only.py** - Pure similarity-based detection
  ```python
  from colpali_engine.models import ColQwen2
  ```

- **04-colqwen-search.py** - Chart identification in PDFs
  ```python
  # Directory scanning + ColQwen2
  ```

- **04-llama-only.py** - Direct chart analysis
  ```python
  from together import Together
  ```

- **04-llama+colqwen.py** - Combined detection & analysis
  ```python
  # ColQwen2 + Llama integration
  ```

- **05-ollama-llama.py** - Local analysis
  ```python
  from ollama import Client
  ```

### Combined Solutions
- **06-markitdown.py** - All-in-one processing
  ```python
  from markitdown import MarkItDown
  ```

## 📚 References

- [ColQwen2](https://huggingface.co/vidore/colqwen2-v0.1) - Visual retrieval model
- [docling](https://github.com/DS4SD/docling) - IBM's document toolkit
- [marker](https://github.com/VikParuchuri/marker) - PDF extraction
- [MegaParse](https://github.com/QuivrHQ/MegaParse) - Advanced parsing
- [MarkItDown](https://github.com/microsoft/markitdown) - Microsoft's converter