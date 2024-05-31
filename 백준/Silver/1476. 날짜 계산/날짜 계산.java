import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int E = sc.nextInt();
		int S = sc.nextInt();
		int M = sc.nextInt();
		
		if (E == 15) E = 0;
	    if (S == 28) S = 0;
	    if (M == 19) M = 0;
	    
	    int i=1;
	    while (true) {
	        if(i%15==E && i%28==S && i%19==M)
	            break;
	        i++;
	    }
	    System.out.println(i);
	}

}
