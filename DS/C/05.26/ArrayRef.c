#include <stdio.h>
#define MAX_NUMS 5
int Average(int inputValues[]);
 
int main(void) {
    int mean;
    int nums[MAX_NUMS];
 
    printf("Enter %d nums,\n", MAX_NUMS);
    for (int i =0; i < MAX_NUMS; i++) {
        printf("Input num %d: ", i);
        scanf("%d", &nums[i]);
    } 
    mean = Average(nums);
    printf("The average of these nums is %d\n", mean);

    return 0;
}

int Average(int inputValues[]) {
    int sum = 0;
 
    for (int i=0; i < MAX_NUMS; i++) {
        sum += inputValues[i];
    }
  
    return (sum / MAX_NUMS);
} 