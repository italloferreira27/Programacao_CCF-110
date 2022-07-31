#include <stdio.h>
#include <stdlib.h>

void multiplos_5(int a, int b);

int main(){
    int n1, n2;
    scanf("%d%d", &n1, &n2);
    multiplos_5(n1, n2);
    return 0;
}
void multiplos_5(int a, int b){
    int i, mult = a;
    for(i = 0; i < 6; i++){
        if((mult-i) % 5 == 0){
            mult = mult - i;
            break;  
        }
    }
    for(i = 0; i < 6; i++){
        if((b+i) % 5 == 0){
            b = b + i;
            break;  
        }
    }
    if(mult < (b-5)){
        mult = mult + 5;
        printf("%d\t", mult);
        multiplos_5(mult, b);
    }
}