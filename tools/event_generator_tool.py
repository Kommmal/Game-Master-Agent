import os
from dotenv import load_dotenv
from agents import function_tool, AsyncOpenAI
from setup_config import model

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

client = AsyncOpenAI(
        api_key = gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

@function_tool
async def event_generator() -> dict:
    """
    Generates a random immersive adventure event prompt for the player.
    The event should be short and vivid, setting up a situation where the narrator can offer choices.
    """
    try:
        print("Running event_generator tool")

        prompt = (
        "Generate a short, vivid event for a text-based adventure game in English only. "
        "Do NOT list choices. Just set the scene in 1–2 sentences. "
        "Example: 'You (the player) reach a fork in the road.' "
        "Events can include a monster appearance, finding an item, or a tense scene. "
        "After every two or three tense scene events, generate one event that involves either a monster appearing or an item being found."
        "Make it mysterious or exciting."
        )


        response = await client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[{"role": "user", "content": prompt}]
        )

        return {"event": response.choices[0].message.content.strip()}

    except Exception as e:
        print("Exception in event_generator tool:", str(e))
        return {"error": str(e)}
