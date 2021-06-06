#include <stdio.h>
#include <stdlib.h>
#define MAX_LEN 10

char *SwitchCase(char *s);
int main(int argc, char *argv[])
{
  char *str; //List of characters to be sorted

  str = argv[1];
  printf("%s", SwitchCase(str));
}
/* Do not modify above */
/* Write your code below */
char *SwitchCase(char *s)
{
  char *result;
  result = s;

  for (int i = 0; i < MAX_LEN; i++)
  {
    if (*(s + i) == '\0')
    {
      break;
    }
    //Upper to lower
    if (*(s + i) < 91)
    {
      *(s + i) += 32;
    }
    else // lower to upper
    {
      *(s + i) -= 32;
    }
  }
  return result;
}