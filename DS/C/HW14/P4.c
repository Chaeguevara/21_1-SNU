#include <stdio.h>

int isPrime(int n);

int main(int argc, char *argv[])
{
    char *input_filename = argv[1];  // name of input file
    char *output_filename = argv[2]; // name of output file
    // YOUR CODE HERE
    FILE *inFile = fopen(input_filename, "r");
    FILE *outFile = fopen(output_filename, "w");
    int inNum;
    int order,newInNum,i;
    while ((fscanf(inFile, "%d", &inNum)) != EOF)
    {
        fprintf(outFile, "%d =", inNum);
        if (isPrime(inNum) != -1)
        {
            fprintf(outFile, " %d\n", inNum);
        }
        else
        {
            order = 0;
            newInNum = inNum;
            i = 2;
            while((newInNum > 1) && (i<inNum))
            {
                while (newInNum % i == 0)
                {
                    if (order == 0)
                    {
                        fprintf(outFile, " %d", i);
                        order++;
                    }
                    else
                    {
                        fprintf(outFile, " * %d", i);
                    }
                    newInNum /= i;
                    
                }
                i++;
            }
            fprintf(outFile, "\n");
        }
    }
    fclose(outFile);
    fclose(inFile);
    return 0;
}

int isPrime(int n)
{
    for (int i = 2; i < n; i++)
    {
        if (n % i == 0)
        {
            return -1;
        }
    }

    return 0;
}