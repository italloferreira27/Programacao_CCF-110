#include <stdio.h>
#include <stdlib.h>
 
int main() {
    int linha, coluna, valor = 0;
    scanf("%d %d", &linha, &coluna);
    int matriz[linha][coluna];

    for(int i = 0; i < linha; i++){
        for(int j = 0; j < coluna; j++){
            scanf("%d", &matriz[i][j]);
        } 
    }
    for(int i = 0; i < linha; i++){
        for(int j = 0; j < coluna; j++){
            if(matriz[i][j] != 0){ //Número a esquerda
                for(int k = i+1; k < linha; k++){
                    for(int r = j; r > -1; r--){
                        if(matriz[k][r] != 0)
                            valor += 1;
                    }      
                }
                j = coluna;
            if(matriz[i][j] == 0 && j == (coluna-1))
                for(int ii = i+1; ii < linha; ii++){
                    for(int jj = 0; jj < coluna; jj++){
                        if(matriz[ii][jj] != 0) //colunas sem o zero
                            valor += 1;
                    }
                }
            }    
        }
    }
    if(valor == 0)
        printf("S\n");
    else
        printf("N\n");
    return 0;
}
/*
//https://www.youtube.com/watch?v=k2VBdNGBvZo
#include <stdio.h>
#include <stdlib.h>
 
char MatrizEscada(int linha, int coluna);

int main() {
    int linha, coluna;
    scanf("%d %d", &linha, &coluna);
    printf("%c\n", MatrizEscada(linha, coluna));

}
char MatrizEscada(int linha, int coluna){
    int matriz[linha][coluna];
    int l, c, l2, c2;
    for(l = 0; l < linha; l++){
        for(c = 0; c < coluna; c++){
            scanf("%d", &matriz[l][c]);
        } 
    }
    for(l = 0; l < linha; l++){
        for(c = 0; c <= coluna; c++){
            if(c == coluna){ // Linhas somente com zeros
                    for(int l2 = l+1; l2 < linha; l2++){
                        for(int c2 = 0; c2 > coluna; c2++){
                            if(matriz[l2][c2] != 0)
                                return 'N';
                        }      
                    }
                    return 'S';
                }
            else{
                if(matriz[l][c] != 0){ //Buscando o elemento a esquerda
                    for(int l2 = l+1; l2 < linha; l2++){
                        for(int c2 = 0; c2 <= c; c2++){
                            if(matriz[l2][c2] != 0)
                                return 'N';
                            }
                        }
                    c = coluna + 1;                            
                    }
                }
            }
        }
    return 'S';
}*/