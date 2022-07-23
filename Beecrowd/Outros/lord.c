/*
//2896
#include <stdio.h>
#include <stdlib.h>
 
int main() {
    int n, compradas, prom, div;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        scanf("%d %d", &compradas, &prom);
        if(compradas >= prom){
            div = compradas / prom;
            div += compradas % prom;
            printf("%d\n", div);
        }
        else
            printf("%d\n", compradas);
    }
    return 0;
}
//2786
#include <stdio.h>
#include <stdlib.h>
 
int main() {
    int largura, comprimento, piso1, piso2;
    scanf("%d %d", &largura, &comprimento);
    if(largura > 0 && comprimento > 0){
        piso1 = ((largura * comprimento) + ((largura - 1) * (comprimento - 1)));
        piso2 = (((comprimento - 1)*2) + ((largura - 1)*2));
    }
    printf("%d\n%d", piso1, piso2);
    return 0;
}*/
//2540
#include <stdio.h>
#include <stdlib.h>
 
int main() {
    
    
    return 0;
}