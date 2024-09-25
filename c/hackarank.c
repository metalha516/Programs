#include<stdio.h>
#include<string.h>
int main(){
    char str[100];
    int digit[10] = {0};
    scanf("%s", str);
    for(int i = 0; i<strlen(str); i++){
       if(str[i] >= 48 && str[i]<=57){
            digit[str[i]-48]++;
       }
    }

    for(int j = 0; j<10; j++){
        printf("%d ", digit[j]);
    }
    
}
