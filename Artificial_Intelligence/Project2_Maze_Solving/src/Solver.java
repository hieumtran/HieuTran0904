import java.util.*;
public class Solver {
	public char[][]maze;
	public int curRow;
	public int curCol;
	public ArrayList<String> path;
	public boolean unsolvable;
	public Solver(char[][]maze,int startRow, int startCol, ArrayList<String> startPath, boolean noSolution) {
		this.maze = maze;
		curRow = startRow;
		curCol = startCol;
		path = startPath;
		unsolvable = noSolution;
	}
	
	//Check if a move is open
	boolean isOpen(int x, int y) {
		return maze[x][y] == ' ';
	}

	
	//Return true if the 'G' (Goal) char is reached
	boolean PathFound() {
		return ((curCol + 1 < maze[curRow].length) && maze[curRow][curCol + 1] == 'G');
	}
	
	//Go up, right, down, left to search for an open move Depth-First Search
	void solveMaze() {
		//If reach the goal position
		if(PathFound()) return;
		
		//Go up (row - 1)
		else if (curRow - 1 >= 0 && isOpen(curRow-1, curCol)) {
			curRow--;
			maze[curRow][curCol] = '*';
			path.add("up");
			solveMaze();
		}
		
		//Go right (col + 1)
		else if (curCol + 1 < maze[curRow].length && isOpen(curRow, curCol+1)) {
			curCol++;
			maze[curRow][curCol] = '*';
			path.add("right");
			solveMaze();
		}
		
		//Go down (row + 1)
		else if (curRow + 1 < maze.length && isOpen(curRow+1, curCol)) {
			curRow++;
			maze[curRow][curCol] = '*';
			path.add("down");
			solveMaze();
		}
		
		//Go left (col - 1)
		else if (curCol - 1 >= 0 && isOpen(curRow, curCol-1)) {
			curCol--;
			maze[curRow][curCol] = '*';
			path.add("left");
			solveMaze();
		}
		//out of boundaries or hit a dead end
		else {
			//startX and startY does not have any open neighbors
			if(path.size() == 0) {
				System.out.println(path.toString());
				unsolvable = true;
				return;
			}
			else {
				maze[curRow][curCol] = '-';
				goBack();
			}
		}	
	}
	
	void goBack() {
		if(path.size() > 0) {
			maze[curRow][curCol] = '-';
			switch(path.get(path.size()-1)) {
			case "up":
				curRow++;
				break;
			case "right":
				curCol--;
				break;
			case "down":
				curRow--;
				break;
			case "left":
				curCol++;
				break;
			}
			path.remove(path.size()-1);
			solveMaze();
		}
	}
	
	//Print the solution
	void printMaze() {
	    for (int i = 0; i < maze.length; i++) {
	        System.out.println(Arrays.toString(maze[i]));
	    }
	}
	
}