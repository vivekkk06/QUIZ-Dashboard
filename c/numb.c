#include <stdio.h>
int main(){
    int n;
    scanf("%d", &n);
    char a[21][20]={"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty"};
    char b[][20]={"Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety", "Hundred"};
    if(n<=20){
        if(n==0){printf("Zero");}
        else
        printf("%s", a[n]);
    }
    else if(n<100){
        printf("%s", b[n/10 - 2]);
        printf(" %s", a[n%10]);
    }
    else{
        printf("%s", a[n/100]);
        printf(" Hundred");
        int n2=n%100;
        if(n2<=20){
            if(n2==0){}
            else
            printf(" %s", a[n2]);
        }
        else{
            printf(" %s", b[n2/10 - 2]);
            printf(" %s", a[n2%10]);
        }
    }
}