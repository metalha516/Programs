#include <stdio.h>
int main(){
    int row,col;
    printf("Enter row and column number : ");
    scanf("%d%d", &row, &col);
    for(int i = 0; i<row; i++){
        for(int j = 0; j<col; j++){
            printf("%c ", "S");
        }
        printf("\n");
    }
    return 0;
}