import sys


class Graph:

    def __init__(self, vertices):
        self.V = vertices

        # Create graph matrix
        self.graph = [
            [0 for column in range(vertices)]
            for row in range(vertices)
        ]

    # Print MST
    def printMST(self, parent):

        print("Edge \tWeight")

        for i in range(1, self.V):
            print(
                parent[i],
                "-",
                i,
                "\t",
                self.graph[i][parent[i]]
            )

    # Find minimum key vertex
    def minKey(self, key, mstSet):

        min_value = sys.maxsize

        for v in range(self.V):

            if (
                key[v] < min_value
                and mstSet[v] == False
            ):
                min_value = key[v]
                min_index = v

        return min_index

    # Prim's Algorithm
    def primMST(self):

        # Store minimum values
        key = [sys.maxsize] * self.V

        # Store MST
        parent = [None] * self.V

        # First vertex
        key[0] = 0
        parent[0] = -1

        mstSet = [False] * self.V

        for count in range(self.V):

            # Pick minimum vertex
            u = self.minKey(key, mstSet)

            mstSet[u] = True

            # Update adjacent vertices
            for v in range(self.V):

                if (
                    self.graph[u][v] > 0
                    and mstSet[v] == False
                    and key[v] > self.graph[u][v]
                ):

                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)


# Driver code
g = Graph(5)

g.graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

g.primMST()

'''
OUTPUT:
Edge    Weight
0 - 1    2
1 - 2    3
0 - 3    6
1 - 4    5
'''