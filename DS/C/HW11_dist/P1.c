/* Description
 * Write a program that reads a positive integer from the keyboard 
 * and displays a 1 if it is divisible by 3 or a 0 otherwise
 */

#include <stdio.h>

void main(int argc, char *argv[])
{
	int input_int;
	int ans = -1;
	/* Please write your code below */
	int remainder = 0;
	printf("Enter any natural number n\n");
	scanf("%d", &input_int);
	remainder = input_int % 3;
	if (remainder == 0)
	{
		ans = 1;
	}
	else
	{
		ans = 0;
	}

	/* Do not modify below */

	printf("ans:%d\n", ans);
}
