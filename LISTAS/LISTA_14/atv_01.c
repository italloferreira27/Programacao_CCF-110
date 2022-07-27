#include <stdio.h>
#include <stdlib.h>

void ast(int n, int *ptrc);

int main(){
    int n, c;
    int* ptrc = &c;
    scanf("%d", &n);
    c = n;
    //printf("%d", *ptrc);
    ast(n, ptrc);
    return 0;
}
void ast(int n, int *ptrc){
    int i;
    // printf("%d%d", *ptrc, n);

    if(n > 1){
        for(i = 0; i < *ptrc; i++){
            printf("* ");
        }
        printf("\n");
        ast(n-1, ptrc);
    }
    else
        for(i = 0; i < *ptrc; i++){
            printf("* ");
        }
}