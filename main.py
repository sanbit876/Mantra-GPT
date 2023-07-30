import textbase
from textbase.message import Message
from textbase import models
from typing import List

# Load your OpenAI API key
models.OpenAI.api_key = "API-KEY"

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = "Act as a Sanskrit-Guru and provide a Sanskrit Mantra which can solve the problem that will be specified by me in the next response"


@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information

    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """

    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1

    # # Generate GPT-3.5 Turbo response
    bot_response = models.OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
    )

    return bot_response, state