from typing_extensions import Annotated, TypedDict
from langgraph.graph.message import add_messages

class StateModel(TypedDict):
    messages: Annotated[list, add_messages]