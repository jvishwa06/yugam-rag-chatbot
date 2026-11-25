# YUGAM RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that finds the event that best matches a question and answers using its details. Each event also has a poster image, which is stored with the event and saved to disk when the event is retrieved.

## How it works

1. **Load events**: `src/main.py` reads `data/events.csv` (columns `event`, `details` and `poster`, where `poster` is an image path under `data/images/`).
2. **Embed**: each event's `details` text is embedded with the `all-MiniLM-L6-v2` sentence-transformers model (`src/embedder.py`).
3. **Store**: the embedding goes into a persistent [ChromaDB](https://www.trychroma.com) collection named `event_rag` (`src/db.py`, saved in `chroma_db/`). The event name, details and the poster (base64-encoded) are kept as metadata.
4. **Retrieve**: a question is embedded and the closest event is fetched (top 1). Its poster is decoded and saved as `retrieved_event.png` (`src/query.py`).
5. **Answer**: the question and the event details go to the Groq chat completions API with the `llama3-8b-8192` model (`src/groq_api.py`), which writes the answer.

Running `src/main.py` builds the database and then runs one sample query.

## Setup

```bash
pip install pandas sentence-transformers chromadb requests python-dotenv
```

Create `src/.env` containing your own key:

```
GROQ_API_KEY=your_groq_key
```

## Run

```bash
cd src
python main.py
```

Edit `query_text` in `src/main.py` to ask a different question.
