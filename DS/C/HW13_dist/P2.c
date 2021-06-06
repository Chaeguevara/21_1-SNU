#include <stdio.h>
#include <stdlib.h>

/* Modify printElement function to print 
   i-th element of input character array 
	 */
void printElement(char **ptr, int i)
{
	char *ptr1;
	/* Write your code here */	
	ptr1 = ptr[i];



	/* Do no modify below */	
	printf("%s\n", ptr1);
}

int main(int argc, char* argv[])
{
	char *arr[] = { "ant", "bat", "cat", "dog", "egg", "fly", "man", "god", "ptr", "str" };
	if (argc < 2){
		printf("Please input any integer as argument\n");
		return -1;
	}
	
	int i = atoi(argv[1]);
	if (i > 9 || i < 0){
		printf("Please input integer between 0 and 9(inclusive)");
		return -1;
	}

	printElement(arr, i);
	return 0;
}
