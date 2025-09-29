from libs.graph import create_graph

def main():
    graph = create_graph()
    
    config = {"configurable": {"thread_id": "1"}}
    
    result = graph.invoke(
        {"messages": [("user", "Hello!")]}, 
        config=config
    )
    print(result["messages"])

if __name__ == "__main__":
    main()
