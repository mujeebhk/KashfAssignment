# Python3 implementation to build a
# graph using Dictionaries
"""
from collections import defaultdict
 
# Function to build the graph
def build_graph():
    edges = [
        ["A", "B"], ["A", "E"],
        ["A", "C"], ["B", "D"],
        ["B", "E"], ["C", "F"],
        ["C", "G"], ["D", "E"]
    ]
    graph = defaultdict(list)
     
    # Loop to iterate over every
    # edge of the graph
    for edge in edges:
        a, b = edge[0], edge[1]
         
        # Creating the graph
        # as adjacency list
        graph[a].append(b)
        graph[b].append(a)
    return graph
 
if __name__ == "__main__":
    graph = build_graph()
     
    print(graph)

""" 