# Local RAG Project

This project is a lightweight Retrieval-Augmented Generation (RAG) example built around local documents. It demonstrates how to ingest PDF and text files, split the content into smaller chunks, generate embeddings, and store them in a persistent vector database for retrieval-based querying.

The workflow is implemented in Jupyter notebooks and uses a local Chroma vector store so the project can run without requiring an external hosted service.

## What this project does

- Loads files from the local `data/` directory
- Supports both PDF and plain-text sources
- Splits large documents into manageable chunks
- Generates embeddings using `sentence-transformers`
- Stores embeddings in a persistent Chroma database
- Provides a notebook-based environment for experimenting with RAG workflows

## Project structure

- `data/`
  - `pdf/` - PDF documents for ingestion
  - `text_file/` - Text-based documents, including sample Python content
  - `vector_store/` - persistent Chroma database files
- `notebook/`
  - `document.ipynb` - basic document loading and text ingestion examples
  - `pdf_loader.ipynb` - end-to-end RAG pipeline: loading PDFs, chunking, embeddings, and vector storage
- `requirements.txt` - Python dependencies for the project
- `.rag311/` - local virtual environment directory for the project

## Main workflow

The project follows this pipeline:

1. Load documents from a directory or file
2. Clean and normalize content from PDFs/text files
3. Split documents into chunks using `RecursiveCharacterTextSplitter`
4. Generate embeddings with a SentenceTransformer model
5. Store the chunks and embeddings in a Chroma collection
6. Retrieve relevant chunks for a query and use them as context for downstream generation tasks

## Technologies used

- Python
- LangChain and LangChain Community loaders
- `langchain-text-splitters`
- `sentence-transformers`
- `chromadb`
- NumPy and scikit-learn utilities
- Jupyter notebooks

## Setup

From the project root, create and activate a virtual environment if needed, then install dependencies:

```bash
pip install -r requirements.txt
```

If you are using the included local environment folder, you can also activate it directly from the project root:

```bash
.\.rag311\Scripts\activate
```

## Run the notebooks

Start Jupyter from the project root:

```bash
jupyter notebook
```

Then open the notebooks inside `notebook/` and run the cells in order.

## Data placement

Place your source data in one of these folders:

- `data/pdf/` for PDF files
- `data/text_file/` for text files

The vector database is stored under:

- `data/vector_store/`

## Notes

- This project is designed for experimentation and learning rather than production deployment.
- Chroma persists its collection locally, so the database remains available between notebook runs.
- If you add new documents, re-run the ingestion and embedding steps to include them in the vector store.
- Some model downloads may happen automatically when the embedding model is first initialized.

## Example use case

A common workflow in this repository is:

1. Add a PDF or text file to `data/`
2. Load and split the document in the notebook
3. Generate embeddings
4. Save the vectors to the local Chroma store
5. Use the stored chunks as retrieval context for a RAG answer

## License

This project is intended for educational and experimental use.
