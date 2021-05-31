#include <stdio.h>
#include <stdlib.h>

int P1(int n);

// Implement P1
// You can define other function, but P1 must return answer.
int P1(int n)
{
    int result = 0;
    if (n == 1)
    {
        return 1;
    }
    else
    {
        // move (n-1) disks to 'spare'
        result += P1(n - 1);
        //move one from 'from' to 'to'
        result += P1(1);
        //move (n-1) disks from 'spare' to 'to'
        result += P1(n - 1);
    }

    return result;
}

// DO NOT MODIFY BELOW!
int main(int argc, char *argv[])
{
    int n = atoi(argv[1]);
    int ans = P1(n);

    printf("%d\n", ans);

    return 0;
}