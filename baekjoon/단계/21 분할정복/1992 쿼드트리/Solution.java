import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution {
    
    public static int[][] img;
    public static void main(String[] args) {
        System.out.println("Hello World!");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        for(int i = 0; i < N; i++) {
			String str = br.readLine();
			
			for(int j = 0; j < N; j++) {
				img[i][j] = str.charAt(j) - '0';
			}
		}
    }
}