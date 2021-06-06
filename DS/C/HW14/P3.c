#include <stdio.h>

char *addDash(char line[]);

int main(int argc, char *argv[])
{
    char *input_filename = argv[1];  // name of input file
    char *output_filename = argv[2]; // name of output file
    // YOUR CODE HERE
    char oneLine[11];
    char newLine[14];
    FILE *inFile;
    FILE *outFile;
    inFile = fopen(input_filename, "r");
    outFile = fopen(output_filename, "w");
    while (fscanf(inFile, "%[^\n]\n", oneLine) != EOF)
    {
        newLine[0] = oneLine[0];
        newLine[1] = oneLine[1];
        newLine[2] = oneLine[2];
        newLine[3] = '-';
        newLine[4] = oneLine[3];
        newLine[5] = oneLine[4];
        newLine[6] = oneLine[5];
        newLine[7] = oneLine[6];
        newLine[8] = '-';
        newLine[9] = oneLine[7];
        newLine[10] = oneLine[8];
        newLine[11] = oneLine[9];
        newLine[12] = oneLine[10];
        newLine[13] = oneLine[11];
        fprintf(outFile,"%s\n",newLine);
    }
    fclose(outFile);
    fclose(inFile);

    return 0;
}