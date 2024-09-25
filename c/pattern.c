// #include<stdio.h>
// int main(){
//   int n;
//   printf("Enter :");
//   scanf("%d", &n);
//   int len = 2*n; 
//   len -= 1;
//   int arr[len][len];
//   for(int i = 0; i<len; i++){
//     for(int j = 0; j<len; j++){
//      int min = i;
//      if(j<i){
//       min = j;
//      }
//      if(len-i-1<min){
//       min = len-i-1;
//      }
//      if(len-j-1<min){
//       min = len-j-1;
//      }
//      arr[i][j] = n-min;
//     }
//   }
//   for(int i = 0; i<len; i++){
//     for(int j = 0; j<len; j++){
//         printf("%d", arr[i][j]);
//     }
//     printf("\n");
//   }
// }

#include<stdio.h>
int main(){
  for(int i = 0; i<5; i++){
    for(int k = 0; k<i; k++){
      printf(" ");
    }
    for(int j = 0; j<5-i; j++){
      printf("*");
    }
    
    printf("\n");
  }
}