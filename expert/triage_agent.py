from agents import Agent, handoff
from setup_config import model
from tools.event_generator_tool import generate_event
from expert.narrator_agent import narrator_agent
from expert.item_agent import item_agent
from expert.monster_agent import monster_agent
from utils.handoff import orchestrator_handoff

triage_agent = Agent(
    name="TriageAgent",
    instructions="""
    You are the Triage Agent, the central controller in a fantasy text-based adventure game.

    🎯 Your Role:
    - Receive events or plot twists from other agents.
    - Use `generate_event()` to retrieve the next story moment.
    - Decide the correct agent to handle the next step:

    ⚔️ If the event includes a MONSTER → handoff to MonsterAgent.
    🎁 If the event includes a WIN or ITEM → handoff to ItemAgent.
    📖 For all other general story progress → handoff to NarratorAgent.

    🔁 Rules:
    - Always use the `generate_event()` tool to fetch the next story moment.
    - Never narrate, reward, or battle directly.
    - Just route the user to the correct agent based on the event content.

    """,
    tools=[generate_event],
    model=model,
    handoffs=[
        handoff(agent=narrator_agent, on_handoff=orchestrator_handoff(narrator_agent)),
        handoff(agent=monster_agent, on_handoff=orchestrator_handoff(monster_agent)),
        handoff(agent=item_agent, on_handoff=orchestrator_handoff(item_agent)),
    ]
)
