import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.Queue;

public class 우선순위큐 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Comparator<int[]> comparator = (i1, i2) -> {
			if (i1[1] > i2[1]) {
				return 1;
			}
		};
		LinkedList<int[]> queue = new LinkedList<>();
		Collections.sort(queue, comparator);
	}

}
