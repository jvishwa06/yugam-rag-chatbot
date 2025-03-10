from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text):
    """Generate an embedding for a given text."""
    return model.encode(text).tolist()
