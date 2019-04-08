import java.util.Scanner;

import java.util.Arrays;
public class BJ_2839 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
	
		int arr[] = new int[5001];
		Arrays.fill(arr, 0xfffffff);
		
		arr[3] = 1;
		arr[5] = 1;
		
		int num  = sc.nextInt();
		
		if(num <= 5){
			if(arr[num] == 0xfffffff)System.out.println(-1);
			else System.out.println(arr[num]);
			
		}else {
			for(int i = 6; i < num+1; i++) {
		
				
				int three = 0;
				int five = 0;
				
				three = arr[i-3];
				five = arr[i-5];	
				
				if(three == 0xfffffff && five == 0xfffffff)continue;
				if(three >= five) arr[i] = five+1;
				else arr[i] =  three+1;
				
			}
				
			if(arr[num] == 0xfffffff)System.out.println(-1);
			else System.out.println(arr[num]);
		}
	
		
	
	}

}
