import java.util.*;
public class BJ_10799_�踷��� {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String[] arr = sc.nextLine().split("");
		Stack<String> stack= new Stack<>();
		int cnt = 0;
		
		for(int i=0 ;i<arr.length;i++) {
			
			if(arr[i].equals("(")) stack.push(arr[i]);
			else
				
				if(stack.peek().equals("(")) {
					stack.pop();
					if(!stack.empty()) {
						cnt+= stack.size();
					}
				}else stack.pop();
		}System.out.println(cnt);	
	}	
}
