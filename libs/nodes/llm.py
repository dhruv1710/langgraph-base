from langchain.chat_models import init_chat_model

llm = init_chat_model(
    "anthropic.claude-3-5-sonnet-20240620-v1:0",
    model_provider="bedrock_converse",
)

def llm_node(state):
    messages = state["messages"]
    response = llm.invoke(messages)
    return {"messages": [response]}