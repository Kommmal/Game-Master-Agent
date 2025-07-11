from agents import Runner, Agent, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
import os
from dotenv import load_dotenv
from tools import roll_dice, generate_event

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)


narrator_agent = Agent(
    name="NarratorAgent",
    instructions="""
    You are the narrator of a fantasy text adventure game.
    Based on player choices, progress the story. Occasionally, call generate_event to surprise the player.
    Always end with a choice (e.g., 'Do you enter the cave or run away?').
    """,
    tools=[generate_event],
)


monster_agent = Agent(
    name="MonsterAgent",
    instructions="""
    You're the combat master. When combat starts, describe the monster, roll dice using the roll_dice tool,
    and determine if the player wins or loses.
    Example: 'You face a goblin. Rolling dice... You rolled 17, the goblin rolls 9. You win!'
    """,
    tools=[roll_dice],
)


item_agent = Agent(
    name="ItemAgent",
    instructions="""
    You are the item and loot master. Grant players magical items, health potions, gold, or weapons
    based on the outcome of an event or battle.
    Keep track of inventory in memory (for now, just output text).
    """,
)


def main():
    print("🧙 Welcome to Fantasy Adventure!\n")
    story = "You wake up in a ruined village. Smoke rises in the distance."
    while True:
        print("\nStory: ", story)
        player_input = input("\nYour move: ")

        # 1. Narration step
        result1 = Runner.run_sync(
        narrator_agent,
        player_input, 
        run_config=config
    )
        story = result1.final_output.strip()
        print("\nNarrator:", story)

        # Trigger battle?
        if "goblin" in story.lower() or "dragon" in story.lower():
            result2 = Runner.run_sync(
            monster_agent,
            "combat", 
            run_config=config
        )
            print("\nMonster Agent:", result2.final_output)

            result3 = Runner.run_sync(
            item_agent, 
            "grant loot", 
            run_config=config
        )
            print("\nItem Agent:", result3.final_output)

        # Exit condition
        if any(x in player_input.lower() for x in ["exit", "quit", "end"]):
            print("👋 Farewell, brave adventurer!")
            break

if __name__ == "__main__":
    main()

