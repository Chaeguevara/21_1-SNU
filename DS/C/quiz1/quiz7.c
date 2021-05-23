#include <stdio.h>

int main(void)
{
    int a = 1;
    int b = 1;
    int c = 3;
    int result = 999;
    result = b + 1 | c + a;
    printf("%d\n", result);
}