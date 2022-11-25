#include <iostream>

using namespace std;

int cache[21][21][21] = {0, };

int rec(int a, int b, int c) {
    if(a <= 0 || b <= 0 || c <= 0) return 1;
    if(a > 20 || b > 20 || c > 20) return rec(20, 20, 20);

    if(cache[a][b][c] != 0) return cache[a][b][c];

    if(a < b && b < c) 
        cache[a][b][c] = rec(a, b, c-1) + rec(a, b-1, c-1) - rec(a, b-1, c);
    else
        cache[a][b][c] = rec(a-1, b, c) + rec(a-1, b-1, c) + rec(a-1, b, c-1) - rec(a-1, b-1, c-1);

    return cache[a][b][c];
}

int main(void) {
    int a, b, c;

    while(1) {
        cin >> a >> b >> c;

        if(a == -1 && b == -1 && c == -1) break;

        cout << "w(" << a << ", " << b << ", " << c << ") = " << rec(a, b, c) << endl;
    }

    return 0;

}