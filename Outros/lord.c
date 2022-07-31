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
}
//2322
#include <stdio.h>
#include <stdlib.h>
 
int main() {
    int i, j, n, troca, valor = 0;
    scanf("%d", &n);
    int num[n];
    for(i = 1; i < n; i++){
        scanf("%d", &num[i]);
        }
    for(i = 1; i < n; i++){
        for(j = i+1; j < n; j++){
            if(num[i] > num[j]){
                troca = num[i];
                num[i] = num[j];
                num[j] = troca;
            }
        }
    }
    for(i = 1; i <= n; i++){
        if(num[i] != i){
            valor = i;
            break;
        }
    }
    printf("%d\n", valor);
    return 0;
}

//Ajude Guku
#include <stdio.h>
#include <stdlib.h>
 
int main() {
    int i, n, soma = 0;
    for(i = 0; i < 10; i++){
        scanf("%d", &n);
        soma += n;
    }
    if(soma >= 8001)
        printf("Goku derrotou Freeza!");
    else
        printf("Freeza derrotou Goku!");
    return 0;
}

//1181
#include <stdio.h>
#include <stdlib.h>
 
int main() {
    int i, j, l;
    double matriz[12][12], soma = 0.0;
    char op[2];
    scanf("%d", &l);
    scanf("%s", &op);
    for(i = 0; i < 12; i++){
        for(j = 0; j < 12; j++){
            scanf("%lf", &matriz[i][j]);
        }
    }
    if(op[0] == 'S'){
        for(i = 0; i < 12; i++){
            soma += matriz[l][i];
        }
        printf("%.1lf\n", soma);
    }
    else
        if(op[0] == 'M'){
            for(i = 0; i < 12; i++){
                soma += matriz[l][i];
            }
            soma = soma / 12.0;
            printf("%.1lf\n", soma);
    }
    return 0;
}

//1183
#include <stdio.h>
#include <stdlib.h>
 
int main() {
    int i, j;
    double matriz[12][12], soma = 0.0, conta = 0.0;
    char op[2];
    scanf("%s", &op);
    for(i = 0; i < 12; i++){
        for(j = 0; j < 12; j++){
            scanf("%lf", &matriz[i][j]);
        }
    }
    if(op[0] == 'S'){
        for(i = 0; i < 12; i++){
            for(j = i+1; j < 12; j++){
                soma += matriz[i][j];
            }
        }
        printf("%.1lf\n", soma);
    }
    else
        if(op[0] == 'M'){
            for(i = 0; i < 12; i++){
            for(j = i+1; j < 12; j++){
                soma += matriz[i][j];
                conta += 1;
            }
        }
        soma = soma / conta;
        printf("%.1lf\n", soma);
    }
    return 0;
}*/