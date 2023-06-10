#include <bits/stdc++.h>
using namespace std;

int N, K;
int arr[2][7] = {0, };
int t1, t2, temp;
int ans = 0;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> K;
    for(int i = 0; i < N; i++) {
        cin >> t1 >> t2;
        arr[t1][t2]++;
    }

    for(int i = 0; i < 2; i++) {
        for(int j = 1; j < 7; j++) {
            int temp = arr[i][j] / K;
            ans += temp;
            if((arr[i][j] % K) > 0) ans++;
        }
    }
    cout << ans;

    return 0;
}