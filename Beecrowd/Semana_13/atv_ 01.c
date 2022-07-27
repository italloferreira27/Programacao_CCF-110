#include <stdlib.h>
#include <stdlib.h>

int main(){
    int i, cont;
    char num[100];

    scanf("%s", &num);
    for(i = 0; i < 100; i++){
        if(num[i] == '1')
            cont += 1;
    }
    if(cont % 2 == 0){
        printf("%s0\n", num);
    }
    else
        printf("%s1\n", num);
    return 0;
}