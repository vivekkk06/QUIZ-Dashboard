#include<iostream>
#include<conio.h>
int main()
{
    int i,j=1,k=1;
    printf("enter a number ");
    scanf("%d",&i);
    for(j=1,j<=i,j++)
    {
        k=k*j;
    }
    printf("factorial of %d = %d", i, k);
    getch();
}