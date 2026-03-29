#include <stdio.h>

int main() {
    int i=0;
    int n[16];
    // int m[16];
    int x,y;
    printf("%lu", sizeof(n));
    while(1){
        scanf("%d %d", &x, &y);
        i=i+1;
        n[i-1]=x;
        n[i]=y;
        if(x==y && x==-1)
            break;
    }
    // while(1){
    //     scanf("%d %d", &x, &y);
    //     i=i+2;
    //     m[i-1]=x;
    //     m[i]=y;
    //     if(x==y && x==-1)
    //         break;
    // }
    for(int j=0; j<sizeof(n); j++){
        printf("%d", n[j]);
    }
    // for(int j=0; j<sizeof(m); j++){
    //     printf("%d", m[j]);
    // }
}