#include <stdio.h>

int main(int argc, char *argv[])
{
    char *input_filename = argv[1]; // name of input file
    // YOUR CODE HERE
    FILE *inFile;
    inFile = fopen(input_filename, "r");
    int oneInt;
    //    char oneChar[10];
    int result = 0;
    while (fscanf(inFile, "%d", &oneInt) != EOF)
    {
        result += oneInt;
        //    printf("%d",oneInt);
    }
    printf("%d\n", result);
    fclose(inFile);

    return 0;
}
