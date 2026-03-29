#include <stdio.h>
int main(){
    float a,b,c;
    scanf("%f %f %f", &a, &b, &c);
    if( a+b <= c || a+c <= b || b+c <= a){
        printf("invalid");
    }
    else
    {
        if(a*a + b*b <= c*c + 0.000001 && a*a + b*b >= c*c - 0.000001
        || b*b + c*c <= a*a + 0.000001 && b*b + c*c >= a*a - 0.000001
        || c*c + a*a <= b*b + 0.000001 && c*c + a*a >= b*b - 0.000001){
            printf("right-angled");
        }
        
        else if(a==b && b==c){
            printf("equilateral");
        }
        else if(a==b || b==c || a==c){
            printf("isosceles");
        }
        else{
            printf("notspecial");
        }
    }
}
