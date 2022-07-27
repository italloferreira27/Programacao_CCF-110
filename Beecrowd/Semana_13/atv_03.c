#include <stdio.h>
#include <stdlib.h>

int main(){
    int i, n, q, troca;

    while(scanf("%d", &n) != EOF && scanf("%d", &q) != EOF){
        int nota[n], pos[q];
        for(i = 0; i < n; i++){
            scanf("%d", &nota[i]);
        }
        for(i = 0; i < n; i++){
            for(int j = i+1; j < n; j++){
                if(nota[i] < nota[j]){
                    troca = nota[i];
                    nota[i] = nota[j];
                    nota[j] = troca;
                }
            }
        }
        for(i = 0; i < q; i++){
            scanf("%d", &pos[i]);
        }
        for(i = 0; i < q; i++){
            printf("%d\n", nota[(pos[i]-1)]);
        }
    }
    return 0;
}