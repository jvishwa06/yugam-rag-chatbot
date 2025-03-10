import pandas as pd
import base64
from db import insert_into_db
from embedder import get_embedding
from query import search_event
from groq_api import generate_response

# Load dataset
df = pd.read_csv("data/events.csv")

# Insert event details into ChromaDB
for i, row in df.iterrows():
    embedding = get_embedding(row["details"])
    
    with open(row["poster"], "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode("utf-8")

    metadata = {"event": row["event"], "details": row["details"], "poster": img_base64}
    insert_into_db(str(i), embedding, metadata)

print("Event database initialized!")

# Run a test query
query_text = "event related to Hands-on with computer visioncls"
event_details, image_path = search_event(query_text)

if event_details:
    print(event_details)
    ai_response = generate_response(query_text, event_details)
    print("\nAI Response:\n", ai_response)
