#include <bits/stdc++.h>
using namespace std;

int n, x, temp;
int arr[1000001] = {0, };
int ans = 0;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);


    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> temp;
        arr[temp] = 1;
    }
    cin >> x;

    for(int i = 1; i < 1000001; i++) {
        if(arr[i] == 1) {
            temp = x - i;
            arr[i] = 0;
            // &&과 ||을 확인
            if(1 > temp || temp > 1000000) continue;
            if(arr[temp] == 1) {
                ans++;
                arr[temp] = 0;
            }
        }
    }
    cout << ans << endl;

    return 0;
}

/*
#include <bits/stdc++.h>
using namespace std;

int a[1000001]={};
// 각 자연수의 존재 여부를 저장하는 배열, 아래에서 x-a[i]가 1000000보다 큰 경우를 예외처리하기 싫어서 그냥 배열을 최대 200만으로 잡음
bool occur[2000001];
int n, x;

int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);

  int ans = 0;
  cin >> n;
  for(int i = 0; i < n; i++) cin >> a[i];
  cin >> x;

  for (int i = 0; i < n; i++) {
    // x-a[i]가 존재하는지 확인
    if(x-a[i] > 0 && occur[x-a[i]]) ans++;
    // 존재하는 값인지, 이미 참조된 값인지 확인
    occur[a[i]] = true;
  }
  cout << ans;
}
*/