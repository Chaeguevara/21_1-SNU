#include <stdio.h>

#define STUDENT_NUMS 2

struct studentType
{
    char name[50];
    int ID;
    int midterm;
    int final;
    int total;
};

typedef struct studentType Student;

void calculateTotal(Student *s);

int main(void)
{

    // Declare an array of structures
    /* Your code */
    Student students[STUDENT_NUMS];
    // Receive input from the keyboard for each student
    /* Your code */
    for (int i = 0; i < STUDENT_NUMS; i++)
    {
        students[i].ID = i;
        printf("input name for student %d: ", i);
        scanf("%s", students[i].name);
        printf("input mideterm score for student %d: ", i);
        scanf("%d", &students[i].midterm);
        printf("input final score for student %d: ", i);
        scanf("%d", &students[i].final);
    }
    // Calculate total score (sum) of each student
    /* Your code */
    for (int i = 0; i < STUDENT_NUMS; i++)
    {
        calculateTotal(&students[i]);
    }

    // Print each student’s total score
    /* Your code */
    for (int i = 0; i < STUDENT_NUMS; i++)
    {
        printf("Total score for %s is %d \n",students[i].name,students[i].total);
    }
    return 0;
}

// Define calculateTotal
void calculateTotal(Student *s)
{
    /* Your code */
    (*s).total = (*s).midterm + (*s).final;
}