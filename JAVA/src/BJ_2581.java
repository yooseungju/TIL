import java.util.Scanner;
public class BJ_2581 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		int Min = Math.min(a, b);
		int Max = Math.max(a, b);
		
		
		for(int i = Min; i < Max+1; i++) {
			if(is_prime(i)) {
				System.out.println(i);
			}	
		}		
	}
	
	static boolean is_prime(int n) {
		if(n==1)return false;
		if(n==2)return true;
		if(n%2==0)return false;
		int sq = (int) Math.sqrt(n)+1;
		for(int i = 2; i < sq; i++) {
			if(n%i==0)return false;
		}
		return true;
	}

}
