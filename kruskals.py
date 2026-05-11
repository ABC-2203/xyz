class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # Add edge
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # Find set of an element (Path Compression)
    def find(self, parent, i):

        if parent[i] == i:
            return i

        return self.find(parent, parent[i])

    # Union of two sets (Union by Rank)
    def union(self, parent, rank, x, y):

        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot

        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # Kruskal Algorithm
    def KruskalMST(self):

        result = []

        # Index for sorted edges
        i = 0

        # Count selected edges
        e = 0

        # Sort edges according to weight
        self.graph = sorted(
            self.graph,
            key=lambda item: item[2]
        )

        parent = []
        rank = []

        # Create subsets
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Select V-1 edges
        while e < self.V - 1:

            # Pick smallest edge
            u, v, w = self.graph[i]
            i += 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            # If no cycle
            if x != y:

                e += 1
                result.append([u, v, w])

                self.union(
                    parent,
                    rank,
                    x,
                    y
                )

        minimumCost = 0

        print("Edges in constructed MST")

        for u, v, weight in result:
            minimumCost += weight

            print(
                "%d -- %d == %d"
                % (u, v, weight)
            )

        print(
            "Minimum Spanning Tree",
            minimumCost
        )


# Driver code
g = Graph(4)

g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.KruskalMST()

'''
OUTPUT:
Edges in constructed MST
2 -- 3 == 4
0 -- 3 == 5
0 -- 1 == 10
Minimum Spanning Tree 19
'''