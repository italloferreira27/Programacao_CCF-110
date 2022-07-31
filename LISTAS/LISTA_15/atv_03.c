#include <stdio.h>
#include <stdlib.h>

void tabuada(int m, int n);

int main(){
    int num, mult = 1;
    scanf("%d", &num);
    tabuada(mult, num);
    return 0;
}
void tabuada(int m, int n){
    int valor, c = n;
    if(m <= c){
        valor = m * c;
        printf("%d * %d = %d\n", m, c, valor);
        m++;
        tabuada(m, n);
    }
    // else
    //     valor = c * c;
    //         printf("%d * %d = %d\n\n", c, c, valor);
}