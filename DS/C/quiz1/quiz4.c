#include <stdio.h>
#define LETTER '1'
#define ZERO 0
#define NUMBER 123

int main(void)
{
    printf("%c", 'a');
    printf("x%x", 12288);
    printf("$%d.%c%d n", NUMBER, LETTER, ZERO);
}
