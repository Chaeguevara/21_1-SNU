/* Description
 * Write a program that reads any english alphabet from the keyboard 
 * and prints every character from that character down 
 * to the character A in the order in which they appear in the ASCII table
 */

#include <stdio.h>

void main(int argc, char* argv[]){
	
	/* Please write your code below */
	char inputC;
	char destC = 'A';
	scanf("%c",&inputC);
	for (inputC; destC-1 != inputC; inputC--)
	{
		printf("%c",inputC);
	}

	/* Do not modify below */
}

