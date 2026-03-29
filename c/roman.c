#include <stdio.h>
int main(){
    int n;
    scanf("%d", &n);
    int a=n/100;
    int c=n%10;
    int b=(n%100-c)/10;

    int a1[14]={1,2,3,4,5,6,7,8,9,10,50,100,500,1000};
    char a21[14][6]={"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "L", "C", "D", "M"};
    char a22[9][6]={"X","XX","XXX","XL","L","LX","LXX","LXXX","XC"};
    char a23[9][6]={"C","CC","CCC","CD","D","DC","DCC","DCCC","CM"};
    char *l[3]={"","",""};
    for(int i=0; i<14; i++){
        if(a1[i]==n){
            printf("%s", a21[i]);
            return 0;
        }
    }
    for(int i=0; i<14; i++){
        if(a1[i]==c){
            l[2]=a21[i];
            break;
        }
    }
    for(int i=0; i<14; i++){
        if(a1[i]==b){
            l[1]=a22[i];
            break;
        }
    }
    for(int i=0; i<14; i++){
        if(a1[i]==a){
            l[0]=a23[i];
            break;
        }
    }
    for(int i=0; i<3; i++){
        printf("%s", l[i]);
    }
}
