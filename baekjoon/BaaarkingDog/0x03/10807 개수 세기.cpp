#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, v, temp;
    int arr[201] = {0, };

    cin >> N;
    for(int i = 0; i < N; i++) {
        cin >> temp;
        arr[temp + 100]++;
    }
    cin >> v;
    
    cout << arr[v + 100] << endl;
    
    return 0;
}