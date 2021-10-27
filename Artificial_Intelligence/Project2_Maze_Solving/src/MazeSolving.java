import java.io.*;
import java.util.*;

public class MazeSolving {
	public static char[][] maze;
	
	public static void main(String[] args) throws IOException {
		int height; //number of rows
		int width;	//number of columns
		char[][]maze = null;
		
		/*-------------Determine if the file is valid---------------*/
		System.out.println("Please enter a file name: ");
		Scanner input = new Scanner(System.in);
		String fileName = input.nextLine();
		
		FileReader f = null;
		input.close();
		try {
			f = new FileReader(fileName);     
		}
		catch(FileNotFoundException e) {
			System.out.println("Invalid File");
			System.exit(1);
		}
		Scanner reader = new Scanner(f);
		
		
		/*---------------------------Begin---------------------------*/		
		System.out.println("Welcome to Maze Solving!\n");
		
		//Getting the number of rows and columns of the given maze
		String size = reader.nextLine();
		String[] dimensions = size.split("\\s+");
		height = Integer.parseInt(dimensions[0]);
		width = Integer.parseInt(dimensions[1]);
		
		
		//initialize 2D array maze
		maze = new char[height][width]; 
		
		
		//Filling maze with #'s from input files
		String line = null;
        ArrayList<String> lines = new ArrayList<String>();
        while (reader.hasNextLine( ))
		{
			lines.add(reader.nextLine());
		}
        reader.close();
        
        int j = 0;
        for (int k = 0; k < lines.size(); k++)
		{
			line = lines.get(k);
			char[] ch = line.toCharArray();
			
			for (int i = 0; i< ch.length;i++)
			{
				maze[j][i] = ch[i];
			}
			j++;
		}
        
        /*-----------------------------------------------------------*/
        //Finding start and finish position with 'S' for start and 'G' for goal
        int startRow=0; 
        int startCol=0;
        ArrayList<String> startPath = new ArrayList<>();

        for (int i = 0; i<height ;i++)
        {
        		if (maze[i][0] == ' ')
        		{
        			maze[i][0] = 'S';
        			startCol = 0;
        			startRow = i;
        		}
        		if (maze[i][width-1] == ' ')
        		{
        			maze[i][width-1] = 'G';
        		}
        }

        Solver solver = new Solver(maze, startRow, startCol, startPath, false);
        //solver.placePlus();
        solver.solveMaze();
        if (solver.unsolvable) {
            System.out.println("The maze is unsolvable");
        } else {
            System.out.println("The path is: \n" );
        }
        solver.printMaze();

	}

}