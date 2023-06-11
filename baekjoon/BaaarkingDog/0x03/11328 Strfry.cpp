#include <bits/stdc++.h>
using namespace std;

int N;
int arr[26] = {0, };
string s1, s2; // string 사용법 숙지
bool sig = true;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    for(int i = 0; i < N; i++) {
        memset(arr, 0, sizeof(arr)); // memset 사용법 숙지
        sig = true;

        cin >> s1 >> s2;
        // for auto 사용법 숙지
        for(auto c : s1) arr[c-'a']++;
        for(auto c : s2) arr[c-'a']--;

        for(int i = 0; i < 26; i++) {
            if(arr[i] != 0) { // 조건 까다롭게 생각하자
                sig = false;
                break;
            }
        }
        if(sig) cout << "Possible\n";
        else cout << "Impossible\n";
    }

    return 0;
}