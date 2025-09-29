from langgraph.graph import StateGraph, END
from ..state import StateModel
from ..nodes import llm_node

def create_graph():
    graph = StateGraph(StateModel)
    graph.add_node("llm", llm_node)
    graph.set_entry_point("llm")
    graph.add_edge("llm", END)
    return graph.compile()

def agent_node(state):
    return {"messages": state["messages"] + ["Hello from agent"]}
