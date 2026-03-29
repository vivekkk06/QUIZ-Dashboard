#include <stdio.h>
int main(){
    
    int i = 0;
    int n[15];
    int x,y;
    while(y != -1){
        scanf("%d %d", &x, &y);
        i=i+2;
        if(x==y && x==-1){
            break;
        }
        else{
            n[i-1]=x;
            n[i]=y;
        }
    }
    for(i = 0; i <= sizeof(n); i++){
        printf("%d ", n[i]);
    }

    
}
