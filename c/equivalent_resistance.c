#include<stdio.h>

int series(){
    int num_re; 
    float sum;
    sum = 0;
    printf("Enter the number of Resistance\n");
    scanf("%d", &num_re);
    float resis[num_re];
    for(int i = 1; i<num_re+1; i++){
        printf("Enter the resistance number %d\n", i);
        scanf("%f", &resis[i]);
        sum = sum + resis[i];
    }
    printf("The equivalent resistance is : %0.2f", sum);
}
float parallel(){
     int num_re; 
     float sum, mul;
     sum = 0;
     mul = 1;
     printf("Enter the number of Resistance\n");
     scanf("%d", &num_re);
     float resis[num_re];
    for(int i = 1; i<num_re+1; i++){
        printf("Enter the resistance number %d\n", i);
        scanf("%f", &resis[i]);
        mul = mul*resis[i];
        sum = sum + resis[i];
    }
    printf("\nThe Equivalent resistance is : %0.2f\n", mul/sum);
}


int main(){
    printf("series/parallel\n");
    char input;
    scanf("%c", &input);
    if(input=='s'){
        series();
    }if(input=='p'){
        parallel();
    }
    return 0;
}