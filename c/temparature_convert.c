#include<stdio.h>
float Celsius_2_Farhenheit(float x){
    float celsius = x;
    float farhenheit = (1.8*celsius)+32;
    return farhenheit;
}
float farhenheit_2_Celsius(float x){
    float farhenheit = x;
    float celsius = 0.5555*(farhenheit - 32);
    return celsius;
}
float celsius_2_kelvin(float x){
    float celsius = x;
    return celsius+273.16;
}
float farhenheit_2_kelvin(float x){
    float farhenheit = x;
    float celsius = farhenheit_2_Celsius(farhenheit);
    return celsius_2_kelvin(celsius);
}
int main(){
   float num;
   printf("Enter the value : ");
   scanf("%f", &num);
   printf("%f", Celsius_2_Farhenheit(num));
   return 0;
}