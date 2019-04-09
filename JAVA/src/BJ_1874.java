import java.util.Stack;
import java.util.Scanner;
import java.util.Arrays;
import java.util.LinkedList;

public class BJ_1874 {
	static String[] arr;
	static Stack<String> stack;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int tc= sc.nextInt();
		
		for(int i= 0; i < tc;i++) {
			arr = sc.next().split("");
			stack = new Stack<String>();	
			if(check())System.out.println("YES");
			else System.out.println("NO");
		}
		
	}
	
	static boolean check() {
		for(int j=0 ; j < arr.length ; j++) {
			if(arr[j].equals("(")) stack.push("(");
			else if(stack.empty()) {return false;}
			else stack.pop();
			
		}		
		if (!stack.empty())return false;
		else return true;
	}

	
	
}
