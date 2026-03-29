#include <stdio.h>
void init(int *arr, int len) {
    for ( int i = 0; i < len; i++ ) {
    *arr = i; arr++;
    }
}
int main(){
    int array[100];
    init(array, 100);
    for ( int i = 0; i < 100; i++ ) {
    printf("%d\n", array[i]);
    }
}