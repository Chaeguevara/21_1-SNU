#include <stdio.h>

// Perform calculation

int main(void)
{
    float opearnd1, operand2; // two input values
    float result = 0.0;       // output value
    char operation;           // operation to perform

    // Get the input values and operator
    printf("Enter first operand: ");
    scanf("%f", &opearnd1);
    printf("Enter operation to perform(+, -, *, /): ");
    scanf("\n %c", &operation);
    printf("Enter second operand: ");
    scanf("%f", &operand2);

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

    } // end switch

    // Print the output value
    printf("The answer is %f\n", result);

} // end main