# Adjacency Matrix
G = [
    [0, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0]
]

# Node names
node = "abcdef"

# Store node index
t_ = {}

for i in range(len(G)):
    t_[node[i]] = i

# Count degree of each node
degree = []

for i in range(len(G)):
    degree.append(sum(G[i]))

# Available colors
colorDict = {}

for i in range(len(G)):
    colorDict[node[i]] = [
        "Blue",
        "Red",
        "Yellow",
        "Green"
    ]

# Sort nodes according to degree
sortedNode = []
indeks = []

# Selection sort
for i in range(len(degree)):

    _max = 0

    for j in range(len(degree)):

        if j not in indeks:

            if degree[j] > _max:
                _max = degree[j]
                idx = j

    indeks.append(idx)
    sortedNode.append(node[idx])

# Main process
theSolution = {}

for n in sortedNode:

    setTheColor = colorDict[n]

    # Assign first available color
    theSolution[n] = setTheColor[0]

    adjacentNode = G[t_[n]]

    for j in range(len(adjacentNode)):

        if (
            adjacentNode[j] == 1
            and (
                setTheColor[0]
                in colorDict[node[j]]
            )
        ):
            colorDict[node[j]].remove(
                setTheColor[0]
            )

# Print solution
for t, w in sorted(theSolution.items()):
    print(
        "Node",
        t,
        "=",
        w
    )

'''
OUTPUT :
Node a = Yellow
Node b = Blue
Node c = Red
Node d = Yellow
Node e = Blue
Node f = Red
'''