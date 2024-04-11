"""
This code is mainly used to run some basic test cases to make sure the code covers all the use cases.
The following use cases are tested
1. grid is empty: raise error
2. block must be among the following: AssertionError: Block Type must be among the following: I, J, L, Q, Z, S, T
3. Testing good examples of input fro the grid
"""
import unittest

from tetris_impl import Blocks, Grid

WIDTH = 10
HEIGHT = 100


class BadGrid(unittest.TestCase):
    """Making sure the grid is initialised with minimum dimension required""" 
    def test_bad_width_grid(self):     
        with self.assertRaises(Exception) as context:
            grid = Grid(2, 20)
        self.assertTrue('Width must be greater than 4 to accomodate all possible block type' in str(context.exception))

    def test_bad_height_grid(self):        
        with self.assertRaises(Exception) as context:
            grid = Grid(10, 2)
        self.assertTrue('Height must be greater than 4 to accomodate all possible block type' in str(context.exception))


class BadBlockType(unittest.TestCase):
    """ Test to ensure bad block_types cannot be initialized"""
    def test_bad_block_type(self):
        with self.assertRaises(Exception) as context:
            block = Blocks(1, 1, "C")
        self.assertTrue('Block Type must be among the following: I, J, L, Q, Z, S, T' in str(context.exception))

class TestGoodInput(unittest.TestCase):
    def test_one_block_multiple_cases(self):
        """ Test to ensure a grid can be re-used for successive cases"""
        lines = [[("Q", 1)], [("Q", 1)]]
        for line in lines:
            grid = Grid(WIDTH, HEIGHT)
            for move in line:
                block = Blocks(move[1], 0, move[0])
                grid.NewBlock(block)
                grid.BlockToMatrix()
                grid.BlockNaturalDrop()
                grid.CheckFullRow()
            score = grid.GetHeight()
            self.assertTrue(score, 2)

    def test_one_block(self):
        """ Test to ensure a grid can be used for only one input with one block"""
        lines = [[("Q", 1)]]
        for line in lines:
            grid = Grid(WIDTH, HEIGHT)
            for move in line:
                block = Blocks(move[1], 0, move[0])
                grid.NewBlock(block)
                grid.BlockToMatrix()
                grid.BlockNaturalDrop()
                grid.CheckFullRow()
        score = grid.GetHeight()
        self.assertTrue(score, 2) 
    
    def test_multiple_block(self):
        """ Test to ensure a grid can be used for only one input with multiple block"""
        lines = [[("Q", 1), ("Q", 4), ("Q", 7), ("L", 0), ("T", 2), ("T", 5), ("J", 8), ("Q", 1), ("Q", 3), ("Q", 5), ("Q", 7)]]
        for line in lines:
            grid = Grid(WIDTH, HEIGHT)
            for move in line:
                block = Blocks(move[1], 0, move[0])
                grid.NewBlock(block)
                grid.BlockToMatrix()
                grid.BlockNaturalDrop()
                grid.CheckFullRow()
            score = grid.GetHeight()
            self.assertTrue(score, 2)

    def test_overflow_block(self):
        """ Test to ensure a grid can handle when the input results in the overflow"""
        lines = [[("Q", 1) for i in range(100)]]
        for line in lines:
            grid = Grid(WIDTH, HEIGHT)
            for move in line:
                block = Blocks(move[1], 0, move[0])
                grid.NewBlock(block)
                grid.BlockToMatrix()
                grid.BlockNaturalDrop()
                grid.CheckFullRow()
                if grid.CheckLoss():
                    break
            score = grid.GetHeight()
            self.assertTrue(score, 100)  

def main():
    unittest.main()

if __name__ == "__main__":
    main()