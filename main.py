from tetris_impl import Grid, Blocks
import argparse
import os
import sys

def read_input(file_path):
    file = open(file_path, 'r')
    individual_line = []
    while True:
        line = file.readline()
        if not line:
            break
        individual_line.append([(x[0], int(x[1:])) for x in line.replace("\n", "").split(",")])
    return individual_line

def update_output(output_filepath, score):
    print(score)
    with open(output_filepath, 'a') as file:
        file.write(f"{score}\n")
    file.close()

def main():
    """
    Loops through the text file one line at a time
    """
    parser = argparse.ArgumentParser(description='Tetris engine!')
    parser.add_argument('-i','--input', help='Input file path, defaults to input.txt in current folder', default="input.txt")
    parser.add_argument('-o','--output', help='Output file path, defaults to output.txt in current folder', default="output.txt")
    parser.add_argument('-wt','--grid_width', help='Input file path, defaults to input.txt in current folder', default=10, type=int)
    parser.add_argument('-ht','--grid_height', help='Output file path, defaults to output.txt in current folder', default=100, type=int)
    args = vars(parser.parse_args())

    file_path = args["input"]
    if not os.path.exists(file_path):
        print("Could not find input file: ", file_path)
        sys.exit()
        
    output_filepath = args["output"]
    if os.path.exists(output_filepath):
        print("Deleting output from previous run: ", output_filepath)
        os.remove(output_filepath)

    WIDTH = args["grid_width"]
    HEIGHT = args['grid_height']


    lines = read_input(file_path)
    for line in lines:
        grid = Grid(WIDTH, HEIGHT)
        for move in line:
            block = Blocks(move[1], 0, move[0])
            grid.NewBlock(block)
            grid.BlockToMatrix()
            grid.BlockNaturalDrop()
            grid.CheckFullRow()
            if grid.CheckLoss():
                print("OUT of scope: Results in crash")
                break
        score = grid.GetHeight()
        update_output(output_filepath, score)  

if __name__ == "__main__":
    main()
