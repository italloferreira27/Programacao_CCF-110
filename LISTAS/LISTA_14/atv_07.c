#include <stdio.h>
#include <stdlib.h>

int FIB(int n);

int main(){
    int n, i;
    scanf("%d", &n);
    if(n < 20){
        for(i = 1; i <= n; i++){
            printf("%d ", FIB(i));
        }
    }
    return 0;
}
int FIB(int n){
    int res;
    if(n > 2){
       return res = FIB(n-1) + FIB(n-2);     
    }
    return 1;
}