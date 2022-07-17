#include <stdio.h>
#include <stdlib.h>

void verificador(int vet[11]);

int main(){
    char cpf[11];
    int CPF[11];// = {0,1,2,3,4,5,6,7,8};

    printf("Digite seu CPF: ");
    scanf("%s", &cpf);
    for(int i = 0; i < 11; i++){
        int C = (int) cpf[i];
        CPF[i] = C - 48;
    }
    
    verificador(CPF);

    return 0;
}

void verificador(int vet[11]){
    int ver1, ver2, resto, soma = 0, res[10], peso[] = {10,9,8,7,6,5,4,3,2}, peso1[] = {11,10,9,8,7,6,5,4,3,2};
    for(int i = 0; i < 9; i++){
        res[i] = vet[i] * peso[i];
        soma += res[i]; 
    }
    resto = soma % 11;
    if(resto < 2)
        ver1 = 0;
    else
        ver1 = 11 - resto;
    soma = 0;
    for(int i = 0; i < 9; i++){
        res[i] = vet[i] * peso1[i];
        soma += res[i]; 
    }
    res[9] = ver1 * 2;
    soma += res[9]; 
    resto = soma % 11;
    if(resto < 2)
        ver2 = 0;
    else
        ver2 = 11 - resto;    
    if(vet[9] == ver1 && vet[10] == ver2)
        printf("O CPF e VALIDO!");
    else
        printf("O CPF e INVALIDO!\nCodigos verificadores: %d e %d", ver1, ver2);
}