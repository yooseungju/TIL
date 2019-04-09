import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class BJ_15552 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int num = Integer.parseInt(bf.readLine());
		
		for(int i=0; i<num;i++){
			StringTokenizer st = new StringTokenizer(bf.readLine());

			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());	
			bw.write(a+b+"\n");
			
		}
		
		bw.flush();
		bw.close();

	}

}
