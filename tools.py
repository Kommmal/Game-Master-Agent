import random
from agents import function_tool

@function_tool
def roll_dice() -> int:
    """Roll a 20-sided dice and return the result."""
    return random.randint(1, 20)


@function_tool
def generate_event() -> str:
    """Generate a random fantasy event."""
    events = [
        "You stumble into a dark forest.",
        "A mysterious merchant appears.",
        "You find a glowing sword stuck in a rock.",
        "A wild goblin jumps from the bushes!",
    ]
    return random.choice(events)