#include<stdio.h>
int try(){
    printf("It's not over unitll you win.\n");
}
int congrats(){
    printf("Congrats... ");
}
int main(){
   int you = 1;
   int success = 7;
   while(you != success){
    try();
    you++;
   }
   if(you == success)
   congrats();

    return 0;
}
