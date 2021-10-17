//숨바꼭질

import java.util.ArrayList;
import java.util.Scanner;

public class N1697 {

	static int N, K;		// 수빈이의 위치, 동생의 위치 
	static int[] visited = new int[200002];
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		K = sc.nextInt();

		ArrayList<Integer> al = new ArrayList<Integer>();
		
		al.add(N);
		visited[N] = 1;
		
		int count = 0;
		int now;
		int next;
		
		if(N == K){
			System.out.print(count);
			sc.close();
			return;
		}
		
		boolean bl = true;
		while(bl && !al.isEmpty()){
			
			for(int i=al.size()-1 ; i>=0 ; i--){
				
				now = al.get(i);
				
				int[] d = {1, -1, now};
				
				for(int j=0 ; j<3 ; j++){
					next = now + d[j];
					
					if(next == K){
						bl = false;
						continue;
					}
					if(0 <= next && next <= 100000 && visited[next] == 0){
						visited[next] = 1;
						al.add(next);
					}
					
				}
				
				al.remove(i);
				
			} // for
			
			count++;
			
		} // while
		
		System.out.print(count);
		sc.close();
	}
}

