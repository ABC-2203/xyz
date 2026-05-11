class Node:
    def __init__(self, data, level, fval):
        """
        Initialize the node with the data,
        level of the node and the calculated fvalue
        """
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        """
        Generate child nodes by moving the blank space
        in four directions: left, right, up, down
        """
        x, y = self.find(self.data, '_')

        # Possible positions for movement
        val_list = [
            [x, y - 1],  # left
            [x, y + 1],  # right
            [x - 1, y],  # up
            [x + 1, y]   # down
        ]

        children = []

        for i in val_list:
            child = self.shuffle(
                self.data,
                x, y,
                i[0], i[1]
            )

            if child is not None:
                child_node = Node(
                    child,
                    self.level + 1,
                    0
                )
                children.append(child_node)

        return children

    def shuffle(self, puz, x1, y1, x2, y2):
        """
        Move blank space and return new puzzle
        """

        if (
            x2 >= 0 and
            x2 < len(self.data) and
            y2 >= 0 and
            y2 < len(self.data)
        ):

            temp_puz = self.copy(puz)

            # Swap tiles
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp

            return temp_puz

        else:
            return None

    def copy(self, root):
        """
        Create a copy of puzzle matrix
        """
        temp = []

        for i in root:
            t = []

            for j in i:
                t.append(j)

            temp.append(t)

        return temp

    def find(self, puz, x):
        """
        Find position of blank space '_'
        """
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if puz[i][j] == x:
                    return i, j


class Puzzle:
    def __init__(self, size):
        """
        Initialize puzzle
        """
        self.n = size
        self.open = []
        self.closed = []

    def accept(self):
        """
        Accept puzzle input from user
        """
        puz = []

        for i in range(self.n):
            temp = input().split(" ")
            puz.append(temp)

        return puz

    def f(self, start, goal):
        """
        f(x) = h(x) + g(x)
        """
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        """
        Calculate number of misplaced tiles
        """
        temp = 0

        for i in range(self.n):
            for j in range(self.n):

                if (
                    start[i][j] != goal[i][j]
                    and start[i][j] != '_'
                ):
                    temp += 1

        return temp

    def process(self):
        """
        Start solving puzzle
        """

        print("Enter the start state matrix:")
        start = self.accept()

        print("Enter the goal state matrix:")
        goal = self.accept()

        start = Node(start, 0, 0)
        start.fval = self.f(start, goal)

        # Add start node to open list
        self.open.append(start)

        print("\n")

        while True:

            cur = self.open[0]

            print("")
            print(" | ")
            print(" | ")
            print(" \\/")
            print(" V ")

            # Print current state
            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")

            # Goal state reached
            if self.h(cur.data, goal) == 0:
                break

            # Generate children
            for i in cur.generate_child():
                i.fval = self.f(i, goal)
                self.open.append(i)

            self.closed.append(cur)

            # Remove current node
            del self.open[0]

            # Sort open list by f value
            self.open.sort(
                key=lambda x: x.fval,
                reverse=False
            )


# Driver code
puz = Puzzle(3)
puz.process()

'''
OUTPUT:
Enter the start state matrix:
1 2 3
_ 4 6
7 5 8
Enter the goal state matrix:
1 2 3
4 5 6
7 8 _



 | 
 | 
 \/
 V 
1 2 3 
_ 4 6 
7 5 8 

 | 
 | 
 \/
 V 
1 2 3 
4 _ 6 
7 5 8 

 | 
 | 
 \/
 V 
1 2 3 
4 5 6 
7 _ 8 

 | 
 | 
 \/
 V 
1 2 3 
4 5 6 
7 8 _ 
'''