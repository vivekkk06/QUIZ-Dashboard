#include <stdio.h>
int main(){
    int r,c;
    scanf("%d %d", &r, &c);
    int m[r][c];
    for(int i=0; i<r; i++){
        for(int j=0; j<c; j++){
            scanf("%d", &m[i][j]);
        }
    }
    int i=0;
    int j=0;
    for(;j<c;){
        j++;
        printf("%d\n", m[i][j]);
    }
    for(;i<r;){
        i++;
        printf("%d\n", m[i][j]);
    }
    for(;j>=0;){
        j--;
        printf("%d\n", m[i][j]);
    }
    for(;i>=1;){
        i--;
        printf("%d\n", m[i][j]);
    }
}