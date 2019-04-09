import java.util.Queue;
import java.util.Scanner;
import java.util.Arrays;
import java.util.LinkedList;

public class BJ_1260 {
	static int[][] graph;
	static boolean visited[];
	static int N;
	static int E;
	static int startPoint;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		graph = new int[1001][1001];
		E = sc.nextInt();
		visited = new boolean[1001];
		startPoint = sc.nextInt();
		
		int a,b;
		
		for(int i=1; i<=E; i++) {
			a = sc.nextInt();
			b = sc.nextInt();
			
			graph[a][b] = graph[b][a] = 1;
		}
		
		dfs(startPoint);
		System.out.println();
		Arrays.fill(visited, false);
		bfs(startPoint);	
	}
	
	static void bfs(int i){
		Queue<Integer> q = new LinkedList<Integer>();
		q.offer(i);
		visited[i] = true;
		
		int temp;
		
		while(!q.isEmpty()) {
			temp = q.poll();
			System.out.print(temp + " ");
			for(int j = 1 ; j < N+1; j++){
				if(graph[temp][j] == 1 && visited[j] == false) {
					visited[j] = true;
					q.offer(j);							
				}
			}			
		}	
	}
	static void dfs(int i){
		visited[i] = true;
		System.out.print(i+" ");
		
		for(int j = 0 ; j < N+1; j++ ) {
			if(graph[i][j] == 1 && visited[j] == false)dfs(j);		
		}	
		
	}

}
