"""Chroma Cloud getting-started example.

Adds a few documents to a collection, then runs a semantic query against it.
Data is intentionally NOT deleted at the end so it persists in the cloud DB.
"""

import os

import chromadb
from dotenv import load_dotenv

# Load CHROMA_API_KEY / CHROMA_TENANT / CHROMA_DATABASE from the .env file
# that `chroma db connect ... --env-file` generated.
load_dotenv()

COLLECTION_NAME = "getting_started_docs"

# Data we will ingest. Each document gets an id and some metadata.
DOCUMENTS = [
    "Chroma is an open-source vector database for building AI applications.",
    "LangChain provides standard building blocks for LLM-powered apps.",
    "Embeddings turn text into vectors that capture semantic meaning.",
    "A vector store performs similarity search over stored embeddings.",
    "Python is a popular language for data science and machine learning.",
]
IDS = [f"doc-{i}" for i in range(len(DOCUMENTS))]
METADATAS = [
    {"topic": "chroma"},
    {"topic": "langchain"},
    {"topic": "embeddings"},
    {"topic": "vector-store"},
    {"topic": "python"},
]

QUERY = "What database is used to search embeddings?"
N_RESULTS = 3


def main() -> None:
    # Connect to Chroma Cloud using the credentials from .env.
    client = chromadb.CloudClient(
        api_key=os.getenv("CHROMA_API_KEY"),
        tenant=os.getenv("CHROMA_TENANT"),
        database=os.getenv("CHROMA_DATABASE"),
    )

    # get_or_create so re-running the script does not error if it already exists.
    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    # Ingest the data. Chroma's default embedding function turns the documents
    # into vectors automatically (no separate embedding call needed).
    collection.upsert(documents=DOCUMENTS, ids=IDS, metadatas=METADATAS)

    # Query the collection by meaning.
    results = collection.query(query_texts=[QUERY], n_results=N_RESULTS)

    # ---- Report ----
    print("=" * 70)
    print(f"Collection: {COLLECTION_NAME}  (total items: {collection.count()})")
    print("=" * 70)

    print("\nINGESTED DATA:")
    for doc_id, doc, meta in zip(IDS, DOCUMENTS, METADATAS):
        print(f"  [{doc_id}] ({meta['topic']}) {doc}")

    print(f"\nQUERY:\n  {QUERY!r}  (top {N_RESULTS} results)")

    print("\nRESULTS (most similar first):")
    res_ids = results["ids"][0]
    res_docs = results["documents"][0]
    res_metas = results["metadatas"][0]
    res_dists = results["distances"][0]
    for rank, (rid, rdoc, rmeta, rdist) in enumerate(
        zip(res_ids, res_docs, res_metas, res_dists), start=1
    ):
        print(f"  {rank}. [{rid}] (distance={rdist:.4f}, topic={rmeta['topic']})")
        print(f"     {rdoc}")

    print("\nDone. Data left intact in the collection (not deleted).")


if __name__ == "__main__":
    main()
