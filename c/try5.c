#include <stdio.h>
// int count=0;
// int counter() {
//     count++;
//     return count;
// }

int counter() {
    static int count = 0;
    printf("count = %d\n", count);
    count++;
    printf("count = %d\n", count);
    return count;
}
int main(){
    printf("%d\n", counter());
    printf("%d\n", counter());
    printf("%d\n", counter());
    counter();
}
