import os
from dotenv import load_dotenv
from typing import cast
from agents import  OpenAIChatCompletionsModel, AsyncOpenAI, handoff
from agents.run import RunConfig

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
        api_key = gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.5-flash",
    openai_client= external_client
)

config = RunConfig(
    model = model,
    model_provider=external_client,
    tracing_disabled= True
)
