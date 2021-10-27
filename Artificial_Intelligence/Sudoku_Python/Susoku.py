print("Welcome to Sudoku Solver")
userinput = input("Please enter a file name: ")
path = "D:\\Classes\\Artificial_Intelligence\\Sudoku_Python\\"
file = open(path+userinput)
board = [[0] * 9] * 9
lines = file.readlines()
#Read in file as a 2D array
i=0
for line in lines:
    board[i] = line.split()
    i += 1

def display(board):
    for i in range(9):
        if i == 3 or i == 6:
            print("-----------------------")
        for j in range(9):
            if j == 3 or j == 6:
                print(" | ", end="")
            print(str(board[i][j]) + " ", end="")
        print()

def solve(board):
    return False

def main():
    print("Original Sudoku Puzzles: ")
    display(board)
    #solve(board)
    if(solve(board)):
        print("Solution for the above Sudoku puzzles")
        display(board)
    else:
        print("Unable to solve the Sudoku puzzles")

main()
