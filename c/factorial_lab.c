#include<stdio.h>
int main(){
    int n = 50;
    unsigned long long int fact = 1;
    for(int i = 1; i<=n; i++){
       fact = fact * i;
    }
    printf("%llu", fact);
   
}