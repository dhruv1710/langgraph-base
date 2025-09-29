from langchain_core.tools import tool

@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together.
    
    Args:
        a: First number to add
        b: Second number to add
        
    Returns:
        The sum of a and b
    """
    return a + b

def adding_tool_node(state):
    messages = state["messages"]
    
    # Extract numbers from the last message (simple example)
    # In a real implementation, you'd parse the message for numbers
    last_message = messages[-1] if messages else ""
    
    # For demo purposes, let's say we add 5 + 3
    result = add_numbers.invoke({"a": 5, "b": 3})
    
    return {"messages": [f"Adding result: {result}"]}
