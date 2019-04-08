import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BJ_1001 {

	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer t = new StringTokenizer(bf.readLine());
		
		int a = Integer.parseInt(t.nextToken());
		int b = Integer.parseInt(t.nextToken());
		
		bw.write(a-b + "\n");
		bw.flush();
		
			

	}

}
