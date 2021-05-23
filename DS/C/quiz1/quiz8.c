#include <stdio.h>

int main(void)
{
    int t = 2;
    int i1 = 1;
    int i2 = 1;
    int i3 = 1;
    int i4 = 1;
    int i5 = 1;
    int j1 = 1;
    int j2 = 1;
    int j3 = 1;
    int j4 = 1;
    int j5 = 1;
    i1 += 1;
    j1 = i1;
    printf("%d\n", j1);
    j2 = ++i2;
    printf("%d\n", j2);
    j3 = i3 + 1;
    printf("%d\n", j3);
    j4 = i4++;
    printf("%d\n", j4);
    j5 = i5 += 1;
    printf("%d\n", j5);
}