import java.util.*;
public class BJ_10799_쇠막대기 {
	
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String[] arr = sc.nextLine().split("");
		Stack<String> stack= new Stack<>();
		int cnt = 0;
		
		for(int i=0 ;i<arr.length;i++) {
			if(arr[i] == "(") stack.push(arr[i]);
			else
				if(stack.peek() == "(") {
				stack.pop();
				if(!stack.empty()) {
					cnt+= stack.size();
				}
			}	
		}
	
	}
	
}
