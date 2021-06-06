#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]){

  if (argc < 4){
    printf("Please input at least 4 integers\n");
  }

  int i = atoi(argv[1]);
  int j = atoi(argv[2]);
  int k = atoi(argv[3]);
  int l = atoi(argv[4]);

  char *alphabet[] = {"ABC", "DEF", "GHI", "JKL"};  

  char a, b, c, d;
    
  /* Write your code here */	
  a = alphabet[0][i];
  b = alphabet[1][j];
  c = alphabet[2][k];
  d = alphabet[3][l];


  /*do not modify below*/

  printf("%c%c%c%c\n", a,b,c,d);
  return 0;
}
