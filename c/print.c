#include<stdio.h>
int main(){
   int n;
   printf("enter number");
   scanf("%d",&n);
   int m=n;
   int end=n*n;
   for(int i=1;i<=end;i++){
      if(i<n){
         printf(" ");
      }
      else{
         printf("*");
      }
      if(i%m==0){
         n=n+(m-1);
         printf("\n");
      }
   }
}