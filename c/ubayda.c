#include<stdio.h>
int main(){
    float num1,num2;
    char operator;
    float total;
    printf("Please enter a operator (+,-,*,/) : ");
    scanf("%c", &operator);
    printf("Enter the num_1");
    scanf("%f", &num1);
    printf("Enter the num_2");
    scanf("%f", &num2);
    switch(operator){
        case '+':
                total = num1 + num2;
                printf("total number is : %f", total);
        default:
        printf("Error");
    }
    return 0;
}