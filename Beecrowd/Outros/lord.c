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
    printf("%d\n%d\n", piso1, piso2);
    return 0;
}
//2540
#include <stdio.h>
#include <stdlib.h>
 
int main() {
    int n, voto, votfav = 0;
    int i;
    float time, dt = (2.0/3.0);

    while((scanf("%d", &n)) != EOF){
        votfav = 0;
        for(i = 0; i < n; i++){
            if((scanf("%d", &voto)) != EOF){
                if(voto == 1)
                    votfav += 1;
            }
            else
                return 0;
        }

        time =  n * dt;
        //printf("%d\n%f\n%d\n%f\n", votfav, time, n, dt);
        if(votfav >= time)
            printf("impeachment\n");
        else
            printf("acusacao arquivada\n");
    }
    return 0;
}*/