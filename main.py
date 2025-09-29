from libs.graph import create_graph

def main():
    graph = create_graph()
    result = graph.invoke({"messages": []})
    print(result["messages"])

if __name__ == "__main__":
    main()
