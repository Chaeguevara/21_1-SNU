#include <stdio.h>

int main(void)
{
        int t =  2;
        {
                printf("%d-1\n", t);
                {
                        printf("%d-2\n", t);
                        t = 3;
                }
                printf("%d-3\n", t);
        }
        {
                printf("%d-4\n", t);
        }
}