import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.*;
public class MainTSP {
	public static int numCities;
	public static int[][] Distance;
	public static ArrayList<ArrayList<Integer>> Population;
	public static int[] individual;
	public static int populationSize = 100;
	public static int numCreatedPop = 500;

	public static void main(String[] args) {
		System.out.println( "Please enter a file name: " );
		Scanner scanner = new Scanner(System.in);
		String fileName = scanner.nextLine();
		scanner.close();
		FileReader f = null;
		try
		{
			f = new FileReader(fileName);
		}
		catch(FileNotFoundException e)
		{
			System.out.println("Invalid File");
			System.exit(1);
		}
		Scanner reader = new Scanner(f);
		
		//Read in the file as a 2D array
		numCities = reader.nextInt();
		Distance = new int[numCities][numCities];
		for (int i = 0; i < Distance.length; i++) {
			for(int j = 0; j < Distance[0].length; j++) {
				Distance[i][j] = reader.nextInt();
			}
		}
		int[][] initialPop = getInitialPop();

		int[][] ans = new int[numCreatedPop][initialPop[0].length];
		int ansIndex = 0;
		for(int i = 0; i < numCreatedPop; i++) {
			initialPop = getNewPop(initialPop);
			//ans.add(sortedPopulation(initialPop)[0]);
			ans[ansIndex] = sortedPopulation(initialPop)[0].clone();
			ansIndex++;
		}
		ans = sortedPopulation(ans);
		
		for(int i = 0; i<ans.length; i++) {
			System.out.println(Arrays.toString(ans[i]) + ": " + fitness(Distance,ans[i]));
		}
		//System.out.println(Arrays.deepToString(ans));
		//System.out.println(fitness(Distance, ans[0]));
	}
	
	public static int[][] getInitialPop(){
		//numCities
		ArrayList<Integer> a = new ArrayList<>();
		for(int i = 0; i < numCities; i++)
			a.add(i);
		//populationSize
		int[][] initialPop = new int[populationSize][numCities];
		for(int i = 0; i < populationSize; i++) {
			Collections.shuffle(a);
			for(int j = 0; j < numCities; j++) {
				initialPop[i][j] = a.get(j);
			}
		}
		return initialPop;
	}
	public static int[][] getNewPop(int[][] initialPop){
		int[][] newPop = new int[initialPop.length][initialPop[0].length];
		int index = 0;
		while(index < initialPop.length) {
			
			int[][] bestPop = selectBest(initialPop);
			int[][] XYCrossover = crossOver(bestPop[0], bestPop[1]);
			newPop[index] = XYCrossover[0].clone();
			if(index + 1 == initialPop.length)
				break;
			newPop[index+1] = XYCrossover[1].clone();
			index += 2;
		}
		
		return newPop;
	}
	
	public static int weightedRandom(int[][] items) {
		Random random = new Random();
		int r = random.nextInt(items.length*(items.length+1)/2) + 1;
		int index = -1;
		for(int i = 1; i<= items.length; i++) {
			r -= i;
			if(r <= 0) {
				index = i;
				break;
			}
		}
		return index-1;
	}
	
	public static int[][] sortedPopulation(int[][] population){
//		TreeMap<Integer, int[]> compare = new TreeMap<>();
//		
//		for(int i = 0; i < population.length; i++) {
//			compare.put(fitness(Distance, population[i]), population[i].clone());
//		}
//		int index = 0;
//		for (int[] a: compare.values()) {
//			population[index] = a;
//			index++;
//		}
		Comparator<int[]> c = (int[] a, int[] b) -> fitness(Distance, a) - fitness(Distance, b);
		Arrays.sort(population, c);
		return population;
	}
	
	//Choose 2 paths with the lowest distance to perform cross over
	public static int[][] selectBest(int[][] population){
		int[][] answer = new int[2][population[0].length];
		population = sortedPopulation(population);
		//System.out.println(Arrays.deepToString(population));
		
		int index0 = population.length - 1 - weightedRandom(population);
		int index1 = population.length - 1 - weightedRandom(population);
		
		answer[0] = population[index0].clone();
		answer[1] = population[index1].clone();

		return answer;
	}
	
	//Perform cross over of the 2 paths with the lowest fitness distance
	public static int[][] crossOver(int[] x, int[]y){
		int[][] answer = new int[2][x.length];
		Random r = new Random();
		int startIndex = r.nextInt((x.length/2)+1);
		int endIndex = startIndex + x.length/2 - 1;
		HashMap<Integer, Integer> mapX = new HashMap<>();
		HashMap<Integer, Integer> mapY = new HashMap<>();
		
		for (int i = 0; i< x.length; i++) {
			mapX.put(x[i], i);
			mapY.put(y[i], i);
		}
		Comparator<Integer> compareX = (Integer a, Integer b) -> mapY.get(a) - mapY.get(b);
		Comparator<Integer> compareY = (Integer a, Integer b) -> mapX.get(a) - mapX.get(b);
		
		ArrayList<Integer> sortedX = new ArrayList<>();
		ArrayList<Integer> sortedY = new ArrayList<>();
		
		for(int i = 0; i<x.length; i++) {
			if(i < startIndex || i > endIndex) {
				sortedX.add(x[i]);
				sortedY.add(y[i]);
			}			
		}
		
		Collections.sort(sortedX, compareX);
		Collections.sort(sortedY, compareY);
		int numXremains = 0, numYremains = 0;
		for(int i = 0; i<x.length; i++) {
			if (i < startIndex || i > endIndex) {
				if(numXremains < sortedX.size() && numYremains < sortedY.size()) {
					x[i] = sortedX.get(numXremains);
					y[i] = sortedY.get(numYremains);
					numXremains++;
					numYremains++;
				}
			}
		}
		
		answer[0] = x.clone();
		answer[1] = y.clone();
		
		return answer;
	}
	
	//Compute the factorial of cities, the maximum number of paths
	public static long factorial (int number) {
		long result = 1;
		for (int factor = 2; factor <= number; factor++) {
			result *= factor;
		}
		return result;
	}
	
	//Calculate the fitness of each individual
	public static int fitness(int[][] dist, int[] arr) {
		int fitness = 0;
		for (int i = 0; i< arr.length; i++) {
			int y = i+1;
			if (y < arr.length)
				fitness += (long)dist[arr[i]][arr[y]];
			//Loop back to the first city
			else 
				fitness += (long)dist[arr[i]][arr[0]];
		}
		return fitness;
	}
	
	//Mutating another individual
	public static List<Integer> mutate(List<Integer> a) {
		ArrayList<Integer> newArr = new ArrayList<>();
		Random rand = new Random();
		int random;
		
		int size = a.size();
		for(int i = 0; i<size; i++) {
			random = rand.nextInt(a.size());
			newArr.add(a.get(random));
			a.remove(random);
		}
		//System.out.println(Arrays.toString(newArr.toArray()));
		return newArr;
	}

}
