// MY INITIAL METHOD
#include <stdio.h>
int main(){
    int n;
    scanf("%d", &n);
    int s=0;
    if(n<127 && n>-128){
        if(n<127 && n>=0){
            for(int i=0; i<8; i++){
                s=s*10+(n%2);
                n=n/2;
                printf("%d\n", s);
            }
        
        printf("%d\n",s);
        int k;
        int m=0;
        printf("0");
        for(int j=0; j<8;j++){
            k=s%10;
            m=m*10 + k;
            s=s/10;
            printf("%d", k);
        }printf("\n0");
        printf("%d\n", m);
        }
        else{
            n=-(n);
            for(int i=0; i<8; i++){
                s=s*10+(n%2);
                n=n/2;
                printf("%d\n", s);
            }
        
        printf("%d\n",s);
        int k;
        int m=0;
        printf("1");
        for(int j=0; j<8;j++){
            k=s%10;
            m=m*10 + k;
            s=s/10;
            printf("%d", k);
        }
        printf("\n");
        printf("%d", m);
        
        while(m%10==0){
            
        }
    }
    }

    else{
        printf("Number out of range!\n");
    }
}