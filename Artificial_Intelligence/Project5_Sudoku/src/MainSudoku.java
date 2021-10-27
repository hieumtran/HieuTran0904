import java.util.*;
import java.io.*;

public class MainSudoku {
	public static final int EMPTY = 0;
	public static final int SIZE = 9;
	
	public static void main(String[] args) {
		System.out.println( "Please enter a file name: " );
		Scanner input = new Scanner(System.in);
		String fileName = input.nextLine();
		input.close();
		FileReader f = null;
		try {
			f = new FileReader(fileName);
		}
		catch(FileNotFoundException e) {
			System.out.println("Invalid file");
			System.exit(1);
		}
		Scanner reader = new Scanner(f);
		
		//Read in the file as a 2D array
		int[][] board = new int[9][9];
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				board[i][j] = reader.nextInt();
			}
		}
		
		//Show the initial Sudoku puzzles board
		System.out.println("The Initial Sudoku Puzzles: ");
		displayBoard(board);
		System.out.println("\n");
		
		if(solve(board)) {
			System.out.println("Solution for the above Sudoku puzzles");
			displayBoard(board);
		}
		else
			System.out.println("Unable to solve the Sudoku puzzles");
		reader.close();
	}
	
	// Method to print out the sudoku puzzles
	public static void displayBoard(int[][] board) {
		System.out.println("-------------------");
		for (int i = 0; i < 9; i++) {
			if (i == 3 || i == 6)
				System.out.println("-------------------");
			for(int j = 0; j < 9; j++) {
				if (j == 3 || j == 6)
					System.out.print("|");
				System.out.print(board[i][j] + " ");
			}
			System.out.println(); 
		}
		System.out.println("-------------------");
	}

	// Method to check if a number is already in a row
	public static boolean isInRow(int row, int number, int[][] board) {
		for(int i = 0; i < SIZE; i++) {
			if(board[row][i] == number)
				return true;
		}
		return false;
	}
	
	// Method to check if a number is already in a columnn
	public static boolean isInCol(int col, int number, int[][] board) {
		for(int i = 0; i < SIZE; i++) {
			if(board[i][col] == number)
				return true;
		}
		return false;
	}
	
	// Method to check if a number is already in a 3x3 grid of a specific row and column
	public static boolean isInSmallGrid (int row, int col, int number, int[][] board) {
		int r = row - row%3;
		int c = col - col%3;
		for (int i = r; i < r+3; i++) {
			for (int j = c; j < c+3; j++) {
				if (board[i][j] == number)
					return true;
			}
		}
		return false;
	}

	// Method to check if a number is good to be in a specific position. 
	// Returns true if the row, column, and 3x3 grid the number is in does not already have that number
	public static boolean isGoodToPlace (int row, int col, int number, int[][] board) {
		return !isInRow(row, number, board) && !isInCol(col, number, board) && !isInSmallGrid(row, col, number, board);
	}
		
	// Method to solve the Sudoku puzzles
	public static boolean solve(int[][] board) {
		for (int row = 0; row < SIZE; row++) {
			for (int col = 0; col < SIZE; col++) {
				if(board[row][col] == EMPTY) {
					for(int number = 1; number <= 9; number++) {
						if(isGoodToPlace(row, col, number, board)) {
							board[row][col] = number;
							if(solve(board))  //Calling solve on the new board with added number
								return true;
							else
								board[row][col] = EMPTY; // Reset the last position to 0 because it is not a solution
						}
					}
					return false;
				}
			}
		}
		return true;
	}
}

