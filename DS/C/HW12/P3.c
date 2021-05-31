#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int P3(int n);
bool isNumPrime(int n);

// Implement P3
// You can define other function, but P3 must return answer.
int P3(int n)
{
    int count = 0;
    int stopper = 2 * n;
    for (n++; n < stopper; n++)
    {
        if (isNumPrime(n) == true)
        {
            count += 1;
        }

    }

    return count;
}

bool isNumPrime(int n)
{
    bool result = true;
    for (int i = 2; i < n; i++)
    {
        if (n % i == 0)
        {
            return false;
        }
    }
    return result;
}

// DO NOT MODIFY BELOW!
int main(int argc, char *argv[])
{
    int n = atoi(argv[1]);
    int ans = P3(n);

    printf("%d\n", ans);

    return 0;
}