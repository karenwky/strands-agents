from strands import Agent, tool
from strands_tools import calculator, current_time, python_repl
from strands.models.ollama import OllamaModel

# Define a custom tool as a Python function using the `@tool` decorator
@tool
def letter_counter(word: str, letter: str) -> int: 
    """
    Count occurrences of a specific letter in a word. 

    Args: 
        word (str): The input word to search in
        letter (str): The specific letter to count

    Returns: 
        int: The number of occurrences of the letter in the word
    """
    if not isinstance(word, str) or not isinstance(letter, str): 
        return 0

    if len(letter) != 1: 
        raise ValueError("The 'letter' parameter must be a single character.")

    return word.lower().count(letter.lower())

# Create an Ollama model instance
model = OllamaModel(
    host="http://localhost:11434",  # Ollama server address
    model_id="qwen3:8b"             # Specify which model to use
)

# Create an agent with tools from the `strands-tools`` example tools package, as well as out custom `letter_counter` tool
agent = Agent(
    tools=[
        calculator, 
        current_time, 
        python_repl, 
        letter_counter
    ], 
    model=model
)

# Ask the agent questions that use the available tools
message = """
Complete these tasks: 

1. What is the time right now in Hong Kong?
2. Calculate 45318 / 1212
3. How many letter R in the word "strawberry"🍓?
4. Output a script that does the above tasks, use your python tools to confirm that the script works before outputting it. 
"""
agent(message)
