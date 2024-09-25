#include <stdio.h>
int max_of_four(int a, int b, int c, int d){
    int max = 0;
    if(b>a){
        max = b;
    }if(c>max){
        max = c;
    }if(d>max){
        max = d;
    }if(a>max){
        max = a;
    }
    return max;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}