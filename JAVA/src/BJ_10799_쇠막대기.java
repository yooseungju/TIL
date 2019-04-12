import java.util.*;
public class BJ_10799_쇠막대기 {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String[] arr = sc.nextLine().split("");
		Stack<String> stack= new Stack<>();
		int cnt = 0;
		
		for(int i=0 ;i<arr.length;i++) {
			
			if(arr[i].equals("(")) stack.push(arr[i]);
<<<<<<< HEAD
			else
				
				if(stack.peek().equals("(")) {
					stack.pop();
					if(!stack.empty()) {
						cnt+= stack.size();
					}
				}else stack.pop();
		}System.out.println(cnt);	
=======
			else {
				stack.pop();
				if(arr[i-1].equals("(")) cnt+= stack.size();
				else cnt++;
			}
	
		}System.out.println(cnt);		
>>>>>>> dc9d23cb41c8b8eb6907fc4498ea03379cdd0205
	}	
}