#include<stdio.h>
int main(){
    // int n;
    // scanf("%d", &n);
    int m = 1;
    int n = 10;
    int i = 0; 
    int flag = 0;
    for(i = m; i<=n; i++){
        for(int j = 2; j<i-1; j++){
            if(i%j == 0){
                flag = 1;
                break;
            }
            
        }
         if(flag == 0){
        printf("%d", i);
    }
    }
   
    
}