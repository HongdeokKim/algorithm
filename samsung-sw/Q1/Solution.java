package Q1;
import java.util.HashSet;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.io.FileInputStream;

class Solution {
	private static int[] dx = new int[] {-1, 0, 1,  0};
	private static int[] dy = new int[] { 0, 1, 0, -1};
	private static int g_area;
	
	public static void main(String args[]) throws Exception {

		// System.setIn(new FileInputStream("res/input.txt"));

		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++) { // 테스트 케이스 순차적으로
			int array_size = sc.nextInt();
			int[][] territory = new int[array_size][array_size];
			HashSet<Integer> height = new HashSet<>();
			g_area = 1;

			System.out.println("[테스트 " + test_case + "]");
			for(int x = 0; x < array_size; x++) { // 테스트 케이스 받기
				for(int y = 0; y < array_size; y++) {
					territory[x][y] = sc.nextInt();
					height.add(territory[x][y]); // 년도 추가
				}
			}

			for(int year : height) { // 연도 탐색
				System.out.println(year + "년차입니다");
				boolean[][] visited = new boolean[array_size][array_size];
				int area = 0;

				for(int x = 0; x < array_size; x++) {
					for(int y = 0; y < array_size; y++) {
						if(!visited[x][y] && (territory[x][y] > year)) { // 방문하지 않았거나, 잠기지 않았다면
							dfs(territory, visited, x, y, array_size, year);
							area = area + 1;
						}
					}
				}
				if(area > g_area) {
					g_area = area;
				}
			}
			System.out.println("#" + test_case + " " + g_area);
		}
	}

	public static void dfs(int[][] te, boolean[][] vi, int x, int y, int as, int ye) {
	
		vi[x][y] = true; // 해당 칸 방문
		System.out.println(x + "," + y + "방문했습니다");

		for(int move = 0; move < 4; move++) {
			int mx = x + dx[move];
			int my = y + dy[move];
			System.out.println(mx + "," + my);
			if((0 <= mx) && (mx < as) && (0 <= my) && (my < as)) { // 유효한 범위에 있는 인덱스인지
				if(!vi[mx][my] && (te[mx][my] > ye)) { // 그리고 갈 필요가 있다면
					dfs(te, vi, mx, my, as, ye);
				}
			}
		}
	}
}