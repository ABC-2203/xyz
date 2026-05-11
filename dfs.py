from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark current node as visited
        visited.add(v)
        print(v, end=' ')

        # Recur for all adjacent vertices
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # Function to do DFS traversal
    def DFS(self, v):

        # Create a set to store visited nodes
        visited = set()

        # Call recursive helper function
        self.DFSUtil(v, visited)


# Driver code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(2)

'''
OUTPUT:
Following is DFS from (starting from vertex 2)
2 0 1 3 
'''