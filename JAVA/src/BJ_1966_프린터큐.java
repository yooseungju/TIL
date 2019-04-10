import java.util.*;
import java.util.LinkedList;
public class BJ_1966_프린터큐 {
	
	static Scanner sc = new Scanner(System.in);
	static LinkedList<Integer> list = new LinkedList();
	static LinkedList<Integer> index = new LinkedList();

	static int N;
	static int M;
	
	public static void main(String[] args) {

		int T = sc.nextInt();
		
		//Testcase �떆�옉
		for(int i =0; i<T;i++) {
			
			N = sc.nextInt();
			M =sc.nextInt();
			sc.nextLine();
			
			int cnt = 0;

			
			String[] arr = sc.nextLine().split(" ");
						
			for(int j=0;j<N;j++) {
				list.add(Integer.parseInt(arr[j]));
			}
			
			while(!list.isEmpty()) {
				int tmp = list.getFirst();
				
				if(go_back(tmp)) {
					int index_tmp = index.getFirst();
					index.removeFirst();
					index.add(index_tmp);
					list.removeFirst();
					list.add(tmp);
					}
				else {
					cnt ++;
					if(index.getFirst() == M)System.out.println(cnt);
					list.removeFirst();
					index.removeFirst();
				}				           				            
			}						
		}
	}
	
	static boolean go_back(int tmp){
		for(int j=0;j<list.size();j++) {
			if(list.get(j) > tmp)return true;  
		}	
		return false;
	}
}