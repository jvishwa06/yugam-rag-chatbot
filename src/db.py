import chromadb

# Initialize ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="event_rag")

def insert_into_db(id, embedding, metadata):
    """Insert event details into ChromaDB."""
    collection.add(ids=[id], embeddings=[embedding], metadatas=[metadata])

def query_db(query_embedding, top_k=1):
    """Retrieve the most relevant event."""
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    return results["metadatas"][0][0] if results["ids"] else None
