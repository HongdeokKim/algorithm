#include <stdio.h>

int main(void) {
    int N, x, y;
    scanf("%d", &N);
    
    x = N / 5;
    
    for(;x >= 0; x--){
        for(y = 0; ((5 * x) + (3 * y)) <= N; y++){
            if(((5 * x) + (3 * y)) == N){
                printf("%d", x + y);
                return 0;
            }
        }
    }
    printf("-1");
    
    return 0;
}