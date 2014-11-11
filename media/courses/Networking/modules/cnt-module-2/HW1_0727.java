import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Random;

/*
 * Author: 0727
 * Data Structures
 * Homework 1
 * 1/15/2014
 */
public class HW1_0727 {
	
	HW1_0727() {
	}
	
	/*
	 * Creates a 3D array of random sizes
	 * Fills each element with a random number [1, 5]
	 */
	public static int[][][] createData() {
		Random rand = new Random();
		int r = rand.nextInt(5) + 1;
		int[][][] array;
		array = new int[r][][];
		
		// Initialize 3D array with random sizes
		for (int i = 0; i < array.length; i++) {
			r = rand.nextInt(5) + 1;
			array[i] = new int[r][];
			
			for (int j = 0; j < array[i].length; j++) {
				r = rand.nextInt(5) + 1;
				array[i][j] = new int[r];
			}
		}
		
		// Assign random values to arrays
		for (int i = 0; i < array.length; i++) {
			
			for (int j = 0; j < array[i].length; j++) {
				
				for (int k = 0; k < array[i][j].length; k++) {
					r = rand.nextInt(5) + 1;
					array[i][j][k] = r;
				}
			}
		}
		return array;
	}
	
	/*
	 * Writes the 3D array to file
	 */
	public static void writeData(int[][][] array, String fileName) {
		FileOutputStream out = null;
		
		try {
			out = new FileOutputStream(fileName);			
		}
		catch (FileNotFoundException e) {
			e.printStackTrace();
			System.exit(1);
		}
		DataOutputStream outs = new DataOutputStream(out);
		
		try {
			outs.writeInt(array.length);
			
			// rows
			for (int i = 0; i < array.length; i++) {
				outs.writeInt(array[i].length);
				
				// columns
				for (int j = 0; j < array[i].length; j++) {
					outs.writeInt(array[i][j].length);
					
					// elements
					for (int k = 0; k < array[i][j].length; k++) {
						outs.writeInt(array[i][j][k]);
					}
				}
			}
		}
		catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	/*
	 * Reads binary data from file and populates new 3D array with it
	 */
	public static int[][][] readData(String fileName) {
		int[][][] array;
		FileInputStream in = null;
		
		try {
			in = new FileInputStream(fileName);
		}
		catch (FileNotFoundException e) {
			e.printStackTrace();
			System.exit(1);
		}
		DataInputStream ins = new DataInputStream(in);
		
		int init, row, col, element;
		try {
			init = ins.readInt();
			array = new int[init][][];
			
			// rows
			for (int i = 0; i < init; i++) {
				row = ins.readInt();
				array[i] = new int[row][];
				
				// columns
				for (int j = 0; j < row; j++) {
					col = ins.readInt();
					array[i][j] = new int[col];
					
					// elements
					for (int k = 0; k < col; k++) {
						element = ins.readInt();
						array[i][j][k] = element;
					}
				}
			}
			return array;
		}
		catch (IOException e) {
			e.printStackTrace();
			array = new int[0][0][0]; // return empty array if issues reading data
			return array;
		}
	}
	
	/*
	 * Display the array
	 */
	public static void printData(int[][][] array) {
		
		for (int i = 0; i < array.length; i++) {
			System.out.println("Frame " + i + ":");
			
			for (int j = 0; j < array[i].length; j++) {
				System.out.print("        ");
				
				for (int k = 0; k < array[i][j].length; k++) {
					System.out.print(array[i][j][k] + " ");
				}
				System.out.println();
			}
		}
	}
	
	/*
	 * Main method as per homework requirement
	 */
	public static void main(String[] args) throws FileNotFoundException, IOException {
		int[][][] data;
		data = createData();
		printData(data);
		writeData(data, "data.out");
		data = readData("data.out");
		printData(data);
	}
}
