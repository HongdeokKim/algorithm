import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Solution {

    public static int[][] video;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        video = new int[N][N];

        for(int i = 0; i < N; i++) {
			String line = br.readLine();
			
			for(int j = 0; j < N; j++) {
                video[i][j] = Character.getNumericValue(line.charAt(j));
            }
		}

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                System.out.print(video[i][j] + " ");
            }
            System.out.println();
        }
    }
}