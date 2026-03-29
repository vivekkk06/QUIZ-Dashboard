#include <stdio.h>
int T(int n){
    if(n==1) return (1);
    else
        return (n+T(n-1));
}
int main(){
    printf("%d\n", T(5));
    printf("%d\n", T(10));
}