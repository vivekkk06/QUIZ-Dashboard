#include <stdio.h>
int main(){
    int n;
    scanf("%d", &n);
    int array[8];
    if(n<=127 && n>=-128){
        if(n>=0){
            for(int i=0;i<8;i++){
                array[i]=n%2;
                n=n/2;
            }
        
            for(int i=7;i>=0;i--){
                printf("%d", array[i]);
            }
        }
        else{
            n=-(n);
            int temp=0;
            for(int i=0;i<8;i++){
                if(n%2==0 && temp==0){
                    array[i]=0;
                    n=n/2;
                }
                else{
                    if(n%2==1 && temp==0){
                        array[i]=1;
                        temp=1;
                        n=n/2;
                    }
                    else{
                    array[i]=!(n%2);
                    n=n/2;
                    }
                }
            }
        
            for(int i=7;i>=0;i--){
                printf("%d", array[i]);
            }
        }
    }
    else
        printf("Number out of range!\n");
}
