# Local RAG Project for Learning

This repository is a hands-on learning project for building a Retrieval-Augmented Generation (RAG) system using local documents. The goal is to understand the core workflow of RAG step by step:

- load knowledge from files,
- split large documents into chunks,
- convert chunks into embeddings,
- store them in a vector index,
- retrieve relevant context for a query,
- pass that context to an LLM for final answer generation.

This project is intentionally simple and educational. It focuses on understanding the mechanics of RAG rather than building a production-ready enterprise system.

## Why this project exists

The purpose of this repository is to help learn how a RAG pipeline works in practice. It demonstrates:

- document ingestion from local files,
- chunking strategy for long-form content,
- embedding generation using a sentence-transformer model,
- vector search with FAISS,
- retrieval of the most relevant chunks,
- summarization using a Groq-hosted LLM.

## Main learning workflow

The system follows this pipeline:

1. Read files from the `data` folder.
2. Detect supported file types like PDF and text.
3. Convert each file into LangChain documents.
4. Split the content into smaller chunks.
5. Generate embeddings for each chunk.
6. Store those embeddings in a FAISS index.
7. Search the index for the most relevant content for a user question.
8. Use the retrieved text as context for a final LLM response.

## Project structure

```text
RAG/
├── app.py                     # Main entry point for the local RAG pipeline
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── data/
│   ├── pdf/                  # PDF files for retrieval
│   ├── text_file/            # Text files and sample documents
│   └── vector_store/         # Local vector database files (if used)
├── faiss_store/
│   ├── faiss.index           # FAISS vector index
│   └── metadata.pkl          # Metadata linked to index entries
├── notebook/
│   ├── document.ipynb        # Learning notebook
│   └── pdf_loader.ipynb      # PDF ingestion and vector-building examples
├── src/
│   ├── __init__.py
│   ├── data_loader.py        # File loading logic
│   ├── embedding.py          # Embedding generation and chunking pipeline
│   ├── search.py             # Query + retrieval + LLM summarization flow
│   └── vectorstore.py        # FAISS vector store implementation
└── .env.example              # Optional example env file (if present in your setup)
```

## Technologies used

This project combines a few important tools commonly used in RAG systems:

- Python
- LangChain and LangChain Community
- FAISS for vector search
- SentenceTransformers for embeddings
- Groq for the language model layer
- Pandas / NumPy utilities in supporting scripts
- Jupyter notebooks for experiments

## Setup

### 1. Create a virtual environment

On Windows:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your LLM API key

This project uses Groq for the final answer generation step. Create a `.env` file in the project root and add your key.

```env
GROQ_API_KEY=your_key_here
```

If you are following the project as an exercise, this is the place where you can understand how an external LLM is connected to the retrieval pipeline.

## How to run the project

From the project root, run:

```bash
python app.py
```

This script:

- loads documents from the `data` folder,
- builds or loads the FAISS index,
- runs a sample question,
- retrieves relevant chunks,
- summarizes the answer with the LLM.

## Data folder

Place your source documents in the `data` folder. This project is designed to support multiple file types, such as:

- PDF files in `data/pdf/`
- text files in `data/text_file/`
- additional formats if supported by the loaders

When new files are added, the indexing step should be refreshed so the new content appears in search results.

## Understanding the code

### `src/data_loader.py`

This module loads files from the local filesystem and converts them into LangChain documents. The idea is to standardize the input format before embedding and searching.

### `src/embedding.py`

This file handles the chunking and embedding process. It converts document text into numerical vectors that can be compared semantically during retrieval.

### `src/vectorstore.py`

This is the vector search layer. It stores every chunk in a FAISS index, allowing the system to perform similarity search on the user query.

### `src/search.py`

This is where the workflow becomes a true RAG pipeline:

- embed the query,
- find similar chunks,
- collect relevant context,
- send that context to the LLM for answer generation.

### `app.py`

This file acts as the main pipeline runner. It wires everything together and demonstrates the end-to-end behavior.

## Learning goals for this project

This repo is best used to learn these RAG concepts:

- retrieval over local knowledge bases,
- semantic similarity search,
- chunking and context selection,
- embedding pipelines,
- combining document retrieval with LLM reasoning,
- building a simple local prototype before scaling to production.

## Example use case

You can ask questions like:

```text
What is the case of Siddharth Dalmia vs Union of India about?
```

The pipeline will:

- pull relevant documents from the vector index,
- select the most relevant chunks,
- build a context window,
- summarize the answer using the LLM.

## Important notes

- This project is meant for learning and experimentation.
- It is not optimized for production deployment or enterprise scale.
- Large documents may require better chunking and metadata strategies.
- Embedding models and LLMs may require internet access for the first download.
- Re-indexing is needed when new documents are added.

## Suggested next improvements

As you learn more, you can extend this project by adding:

- a better prompt template,
- metadata-aware filtering,
- a web UI with Streamlit or Gradio,
- support for more document formats,
- hybrid search (
  keyword + semantic search),
- logging and evaluation of retrieval quality,
- a more robust production-ready architecture.

## License

This project is intended for educational and experimental use.

## Summary

This repository is a practical introduction to RAG. It gives you a working example of how a local knowledge base can be searched, retrieved, and used to answer questions with the help of an LLM. The best way to learn from it is to read through the files, run it locally, and experiment with different documents, chunk sizes, and query types.
