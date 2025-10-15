import logging
import random

from google.adk import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

AGENT_MODEL = 'openai/qwen2.5-72b-instruct'


def roll_die(sides: int) -> int:
    """Roll a die and return the rolled result."""
    logging.info(f"--- Tool: roll_die called, sides={sides} ---")
    return random.randint(1, sides)


root_agent = Agent(
    name="roll_agent",
    model=LiteLlm(model=AGENT_MODEL),
    description="Handles rolling dice of different sizes.",
    instruction="""
      You are responsible for rolling dice based on the user's request.
      When asked to roll a die, you must call the roll_die tool with the number of sides as an integer.
    """,
    tools=[roll_die],
    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(  # avoid false alarm about rolling dice.
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)

a2a_app = to_a2a(root_agent, port=8001)
