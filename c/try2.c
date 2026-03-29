// #include <stdio.h>
// void try(int a) {
//     a++;/* will not change value a */
// }
// int main() {
//     int a = 10;
//     try(a);
//     printf("a = %d\n", a);
// }
#include <stdio.h>
int try(int a) {
    a++;/* will not change value a */
    return a;
}
int main() {
    int a = 10;
    printf("a=%d\n", try(a));
    printf("a = %d\n", a);
    printf("%d\n", try(4));
}
