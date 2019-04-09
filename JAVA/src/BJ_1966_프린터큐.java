import java.util.Scanner;
import java.util.PriorityQueue;
import java.util.Comparator;
public class BJ_1966_프린터큐 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int i =0; i<T;i++) {
			
			PriorityQueue<Printer> pq = new PriorityQueue<Printer>(100000, new Comparator<Printer>(){
				@Override
				public int compare(Printer o1, Printer o2) {
					// TODO Auto-generated method stub
					if(o1.weight > o2.weight) return -1;
					
					return 0;
				}
				
				
			});
			int N = sc.nextInt();
			int M =sc.nextInt();		
			
		}
	}


}

class Printer{
	int index;
	int weight;
	
	Printer(int index, int weight){
		this.index = index;
		this.weight = weight;
	}
	
}

