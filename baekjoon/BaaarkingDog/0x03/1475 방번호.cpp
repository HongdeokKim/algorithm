#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    int temp;
    int arr[10] = {0, };
    int max = 0;

    cin >> N;
    while(N > 0) {
        temp = N % 10;
        if(temp == 6 || temp == 9)
            arr[6]++;
        else 
            arr[temp]++;
        N /= 10;
    }

    arr[6] = (arr[6]%2)==1 ? arr[6]/2+1 : arr[6]/2;

    for(int i = 0; i < 10; i++) {
        if(arr[i] > max)
            max = arr[i];
    }
    cout << max << endl;
    return 0;
}