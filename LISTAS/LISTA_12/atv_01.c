/*Certo dia o professor de Johann Friederich Carl Gauss (aos 10 anos de idade) mandou que os alunos somassem
os números de 1 a 100. Imediatamente Gauss achou a resposta – 5050 – aparentemente sem cálculos. Supõe-se que já aí,
Gauss, houvesse descoberto a fórmula de uma soma de uma progressão aritmética.*/

#include <stdio.h>
#include <stdlib.h>

int main(){

    int num1, num2, pa, n;

    printf("Digite o termo inicial e o termo final: ");
    scanf("%d" "%d", &num1, &num2);
    printf("Digite a quantidade de termos: ");
    scanf("%d", &n);

    pa = ((num1 + num2)*n)/2;

    printf("O valor da P.A. = %d", pa);

return 0;
}