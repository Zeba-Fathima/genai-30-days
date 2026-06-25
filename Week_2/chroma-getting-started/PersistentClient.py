import chromadb

client = chromadb.PersistentClient(path="./chroma_data")   # folder to store data

collection = client.get_or_create_collection(name="local_demo")
collection.upsert(
    documents=[
        "Chroma can save data to disk.",
        "PersistentClient survives restarts.",
        "No server or cloud needed.",
    ],
    ids=["d1", "d2", "d3"],
)

print("Total items:", collection.count())
results = collection.query(query_texts=["does my data persist?"], n_results=2)
for doc, dist in zip(results["documents"][0], results["distances"][0]):
    print(f"  ({dist:.4f}) {doc}")
