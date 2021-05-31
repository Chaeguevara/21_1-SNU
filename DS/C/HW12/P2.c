#include <stdio.h>
#include <stdlib.h>

int P2(int n);

// Implement P2
// You can define other function, but P2 must return answer.
int P2(int n)
{
    int result = 1;
    int remainder = -1;
    int n_rem = -1;
    for (n; n > 0; n--)
    {
        remainder = result % n;
        if (remainder == 0)
        {
            result = result;
        }
        else if (remainder == 1)
        {
            result *= n;
        }
        else
        {
            n_rem = n % remainder;
            if (n_rem == 0)
            {
                result = result * (n / remainder);
            }
            else
            {
                result *= n;
            }
        }
    }

    return result;
}

// DO NOT MODIFY BELOW!
int main(int argc, char *argv[])
{
    int n = atoi(argv[1]);
    int ans = P2(n);

    printf("%d\n", ans);

    return 0;
}