import os

from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch


if __name__ == "__main__":

    print("[INFO] Loading documents...")

    docs = load_all_documents("data")

    print(f"[INFO] Total documents loaded: {len(docs)}")

    # Create vector store
    store = FaissVectorStore(
        persist_dir="faiss_store",
        embedding_model="all-MiniLM-L6-v2"
    )

    # FAISS files
    faiss_path = os.path.join("faiss_store", "faiss.index")
    metadata_path = os.path.join("faiss_store", "metadata.pkl")

    # Build index if it doesn't exist
    if os.path.exists(faiss_path) and os.path.exists(metadata_path):

        print("[INFO] Existing FAISS index found.")
        print("[INFO] Loading FAISS index...")

        store.load()

    else:

        print("[INFO] FAISS index not found.")
        print("[INFO] Building FAISS index from documents...")

        store.build_from_documents(docs)

    # RAG Search
    rag_search = RAGSearch()

    query = "What is the case of Siddharth Dalmia vs Union of India about?"

    print(f"\n[INFO] Query: {query}")

    summary = rag_search.search_and_summarize(
        query,
        top_k=3
    )

    print("\n========== SUMMARY ==========")
    print(summary)