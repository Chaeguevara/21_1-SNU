#include <stdio.h>

// Perform calculation

int main(void)
{
    int opearnd1, operand2; // two input values
    int result = 0;       // output value
    char operation;           // operation to perform

    // Get the input values and operator
    printf("Enter first operand: ");
    scanf("%d", &opearnd1);
    printf("Enter operation to perform(+, -, *, /): ");
    scanf("%c", &operation);
    printf("The operation is %c\n",operation);
    printf("Enter second operand: ");
    scanf("%d", &operand2);
    printf("The operand1 is %d\n",opearnd1);

    switch (operation)
    {
    case '+':
        result = opearnd1 + operand2;
        break;
    case '-':
        result = opearnd1 - operand2;
        break;
    case '/':
        result = opearnd1 / operand2;
        break;
    case '*':
        result = opearnd1 * operand2;
        break;
    default:
        printf("Invalid Operation\n");
        break;
    } // end switch

    // Print the output value
    printf("The answer is %d\n", result);

} // end main