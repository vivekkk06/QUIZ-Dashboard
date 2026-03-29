#include <stdio.h>
int fib(int n){
    if(n==1) return (1);
    if(n==2) return (1);
    else
        return (fib(n-2)+fib(n-1));
}
int main(){
    for(int i=1;i<30;i++){
        printf("%d\n", fib(i+1));
        printf("%d\n", fib(i));
        float r=(float)fib(i+1)/fib(i);
        printf("the ratio : %f\n\n", r);
    }
}