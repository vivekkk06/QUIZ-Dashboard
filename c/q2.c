#include <stdio.h>
int main(){
    int a1[15][2]={0};
    int a2[15][2]={0};
    int a3[15][2]={0};
    int i=0;
    int j=0;
    while(1){
        scanf("%d", &a1[i][0]);
        scanf("%d", &a1[i][1]);
        if(a1[i][0]==a1[i][1] && a1[i][0]==-1){
            break;
        }
        i++;
    }
    while(1){
        scanf("%d", &a2[j][0]);
        scanf("%d", &a2[j][1]);
        if(a2[j][0]==a2[j][1] && a2[j][0]==-1){
            break;
        }
        j++;
    }
    int n=0;
    for(int k=0;k<=j; k++){
        int f=0;
        for(int l=0;l<=i; l++){
            if(a2[k][1]==a1[l][1]){
                a3[n][0] = a2[k][0] + a1[l][0];
                a3[n][1] = a2[k][1];
                if(a3[n][0]!=0){
                n++;
                f=1;
                }
                else{
                    f=1;
                }
        }
        }
        if(f==0){
            a3[n][0] = a2[k][0];
            a3[n][1] = a2[k][1];
            n++;
        }
        }
    
    for(int o=0; o<=i; o++){
        int f=0;
        for(int l=0;l<=j; l++){
            if(a2[l][1]==a1[o][1]){
                f=1;
            }
        }
        if(f==0){
            a3[n][0] = a1[o][0];
            a3[n][1] = a1[o][1];
            n++;
        }
    }
    printf("a3 : \n");
    for(int j=0; j<n; j++){
        printf("%d %d \n", a3[j][0], a3[j][1]);
    }
    
    int a4[15][2]={0};
    for(int q=0; q<=n; q++){
        int max=-1;
        for(int p=0; p<=n; p++){
            if(a3[p][1]>max){
                max=a3[p][1];
            }
        }
        a4[q][1]=max;
        for(int p=0; p<=n; p++){
            if(a3[p][1]==max){
                a3[p][1]=-1;
                a4[q][0]=a3[p][0];
                a3[p][0]=-1;
            }
        }
    }
    int a5[15][2]={0};
    for(int y=0; y<=n; y++){
        if(a4[y][1]!=-1){
            a5[y][1]=a4[y][1];
            a5[y][0]=a4[y][0];
        }
    }

    printf("a5 : \n");
    for(int j=0; j<=n; j++){
        if(a5[j][0]!=0){
            printf("%d %d ", a5[j][0], a5[j][1]);
        }
    }
    printf("\n %d %d %d", a5[n-2][0], a5[n-2][1], n);
    for(int j=0; j<15; j++){
            printf("\n%d %d ", a5[j][0], a5[j][1]);
    }
    // tanuj +1
}