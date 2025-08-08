import chainlit as cl
from agents import Runner
from setup_config import config
from expert.narrator_agent import narrator_agent
from expert.monster_agent import monster_agent
from expert.item_agent import item_agent


@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])
    await cl.Message("🧙 Welcome, brave adventurer! Your story begins now...\n reply with start to let the game begins").send()

@cl.on_message
async def handle(msg: cl.Message):
    history = cl.user_session.get("history", [])
    history.append({"role": "user", "content": msg.content})

    thinking = cl.Message("Narrating your next chapter...")
    await thinking.send()

    try:
        result = await Runner.run(
            narrator_agent,   
            history,
            run_config=config
        )

        output = result.final_output

        thinking.content = output
        await thinking.update()

        history = result.to_input_list()
        cl.user_session.set("history", history)

    except Exception as e:
        thinking.content = f"❌ Error: {e}"
        await thinking.update()
