import java.util.StringTokenizer;
import java.util.Scanner;
public class BJ_1152 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String str  = sc.nextLine();
		
		StringTokenizer words = new StringTokenizer(str);
		System.out.println(words.countTokens());
	
	}

}
