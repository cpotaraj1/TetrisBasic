"""
Implementation of both Grid and Blocks can be found here
"""

class Blocks():
    """Implementation of tetris blocks"""

    def __init__(self, x, y, block_type):
        """Attributes for class."""
        assert block_type in ["I", "J", "L", "Q", "Z", "S", "T"], "Block Type must be among the following: I, J, L, Q, Z, S, T"
        self.block_matrix = []
        self.x = x
        self.y = y
        self.block_type = block_type
        self.coords = []
        

    def block_to_matrix(self):
        """Returns a matrix with 0 denoting empty space and 2 denoting occupied space"""
        if self.block_type == "I":
            self.block_matrix = [
                [0, 0, 0, 0],                
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [2, 2, 2, 2]
            ]
        elif self.block_type == "J":
            self.block_matrix = [
                [0, 2, 0],
                [0, 2, 0],
                [2, 2, 0]
            ]
        elif self.block_type == "L":
            self.block_matrix = [
                [2, 0, 0],
                [2, 0, 0],
                [2, 2, 0]
            ]
        elif self.block_type == "Q":
            self.block_matrix = [
                [2, 2],
                [2, 2]
            ]
        elif self.block_type == "Z":
            self.block_matrix = [
                [2, 2, 0],
                [0, 2, 2],
                [0, 0, 0]
            ]
        elif self.block_type == "S":
            self.block_matrix = [
                [0, 2, 2],
                [2, 2, 0],
                [0, 0, 0]
            ]
        elif self.block_type == "T":
            self.block_matrix = [
                [2, 2, 2],
                [0, 2, 0],
                [0, 0, 0]
            ]
        return self.block_matrix

    def block_to_tuples(self, matrix=None):
        """Returns a list of tuples (ordered pairs) for block coordinates in (x,y) form."""
        if type(matrix) == type(None):  # if there is no inputted matrix, then the matrix will just be self.matrix
            matrix = self.block_matrix
        self.coords = []
        for i in range(len(matrix)):
            for z in range(len(matrix[i])):
                if matrix[i][z] != 0:
                    self.coords.append((z + self.x, i + self.y))
        return self.coords
    


class Grid():
    """Represents the tetris grids and the blocks on it."""

    def __init__(self, width, height):
        """
        Attributes for class
        Matrix: 0 means block is empty. 1 means the block is settled. 2 means the block is dropping.
        """
        assert width >= 4, "Width must be greater than 4 to accomodate all possible block type"
        assert height >= 4, "Height must be greater than 4 to accomodate all possible block type"
        self.matrix = [[0 for z in range(width)] for i in range(height)]
        self.width = width
        self.height = height
        self.coords = ""
        self.block_type = ""
        self.block = None

    def NewBlock(self, block):
        """Creates a new block and returns the starting coordinates for that block."""
        for i in self.matrix:
            if 2 in i:
                return
        self.block = block
        self.block.block_to_matrix()

    def BlockToMatrix(self):
        """Updates the matrix with the block."""
        self.coords = self.block.block_to_tuples()
        for h in range(self.height):
            for w in range(self.width):
                if self.matrix[h][w] == 2:
                    self.matrix[h][w] = 0
        for i in self.coords:
            self.matrix[i[1]][i[0]] = 2

    def BlockCompleteDrop(self):
        """Block dropping due to gravity."""
        self.coords = self.block.block_to_tuples()
        # Checks for collision
        for i in self.coords:
            if i[1] == self.height - 1:
                for i in self.coords:
                    self.matrix[i[1]][i[0]] = 1
                return
            if self.matrix[i[1] + 1][i[0]] == 1:
                for i in self.coords:
                    self.matrix[i[1]][i[0]] = 1
                return
        self.block.y += 1
        # print(self.matrix)
        # import pdb; pdb.set_trace()
        self.BlockToMatrix()
        self.BlockNaturalDrop()
        
    def BlockNaturalDrop(self):
        self.BlockCompleteDrop()
        self.CheckFullRow()
        

    def CheckFullRow(self):
        """Checks if there has been a complete row in the game!"""
        for i in range(len(self.matrix)):
            if self.matrix[i] == [1 for x in range(self.width)]:
                del self.matrix[i]
                self.matrix.insert(0, [0 for x in range(self.width)])

    def CheckLoss(self):
        """Checks if the user has stacked tiles up to the top, and ends the game if that is true."""
        if 1 in self.matrix[1]:
            return True
        
    def GetHeight(self):
        for i in range(len(self.matrix)):
            if 1 in self.matrix[i]:
                return self.height - i