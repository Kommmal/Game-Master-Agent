# 🧙 Game Master Agent – Fantasy Adventure Game

Welcome to **Fantasy Adventure**, a dynamic text-based game powered by multiple AI agents! This game immerses you in a rich, branching fantasy world where your choices shape the story.

---

## 🎮 What It Does

This Python application uses the **OpenAI Agent SDK** to simulate a multi-agent role-playing adventure. You interact with a team of AI agents who narrate the story, handle battles, and reward you based on your actions.

---

## 🧠 Key Features

- 🧾 **Narration**: Story unfolds dynamically based on your inputs.
- ⚔️ **Combat System**: Fight monsters using dice-roll logic.
- 🧰 **Inventory Rewards**: Receive magical items and loot after battles.
- 🎲 **Tool Usage**: Includes tools like `roll_dice()` and `generate_event()` for randomness and storytelling twists.
- 🤖 **Agent Handoff**: Automatically switches between specialized agents based on gameplay.

---

## 🔁 Agent Handoff Explained

This game uses **dynamic handoff logic** to shift control between agents based on the story context:

- The **NarratorAgent** runs first to progress the story.
- If the narration mentions keywords like `"goblin"` or `"dragon"`, a **handoff** to:
  - `MonsterAgent` is triggered to handle combat, using the `roll_dice()` tool.
  - After combat, control passes to the `ItemAgent` to reward the player with loot.
- The system smoothly passes between agents using `Runner.run_sync()` with conditional checks.

This handoff system creates a natural flow between storytelling, combat, and rewards — like a true Dungeon Master experience.

---

## 🧩 Agents Overview

| Agent          | Role                                                                 |
|----------------|----------------------------------------------------------------------|
| 🎤 NarratorAgent | Drives the story, provides scenarios, and presents player choices    |
| 🐉 MonsterAgent  | Handles combat, rolls dice, and determines battle outcomes          |
| 💰 ItemAgent     | Rewards player with loot based on achievements or events           |

---

## ⚙️ Tech Stack

- Python 3.11+
- [OpenAI Agent SDK](https://github.com/openai/openai-python)
- [uv](https://pypi.org/project/uv/) – ultra-fast Python package installer
- `dotenv` – for environment variable management

---

## 🚀 Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/Kommmal/Game-Master-Agent.git
   cd Game-Master-Agent

