#include <stdio.h>
#include <stdlib.h>

int main() {
 
    int x, n, hr = 0, min = 0, seg = 0;
    scanf("%d", &n);
    hr = n / 3600;
    x = n % 3600;
    min = x / 60;
    x = x % 60;
    seg = x;
    printf("%d:%d:%d\n", hr, min, seg);
    return 0;
}