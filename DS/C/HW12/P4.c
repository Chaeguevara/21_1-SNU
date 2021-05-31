#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int P4(int n);
int digitSum(int n);
bool isSelfNum(int n);

// Implement P4
// You can define other function, but P4 must return answer.
int P4(int n)
{
    if (isSelfNum(n)){
        n++;
    }
    while(!isSelfNum(n)){
        n++;
    }
    return n;
}

int digitSum(int n)
{
    int result = 0;
    while (n != 0)
    {
        result += n % 10;
        n /= 10;
    }
    return result;
}

bool isSelfNum(int n){
    bool result = true;
    for(int i =1; i <= n; i ++){
        if(n == (i + digitSum(i))){
            return false;
        }
    }
    return result;
}
// DO NOT MODIFY BELOW!
int main(int argc, char *argv[])
{
    int n = atoi(argv[1]);
    int ans = P4(n);

    printf("%d\n", ans);

    return 0;
}