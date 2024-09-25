#include<stdio.h>
int main(){
  int arr[] = {20,60,80,5,7,9};
  int size = sizeof(arr)/4;
  int  max_value = arr[0];
  int  min_value = arr[0];
  for(int i = 1; i<size; i++){
    if(arr[i]>max_value){
        max_value = arr[i];
    }if(arr[i]<min_value){
        min_value = arr[i];
    }
  }
  printf("Maximum value is : %d\nMinimum value is: %d",max_value,min_value);
   return 0;
}