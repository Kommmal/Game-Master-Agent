import random
from agents import function_tool

@function_tool
async def roll_dice(sides: int = 6) -> dict:
    """
    Rolls a dice with the given number of sides (default is 6).
    Returns the rolled number.
    Example: roll_dice(20) for a D20.
    """
    try:
        print(f"Rolling a {sides}-sided dice")
        result = random.randint(1, sides)
        return {"roll": result}
    except Exception as e:
        print("Exception in roll_dice tool:", str(e))
        return {"error": str(e)}
