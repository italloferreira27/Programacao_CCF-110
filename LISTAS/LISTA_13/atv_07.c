/*#include <stdio.h>
#include <stdlib.h>

int aprovado(int matriz[10][5]);

int main(){
    int aluno[10][5], a;
    int i, j;

    printf("Digite a nota dos 10 alunos:\n");
    for(i = 0; 1 < 10; i++){
        for(j = 0; j < 5; j++){
            aluno[i][j] = ("%d", rand() % 100); //Gera numero aleatorio de 1 a 100
        }
    }
    printf("%d", aluno[10][5]);
    //a = aprovado(aluno[10][5]);
    //printf("%f", a);
    
    return 0;
}

int aprovado(int matriz[10][5]){
    float media[10], cont = 0;
    int i, j;
    for(i = 0; 1 < 10; i++){
        for(j = 0; j < 5; j++){
            cont = cont + matriz[i][j];
        }
        media[i] = cont/5;
        cont = 0;
        if(media[i] >= 60)
            printf("Aluno %d foi APROVADO!", i);
        else
            printf("Aluno %d foi REPROVADO!", i);
    }
}*/
#include <stdio.h>
#include <stdlib.h>

void Aprovado(float matriz[10], int n); //void Aprovado(float * matriz, int n);

int main() {
    float notas[10][5];
    int i, j;
    for(i = 0; i < 10; i++){
        printf("Digite as notas do Aluno %d:\n", i+1);
        for(j = 0; j < 5; j++){
            scanf("%f", &notas[i][j]);
        }
        Aprovado(notas[i], i);
    }
    return 0;
}

void Aprovado(float matriz[10], int n){ //void Aprovado(float * matriz, int n){
    int media = 0, i;
    for(i = 0; i < 5; i++){
        media = media + matriz[i];
    }

    if(media / 5 >= 60)
        printf("Aluno %d APROVADO!\n", n+1);
    else
       printf("Aluno %d REPROVADO!\n", n+1);
}
