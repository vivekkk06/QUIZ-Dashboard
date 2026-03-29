#include <stdio.h>
int main(){
    int n[15];
    int i=0;
    while(i<16){
        scanf("%d", &n[i]);
        i++;
        if(n[i]==n[i-1] && n[i]==-1)
            break;
    }
    int m[15];
    int l=0;
    while(i<16){
        scanf("%d", &m[l]);
        l++;
        if(m[l]==m[l-1] && m[l]==-1){
            break;}
    }
    for(int j=0; j<sizeof(n); j++){
        printf("%d", n[j]);}
    for(int j=0; j<sizeof(m); j++){
        printf("%d", m[j]);}
}
