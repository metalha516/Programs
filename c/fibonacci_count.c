#include<stdio.h>
int main(){ int num_1, num_3,num_2, n, x;
    n = 20;
    // x = 13;
    // int count = 2;
    num_1 = 0;
    num_2 = 1;
    printf("Fibonacci Series : %d %d ", num_1, num_2);
    while(num_3<n){
        num_3 = num_1+num_2;
        printf("%d ", num_3);
        // count++;
        // if(num_3 == x){
        //     printf("%d", count);
        // }
        num_1 = num_2;
        num_2 = num_3;
        }}