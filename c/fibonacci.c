#include<stdio.h>
int main(){
    int x,y,z,n;
    // printf("Enter the number of fibonacci you want");
    // scanf("%d", &n);
    x = 0;
    y = 1;
    printf("Fbonacci : %d\t%d", x,y);
    for(int i = 2; i < 10; i++){
       
        z = x+y;
        
        printf("\t%d", z);
        x = y;
        y = z;
        
    }
    // while(z<=n){
    //     printf("\t%d", z);
    //     x = y;
    //     y = z;
    //     z = x+y;
    // }

    return 0;
}