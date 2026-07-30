# NLP Coursework

Problem sets and a final research project from a Natural Language Processing course (CS4343).

## Contents

- `PS1/UAStringParser.java` — Command-line tool that reads a text file, splits it into whitespace-delimited tokens, and prints every token matching a user-supplied regular expression along with a count of matching vs. total tokens. Run as `java UAStringParser <inputFile> <regex>`.
- `PS2/application/` — An n-gram language model exposed as a Discord bot:
  - `grams.py` — Builds unigram/bigram/trigram frequency models from a text corpus, computes log-probabilities, and saves/loads the models as JSON (`ngrams/`, `output/`).
  - `main.py` — Trains (or loads cached) n-gram models from `shakespear.txt`, then given a prompt predicts the next ~10 words using weighted-random bigram or trigram continuation and returns the generated text with its probability.
  - `bot.py` — A `discord.py` bot: when mentioned in a message, it feeds the message text to `main.py` as a prompt, generates both a bigram and a trigram continuation, and replies in the Discord channel with the generated text and its computed probability. Reads the bot token from the `NLP_BOT_TOKEN` environment variable.
  - `.env.example` — Template for the required environment variable.
  - `PS2Sharum.tex`/`.pdf` — Write-up.
- `Project/` — Final research project on sentiment analysis and language generation, titled *"Sentiment Inversion: An Implementation of a Transform and Feedforward Neural Networks"*. It proposes combining a BowTie feedforward network (sentiment classification) with a Transformer (context-preserving language generation with scaled dot-product attention) to invert the sentiment of a sentence while keeping its context, using the HuggingFace IMDB and WikiText datasets. Includes the proposal and final research report (`.tex`/`.pdf`), presentation slides, bibliography (`Bib/`), and `Code/Data.ipynb` — an exploratory notebook that loads datasets via `datasets.load_dataset` (HuggingFace `datasets` library; dependencies pinned in `Code/requirements.txt`).

## Stack

Java, Python (`discord.py`, HuggingFace `datasets`), LaTeX.

## Running

### PS1 — string parser
```
cd PS1
javac UAStringParser.java
java UAStringParser input.txt "<your-regex>"
```

### PS2 — n-gram Discord bot
```
cd PS2/application
pip install discord.py python-dotenv
cp .env.example .env      # then edit .env and set NLP_BOT_TOKEN=<your-discord-bot-token>
python bot.py
```
`bot.py` reads `NLP_BOT_TOKEN` from the environment (via `os.environ["NLP_BOT_TOKEN"]`) — make sure it's exported or loaded from `.env` before running. On first run it builds the n-gram models from `shakespear.txt` and caches them as JSON under `ngrams/`; a bot mention in Discord (`@BotName some text`) triggers a bigram and trigram continuation reply.

### Project/Code — exploratory notebook
```
cd "Project/Code"
pip install -r requirements.txt jupyter
jupyter notebook Data.ipynb
```
