#include <stdio.h>
#include <stdbool.h>
int main(void)
{
    int upperLimit = 100;
    for (int i = 1; i <= upperLimit; i++)
    {
        int divCount = 0;
        //printf("%d",i);
        for (int j = 1; j < i; j++)
        {
            if (i % j == 0)
            {
                divCount++;
            }
            if (divCount >= 2)
            {
                break;
            }
        }
        if (divCount == 1)
        {
            printf("%d\n", i);
        }
    }
}