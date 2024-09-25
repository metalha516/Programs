#include<stdio.h>
//a 2 z
int main(){
    for(int i =0; i<27; i++){
        for(int a = 0; a<i; a++){
            printf("%c ", 97+a);
        }
        printf("\n");
    }

}
// int main(){
//  for(int i = 0; i<=5; i++){
//     for(int j = 1; j<i; j++){
//         printf(" ");
//     }
//     for(int k = ((9-(i*2)-2)); k>1; k--){
//         printf("*");
//     }
//     printf("\n");
//  }
// }

// #include<stdio.h>
// int main(){
//   for(int i = 0; i<5; i++){
//     for(int k = 0; k<i; k++){
//       printf(" ");
//     }
//     for(int j = 0; j<5-i; j++){
//       printf("*");
//     }
    
//     printf("\n");
//   }
// }

// int main(){
//   for(int i = 6; i>0; i--){
//     for(int k = 6-i; k>0; k--){
//       printf(" ");
//     }
//     for(int j = (2*i)-1; j>0; j--){
//       printf("*");
//     }
//     printf("\n");
//   }
// }