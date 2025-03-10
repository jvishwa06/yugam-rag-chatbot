import base64
from db import query_db
from embedder import get_embedding

def search_event(query):
    """Finds the best matching event based on query."""
    query_embedding = get_embedding(query)
    result = query_db(query_embedding)

    if result:
        event_info = f"Event: {result['event']}\nDetails: {result['details']}"
        
        # Decode base64 image
        img_data = base64.b64decode(result["poster"])
        image_path = "retrieved_event.png"
        with open(image_path, "wb") as img_file:
            img_file.write(img_data)
        
        return event_info, image_path
    return "No relevant event found.", None
