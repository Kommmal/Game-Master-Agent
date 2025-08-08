from agents import Agent, handoff
from setup_config import model
from agents import Agent
from utils.handoff import orchestrator_handoff
from expert.item_agent import item_agent
from expert.monster_agent import monster_agent
from expert.narrator_agent import narrator_agent

orchestrator_agent = Agent(
    name="OrchestratorAgent",
    instructions="""
    You are the Orchestrator controlling the flow of the adventure game.  
    You never generate story content yourself.  
    Always respond in English only.

    Your job is to read the user's messages and the latest events, then hand off control to the correct agent:  

    - When the user says "start", hand off control to NarratorAgent to begin the story.  
    - When the event involves a monster, hand off control to MonsterAgent to handle combat.  
    - When the event involves an item, win a combat hand off control to ItemAgent to handle item interactions.
    - If combat ends with player defeat, hand off to NarratorAgent.
    - If combat ends with monster defeat, hand off to ItemAgent.  
    - Otherwise, hand off control to NarratorAgent to continue the story.  

    Always wait for the user's input before passing control to the next agent.  
    """,
    model=model,
    handoffs=[
        handoff(agent=narrator_agent, on_handoff=orchestrator_handoff(narrator_agent)),
        handoff(agent=monster_agent, on_handoff=orchestrator_handoff(monster_agent)),
        handoff(agent=item_agent, on_handoff=orchestrator_handoff(item_agent)),
    ],
)
