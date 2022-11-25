#include <bits/stdc++.h>

using namespace std;

using long ll;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int A, B, C;
    long long res = 1;

    cin >> A >> B >> C;
    
    for(int i = 0; i < B; i++) {
        res = res * A;
    }

    cout << res % C << endl;

    return 0;
}

// 재귀, 분할정복