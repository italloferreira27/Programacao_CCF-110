#include <stdio.h>
#include <stdlib.h>

float distancia(int x1, int x2, int y1, int y2, int z1, int z2);

int main(){
    int x1, x2, y1, y2, z1, z2;
    printf("Digite a coordenada (x,y,z) do primeiro ponto: ");
    scanf("%d %d %d", &x1, &y1, &z1);
    printf("Digite a coordenada (x,y,z) do segundo ponto: ");
    scanf("%d %d %d", &x2, &y2, &z2);
    printf("A distancia dos 2 pontos no espaco e de %f", distancia(x1, x2, y1, y2, z1, z2));
    return 0;
}
float distancia(int x1, int x2, int y1, int y2, int z1, int z2){
    float distancia;
    distancia = sqrt((pow((x2 - x1), 2) + pow((y2 - y1), 2) + pow((z2 - z1), 2)));
    return distancia;
}