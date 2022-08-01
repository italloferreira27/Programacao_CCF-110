/*//Número 1 - "a"
#include <stdio.h>
#include <stdlib.h>

int Elimina_par(int *, int x);

int main(){
    int valor, num, i;
    printf("Digite o tamanho do vetor: ");
    scanf("%d", &num);
    int vetor[num], *vetptr = vetor;
    printf("Preencha o vetor: ");
    for(i = 0; i < num; i++){
        scanf("%d", &vetor[i]);
    }
    //Chamando a 1ª função para contar os impares e alocar os números ímpares nas primeiras posições 
    valor = Elimina_par(vetptr, num);
    printf("Existe %d numeros impares.", valor);
    //Escrevendo os números ímpares
    printf("\nNumeros impares: ");
    for(i = 0; i < valor; i++){
        printf("%d ", vetor[i]);
    }
    return 0;
}
int Elimina_par(int *vetptr, int x){
    int i, cont = 0, *vetor = vetptr; //Na hora da prova eu criei esse ponteiro "vetor" para o ponteiro "vetptr"
    //mas pode-se trabalhar com o próprio ponteiro, porém estou replicando o que fiz na prova.
    for(i = 0; i < x; i++){
        if(vetor[i] % 2 != 0){
            vetor[cont] = vetor[i];
            cont += 1;
        }
    }
    return cont;
}*/
//Número 1 "B"
#include <stdio.h>
#include <stdlib.h>

int Elimina_par(int *, int x);
int Ordena(int *, int x);

int main(){
    int valor, i, vetor[10], *vetptr = vetor;
    //Entrada dos valores
    printf("Preencha o vetor: ");
    for(i = 0; i < 10; i++){
        scanf("%d", &vetor[i]);
    }
    //Chamando a 1ª função para contar os ímpares e alocar os números ímpares nas primeiras posições  
    valor = Elimina_par(vetptr, 10);
    printf("Existe %d numeros impares.", valor);
    //Chamando a 2ª função para organizar de forma crescente os números ímpares
    Ordena(vetptr, valor);
    //Escrevendo o números ímpar ordenado
    printf("\nNumeros impares ordenado: ");
    for(i = 0; i < valor; i++){
        printf("%d ", vetor[i]);
    }
    return 0;
}
int Elimina_par(int *vetptr, int x){
    int i, cont = 0, *vetor = vetptr;
    for(i = 0; i < x; i++){
        if(vetor[i] % 2 != 0){
            vetor[cont] = vetor[i];
            cont += 1;
        }
    }
    return cont;
}
int Ordena(int *vetptr, int x){
    int i, j, troca;
    for(i = 0; i < x; i++){
        for(j = i; j < x; j++){
            if(vetptr[i] > vetptr[j]){
                troca = vetptr[i];
                vetptr[i] = vetptr[j];
                vetptr[j] = troca;
            }
        }
    }
}