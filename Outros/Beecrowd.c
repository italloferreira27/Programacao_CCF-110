/*
//1029
#include <stdio.h>
#include <stdlib.h>

int Fibonacci(int x, int* ptr){
    int resultado;
    *ptr += 1;
    if(x == 0)
         return 0;
    if(x == 1)
        return 1;
    return Fibonacci(x-1, ptr) + Fibonacci(x-2, ptr);
}

int main(){
    int N, num, valor = 0, call = -1, i;
    int* ptr = &call;
    scanf("%d", &N);
    for(i = 0; i < N; i++){
        scanf("%d", &num);
        valor = Fibonacci(num, ptr);
        printf("fib(%d) = %d calls = %d\n", num, *ptr, valor);
        call = -1;
    }
    return 0;
}

//1028
#include <stdio.h>
#include <stdlib.h>

int Max_Fig(int x, int y){
    int a = x - y;
    if(a == y)
        return a;
    if(a > y)
        Max_Fig(a, y);
    else
        Max_Fig(y, a);
}

int main(){
    int N, n1, n2, i;
    scanf("%d", &N);
    if(N != 0){
        for (i = 0; i < N; i++){
            scanf("%d %d", &n1, &n2);
            if(n1 >= n2)
                printf("%d\n",Max_Fig(n1, n2));
            else
                printf("%d\n",Max_Fig(n2, n1));
        }
    }
    return 0;
}
*/