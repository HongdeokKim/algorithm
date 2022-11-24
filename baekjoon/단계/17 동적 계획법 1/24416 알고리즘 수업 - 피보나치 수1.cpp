#include <iostream>

using namespace std;

int f[41];
int ex_1 = 0;
int ex_2 = 0;

int fib_1(int n) {
    if(n == 1 || n == 2) {
        ex_1++;
        return 1;
    }
    else {
        return fib_1(n - 1) + fib_1(n - 2);
    }
}

int fib_2(int n) {
    f[1] = f[2] = 1;

    for(int i = 3; i <= n; i++) {
        ex_2++;
        f[i] = f[i - 1] + f[i - 2];
    }

    return f[n];
}


int main(void) {
    int n;

    cin >> n;
    fib_1(n);
    fib_2(n);
    cout << ex_1 << " " << ex_2 << "\n";

    return 0;
}