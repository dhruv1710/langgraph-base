from langgraph.graph import StateGraph, END
from ..state import StateModel
from ..nodes import llm_node
from ..utils import get_checkpointer

def create_graph():
    graph = StateGraph(StateModel)
    graph.add_node("llm", llm_node)
    graph.set_entry_point("llm")
    graph.add_edge("llm", END)
    return graph.compile(checkpointer=get_checkpointer())

def agent_node(state):
    return {"messages": state["messages"] + ["Hello from agent"]}
