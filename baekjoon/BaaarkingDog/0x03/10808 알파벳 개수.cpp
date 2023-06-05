#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    char arr[101]; // 단어의 길이가 최대 100, 널을 생각해서 100 + 1 자리를 만들어야함
    int ans[26] = {0, };

    cin >> arr;

    for(int i = 0; i < 26; i++) {
        for(char* ptr = arr; *ptr != '\0'; ptr++) {
            if((int)(*ptr)-'a' == i) (ans[i])++;
        }
        cout << ans[i] << " ";
    }

    return 0;
}

/*
int freq[26];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  string s;
  cin >> s;
  for(auto c : s)
    freq[c-'a']++; // 아스키 연산으로 직접적인 인덱스 접근 -> for을 사용하지 않게됨
  for(int i = 0; i < 26; i++)
    cout << freq[i] << ' ';
}
*/