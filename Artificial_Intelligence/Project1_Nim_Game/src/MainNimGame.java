import java.util.*;

public class MainNimGame {

	public static void main(String[] args) {
		System.out.println("Welcome to the NIM Game! Please pick the number of sticks you want to start with.");
		Scanner input = new Scanner(System.in);
		int numSticks = input.nextInt();
		System.out.println("There are " + numSticks + " sticks. You can only choose 1, 2, or 3 sticks. Let's start!");
		
		Random rand = new Random();
		int compStick = 0;
		int playerStick = 0;
		
		while (numSticks > 0) {
			compStick = rand.nextInt(3) + 1;
			if (numSticks <= 3) {
				compStick = numSticks;
				System.out.println("The computer picks " + numSticks + ". There are 0 stick left. \nSorry, you lose...");
				System.exit(0);
			}
			numSticks -= compStick;
			System.out.println("\nThe computer picks " + compStick + " sticks. There are " + numSticks + " left.");
			System.out.println("How many sticks do you pick? 1, 2 or 3?");
			
			playerStick = input.nextInt();
			while (playerStick > 3 || playerStick < 1) {
				System.out.println("Invalid choice. Please choose again.");
				playerStick = input.nextInt();
			}
			
			numSticks -= playerStick;
			System.out.println("There are " + numSticks + " left.");
			if (numSticks == 0) {
				System.out.println("Congratulations! You Win!");
			}
		}
		System.out.println("\nGAME OVER");
		input.close();
	}
}
