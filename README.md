# Restaurant Name Generator - Cookchain

Generates restaurant names and menu items using LangChain + Google Gemini. Built this to experiment with LangChain's sequential chains.

## Stack

- LangChain (prompt chaining)
- Streamlit (UI)
- Google Gemini 2.5 Flash
- Python 3.8+

## Setup

```bash
git clone <repo-url>
cd cookchain
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Add your Google API key to `.env`:

```
GOOGLE_API_KEY=your_key_here
```

Get one from [Google AI Studio](https://makersuite.google.com/app/apikey).

## Run

```bash
streamlit run main.py
```

Go to `localhost:8501` and pick a cuisine.

## How it works

Two chained prompts:

1. Generate restaurant name from cuisine
2. Generate menu items using that name

Runs in parallel with `RunnableParallel`, returns formatted output with emojis.

Edit `langchain_helper.py` to change the model, temperature, or prompts. Add cuisines in `main.py`.

## Example

```
🍽️ Here's a fancy name suggestion for your Italian restaurant:

✨ "La Tavola Dorata" ✨

📋 And here are some menu items for La Tavola Dorata, as a comma-separated list:

Antipasto Misto Semplice, Burrata & Heirloom Tomatoes, Prosciutto di Parma with Melon,
Tagliatelle al Tartufo Bianco, Rigatoni alla Carbonara di Guanciale...
```
