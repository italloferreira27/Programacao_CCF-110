#include <stdio.h>
#include <stdlib.h>

void segundos(int h, int m, int s);

int main(){
    int hr, min, seg;
    printf("Digite as HORAS os MINUTOS e os SEGUNDOS: ");
    scanf("%d %d %d", &hr, &min, &seg);
    segundos(hr, min,seg);

    return 0;
}
void segundos(int h, int m, int s){
    int seg;
    seg = s + (m * 60) + (h * 3600);
    printf("Sao %d segundos!", seg);
}