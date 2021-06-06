#include <stdio.h>
#include <stdlib.h>

void printStars(int n);

int main(int argc, char *argv[])
{
    int N = atoi(argv[1]);
    // YOUR CODE HERE
    printStars(N);
    return 0;
}

void printStars(int n)
{
    int newN, newK;
    for (int k = 1; k <= n; k++)
    {
        newN = n;
        for (newN - k; newN - k > 0; newN--)
        {
            printf("%c", ' ');
        }
        newK = 2*k-1;
        for(newK; newK >0; newK--){
            printf("%c",'*');
        }
        printf("\n");
    }
}