#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll pow(ll a, ll b, ll c) {
    int temp; // 자료형 생각해야했음!
    if(b == 1) return a % c; // terminal
    else if(b % 2) return (pow(a, b - 1, c) * a) % c; // 홀수라면
    else { // 짝수라면
        temp = pow(a, b / 2, c);
        return (temp * temp) % c;
    }
}

int main(void) {
    int A, B, C;
    cin >> A >> B >> C;
    cout << pow(A, B, C) << endl;

    return 0;
}

// 재귀, 분할정복
// (A * A * A) % C == (A % C)(A % C)(A % C)
// temp 자료형에서 오버플로우가 날 수도 있음
// https://chan9.tistory.com/78