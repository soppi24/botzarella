# Botzerella

Meet **Botzarella** (Bot Mozzarella, made sense in my head), A RAG-powered chatbot that analyzes restaurant reviews using local LLMsa dramatic pizza sommelier who references actual customer reviews when answering questions.

## What's All This?

You're looking at my first AI project, with way more to come in future, but I think this small step is pretty cool. I managed to build a 'retrieval-augmented generation system' (That's the RAG!) that:
- Converts reviews to vector embeddings 
- Searches for relevant reviews when you ask questions
- Feeds those reviews to a local Llama model for responses

WAY more practical than training your own model, but I suppose short term.

## Setup & Run

**Important:** Ollama must be running in the background any time it runs or this won't work. Been there, done that.

```bash
# Install Ollama and download models
ollama serve
ollama pull llama3.2 
ollama pull mxbai-embed-large

# Install the important libraries and ask away
pip install langchain-ollama langchain-chroma langchain-core pandas
python main.py
```

## Hardware Warning

This runs locally and is **very CPU/GPU intensive**. I used my desktop PC - didn't even dare test on my laptop. Of course, first responses are slow as models load into memory, but that's part of the fun right?

## Files

- `main.py` - Main chatbot with Botzarella's dramatic personality
- `vector.py` - Vector database setup and retrieval
- `realistic_restaurant_reviews.csv` - Review data

Tech Stack (Or if you can even call it that)

- Ollama 
- LangChain 
- Chroma 
- mxbai-embed-large 
- Python packages: langchain-ollama, langchain-chroma, langchain-core, pandas