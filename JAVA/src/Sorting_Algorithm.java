
public class Sorting_Algorithm {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[] arr = {9,6,7,3,5};
		int[] new_arr = bubble_sort(arr);
		
		for(int i =0; i<new_arr.length;i++) {
			
			System.out.print(new_arr[i]);
			
		}

	}
	
	// 선택정렬
	public static int[] selection_sort(int[] arr) {
		for(int i=0; i<arr.length-1;i++) {
			int least = i;
			for(int j=i+1;j<arr.length; j++){
				if(arr[j] < arr[least]) least = j;		
			}
			
			if(i!=least) {
				int tmp = arr[i];
				arr[i] = arr[least];
				arr[least] = tmp;		
			}			
		}	
		return arr;
	}
	
	// 삽입정렬
	public static int[] insert_sort(int[] arr) {
		for(int i=1; i<arr.length;i++){
			int key = arr[i];
			int c = 0;
			for(int j=i-1; j>=0 && arr[j]>key;j--) {
				arr[j+1] = arr[j];
				c = j;
			}
			arr[c] = key;
		}
		return arr;
	}
	
	//버블정렬
	public static int[] bubble_sort(int[] arr) {
		for(int i = arr.length-1; i>0;i--) {
			for(int j = 0; j<i ; j++) {
				if(arr[j]>arr[j+1]) {
					int tmp = arr[j+1];
					arr[j+1] = arr[j];
					arr[j] = tmp;
				}
			}
		}
		
		return arr;
	}
	//셀정렬 
	public static int[] shell_sort(int[] arr) {
		
		
		return arr;
	}
	
	//퀵정렬
	public static int[] quick_sort(int[] arr, int left, int right) {
		
		if(left<right) {
			int pivot = (left+right)/2;
				
		}
		
		
		
		return arr;
	}
}
