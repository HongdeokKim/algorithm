# 파이썬의 경우와 달리...
# 직접 아랫자리부터 carry를 확인하여 진행

A, B = map(int, input().split())

print(A + B)

'''
#include <stdio.h>
#include <string.h>

int member(int a, int b);

int main()
{
    char num1[10002], num2[10002];
    int rst[10002];
    int len1, len2, len;
    int i, next;
    int x, y;

    scanf("%s %s", num1, num2);

    len1 = strlen(num1);
    len2 = strlen(num2);

    len = len1;
    if(len < len2) len = len2; 

    next = 0;

    for(i=1; i<=len; i++)
    {
        if(len1-i < 0) x = 0;
        else x = num1[len1-i]-'0';

        if(len2-i < 0) y = 0;
        else y = num2[len2-i]-'0';

        rst[i] = (x+y+next)%10; 
        next = (x+y+next)/10;
    }

    if(next > 0) rst[++len] = next;    
    for(i=len; i>0; i--) printf("%d", rst[i]);

    return 0;
}
'''