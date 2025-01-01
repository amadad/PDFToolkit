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

### PDF to Markdown Converters
- **01-docling.py** - Basic PDF to markdown converter
  ```python
  # Convert PDFs to basic markdown format
  from docling.document_converter import DocumentConverter

  # Process workflow:
  # 1. Load PDF document
  # 2. Extract text content
  # 3. Convert to markdown
  # 4. Save output file

  # Features:
  # - Basic text extraction
  # - Simple markdown conversion
  # - Maintains basic structure
  # - Handles multiple pages
  ```

- **02-marker.py** - PDF to enhanced markdown converter
  ```python
  # Convert PDFs to markdown with AI image descriptions
  from marker.converters.pdf import PdfConverter

  # Process workflow:
  # 1. Extract text/images from PDF
  # 2. Save images to disk
  # 3. Get GPT-4o Vision descriptions
  # 4. Insert descriptions into markdown
  # 5. Save enhanced markdown with AI descriptions

  # Features:
  # - Preserves document layout and structure
  # - Extracts and saves embedded images
  # - Uses GPT-4o Vision for detailed image analysis
  # - Generates markdown with AI image descriptions
  # - Handles both inline and referenced images
  ```

### Document Analysis
- **03-megaparse.py** - Advanced document structure parser
  ```python
  # Parse complex document structures with UnstructuredParser
  from megaparse import MegaParse

  # Process workflow:
  # 1. Load document with UnstructuredParser
  # 2. Extract hierarchical structure
  # 3. Process tables and lists
  # 4. Generate structured output

  # Features:
  # - Deep structural analysis
  # - Table and list detection
  # - Maintains document hierarchy
  # - Supports multiple formats
  ```

- **06-markitdown.py** - Complete document processor
  ```python
  # All-in-one document processing solution
  from markitdown import MarkItDown

  # Process workflow:
  # 1. Load document
  # 2. Process text and visuals
  # 3. Generate descriptions
  # 4. Create enhanced output

  # Features:
  # - Complete processing
  # - Multiple model support
  # - Configurable pipeline
  # - Rich output options
  ```

### Chart Detection
- **04-colqwen-only.py** - Visual similarity detector
  ```python
  # Detect and analyze visuals using similarity
  from colpali_engine.models import ColQwen2

  # Process workflow:
  # 1. Load document images
  # 2. Generate embeddings
  # 3. Compare with reference set
  # 4. Output similarity scores

  # Features:
  # - Visual similarity detection
  # - Embedding generation
  # - Reference comparison
  # - Batch processing support
  ```

- **04-colqwen-search.py** - Chart detection system
  ```python
  # Scan and identify charts in PDFs
  from colpali_engine.models import ColQwen2

  # Process workflow:
  # 1. Scan PDF directories
  # 2. Extract potential charts
  # 3. Analyze with ColQwen2
  # 4. Generate report

  # Features:
  # - Directory scanning
  # - Chart identification
  # - Batch processing
  # - Report generation
  ```

### Chart Analysis
- **04-llama-only.py** - Direct chart analyzer
  ```python
  # Analyze charts using Llama model
  from together import Together

  # Process workflow:
  # 1. Load chart image
  # 2. Process with Llama
  # 3. Generate description
  # 4. Output analysis

  # Features:
  # - Direct chart analysis
  # - Natural language output
  # - Cloud processing
  # - Detailed descriptions
  ```

- **05-ollama-llama.py** - Local chart analyzer
  ```python
  # Local chart analysis with Llama
  from ollama import Client

  # Process workflow:
  # 1. Initialize local Llama
  # 2. Process chart locally
  # 3. Generate description
  # 4. Save results

  # Features:
  # - Local processing
  # - No API dependency
  # - Fast inference
  # - Privacy focused
  ```

### Combined Analysis
- **04-llama+colqwen.py** - Combined visual analyzer
  ```python
  # Combine detection and analysis capabilities
  from colpali_engine.models import ColQwen2

  # Process workflow:
  # 1. Detect charts with ColQwen2
  # 2. Filter relevant images
  # 3. Analyze with Llama
  # 4. Generate combined output

  # Features:
  # - Dual model processing
  # - Enhanced accuracy
  # - Comprehensive analysis
  # - Flexible output formats
  ```

## 📚 References

- [ColQwen2](https://huggingface.co/vidore/colqwen2-v0.1) - Visual retrieval model
- [Docling](https://github.com/DS4SD/docling) - IBM's document toolkit
- [Marker](https://github.com/VikParuchuri/marker) - PDF extraction by [Vik Paruchuri](https://x.com/vikparuchuri)
- [MegaParse](https://github.com/QuivrHQ/MegaParse) - Advanced parsing
- [MarkItDown](https://github.com/microsoft/markitdown) - Microsoft's converter
- [Ollama](https://ollama.ai/) - Local LLM inference
- [Together](https://together.ai/) - Cloud LLM inference
- [Unstructured](https://unstructured.io/) - Document parsing
- [Llama](https://github.com/facebookresearch/llama) - Facebook's LLM
