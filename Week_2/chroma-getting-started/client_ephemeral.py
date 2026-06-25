import chromadb

client = chromadb.Client()           # ephemeral / in-memory

collection = client.get_or_create_collection(name="temp_demo")
collection.upsert(
    documents=["hello world", "goodbye world"],
    ids=["1", "2"],
)
print(client.heartbeat())            # check it's alive (returns a timestamp)
print(collection.query(query_texts=["hi"], n_results=1))
# Data vanishes when the script ends.
