#include <stdio.h>
 
int main() {
 
    int n, num, in = 0, out = 0;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        scanf("%d", &num);
        if(num <= 20 && num >= 10)
            in += 1;
        else
            out += 1;
    }
    printf("%d in\n%d out\n", in, out);
    return 0;
}