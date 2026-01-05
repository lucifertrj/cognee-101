# Cognee-101

> How does AI memory work? - YouTube Video AI Memory Series Part-2

[![How does AI memory work? - YouTube Video AI Memory Series Part-2](https://img.youtube.com/vi/3nWd-0fUyYs/maxresdefault.jpg)](https://www.youtube.com/watch?v=3nWd-0fUyYs)

## 🎯 Overview

This project demonstrates the core concepts of AI memory systems using Cognee:

- **add**: Ingesting and preparing data for processing in Cognee
- **cognify**: Transforming ingested data into a knowledge graph with embeddings, chunks, and summaries
- **memify**: Semantic enrichment of existing knowledge graphs with derived facts
- **search**: Query your AI memory with vectors, graphs, and LLMs

## 📦 Prerequisites

- Python 3.9 – 3.12 is required to run Cognee.
- [uv](https://github.com/astral-sh/uv) package manager

## 🚀 Installation

1. **Create a virtual environment:**

   ```bash
   uv venv
   source .venv/bin/activate
   ```

2. **Initialize the project:**

   ```bash
   uv init
   ```

## ⚙️ Configuration

### For `app.py` (Basic Example)

1. **Install dependencies:**
   ```bash
   uv add cognee
   ```

2. **Set up environment variables:**
   - Check `.env.example_app` for the required environment variables
   - Create a `.env` file with the necessary configuration

### For `custom.py` (Custom Example with Qdrant)

1. **Install dependencies:**
   ```bash
   uv add cognee_community_vector_adapter_qdrant
   ```

2. **Set up environment variables:**
   - Check `.env.example_custom` for the required environment variables
   - Create a `.env` file with the necessary configuration


## 📁 Project Structure

```
cognee-101/
├── app.py                    # Basic Cognee example
├── custom.py                 # Custom example with Qdrant adapter
├── constant.py               # User preferences constant
├── .env                      # Configuration credentials
├── pyproject.toml            # Project dependencies
├── uv.lock                   # Lock file for dependencies
└── README.md                 # This file
```

---

Refer to the official [Cognee](https://github.com/topoteretes/cognee)
