import java.util.Scanner;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class HelloWorld {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		
		for(int i=0; i<num; i++) {
			int n=sc.nextInt();
			System.out.println(fibo(n) + " " + fibo(n+1));
		}
	}	
	
	public static int fibo(int n){
		if(n==0) return 1;
		if (n==1)return 0;
		
		int a = 1;
		int b = 0;
		int c = 1;
		
		for(int i=0; i<n-2 ;i++){  
			a=b;
			b=c;
			c= a+b;
		}
		
		return c;
	}
}
