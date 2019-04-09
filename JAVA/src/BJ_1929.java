import java.util.Scanner;
import java.util.Arrays;
public class BJ_1929 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		int max = Math.max(a, b);
		int min = Math.min(a,b);
		
		boolean[] arr = new boolean[max+1]; 
		Arrays.fill(arr, true);
		int s = (int)Math.sqrt(max)+1;
		
		arr[1] = false;
		
		for(int i=2 ;  i< s+1 ; i++){
			for(int j = 2; i*j<=max; j++)
				arr[i*j] = false;	
		}
		for(int i=min; i<max+1;i++) {
			if(arr[i]==true)System.out.println(i);
		}			
	}

}
