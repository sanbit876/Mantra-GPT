# Mantra-GPT

✨ Mantra-GPT is a chat-bot application based upon textbase and GPT-3.5 that can solve user problems by providing suitable sanskrit-mantra to chant!! ✨

## Installation

Clone the repository and install the dependencies using [Poetry](https://python-poetry.org/) (you might have to [install Poetry](https://python-poetry.org/docs/#installation) first).

```bash
git clone https://github.com/sanbit876/mantra-gpt.git
cd mantra-gpt
poetry install
```

## Start development server

> If you're using the default template, **remember to set the OpenAI API key** in `main.py`.

Run the following command:

```bash
poetry run python mantra-gpt/textbase_cli.py test main.py
```

Now go to [http://localhost:4000](http://localhost:4000) and start chatting with your bot! The bot will automatically reload when you change the code.
