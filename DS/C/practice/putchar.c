#include <stdio.h>
#include <unistd.h>
 
int main(void) {
    putchar('s');
 
    sleep(5);
 
    putchar('s');
    putchar('\n');
    return 0;
}