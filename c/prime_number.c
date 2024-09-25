#include <stdio.h>
int main(){
    int x, y;
    printf("Enter the number : ");
    scanf("%d", &x);
    for (int i = 2; i < x; i++){
        if(x%i==0){
           y = 0;
           break;
        }
        else{
            y = 1;
        }
    }
    if(y == 0){
        printf("Not prime");
    }
    if(y == 1){
        printf("Prime");
    }
    return 0;
}