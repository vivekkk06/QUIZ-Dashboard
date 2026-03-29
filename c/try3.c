#include <stdio.h>
void try(int* a) {
    (*a)++; /* Will change value a */
}
int main(){
    int a = 10;
    try(&a);
    printf("a = %d\n", a);
}