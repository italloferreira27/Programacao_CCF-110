/*O custo ao consumidor de um carro novo é a soma do custo de fábrica com o percentual do distribuidor e dos impostos
 (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escreva
  um algoritmo que leia o custo de fábrica de um carro e escreva o custo do consumidor.*/

#include <stdio.h>
#include <stdlib.h>

int main(){

    float custo_fab, custo_cons;

    printf("Digite o custo de fabrica do carro: ");
    scanf("%f", &custo_fab);

    custo_cons = ((custo_fab*0.28) + (custo_fab*0.45) + custo_fab);

    printf("O custo do carro para o consumidor e %.2f", custo_cons);
    
    return 0;
}