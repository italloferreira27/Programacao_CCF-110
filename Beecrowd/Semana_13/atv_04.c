#include <stdio.h>
#include <stdlib.h>
 
int main() {
    int n, voto, votfav = 0;
    int i;
    float time, dt = (2.0/3.0);

    while((scanf("%d", &n)) != EOF){
        votfav = 0;
        for(i = 0; i < n; i++){
            if((scanf("%d", &voto)) != EOF){
                if(voto == 1)
                    votfav += 1;
            }
            else
                return 0;
        }

        time =  n * dt;
        //printf("%d\n%f\n%d\n%f\n", votfav, time, n, dt);
        if(votfav >= time)
            printf("impeachment\n");
        else
            printf("acusacao arquivada\n");
    }
    return 0;
}