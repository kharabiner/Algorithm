import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
        
		int[] numbers = new int[5];
		for(int i = 0; i<5; i++)
			numbers[i] = scanner.nextInt();
		
		while(numbers[0]!=1 || numbers[1]!=2 || numbers[2]!=3 || numbers[3]!=4 || numbers[4]!=5) {
			for(int i = 0; i < 4; i++) {
				if(numbers[i]>numbers[i+1]) {
					swap(numbers, i, i+1);
					printArray(numbers);
				}
			}
		}
        
        
        
        scanner.close(); 
	}
	
	static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
	static void printArray(int[] arr) {
		int n = arr.length;
		for(int i = 0; i < n; i++)
			System.out.print(arr[i]+" ");
		System.out.println();
	}
}
