#include <stdio.h>
#include <stdlib.h>

/*
  Print the number of connected components in the linked list
*/
struct Node {
    int data;
    struct Node* next;
};
 
/* Create a new node */
struct Node * createNode(struct Node * newNode, int data){
  newNode = (struct Node *) malloc(sizeof(struct Node));
  newNode->data = data;
  return newNode;
}

int isNumInInput(int curr, int *inputArr, int length){
  for (int i=0; i < length; i++){
    if (curr == inputArr[i]){
      return 1;
    }
  }
  return -1;
}
int main(int argc, char* argv[])
{  
  int length = argc - 2;
  int * inputArr = (int *) malloc(sizeof(int) * length);
  
  char * filepath = argv[1]; 

  for (int i = 0; i < length; ++i){
    inputArr[i] = atoi(argv[i+2]);
  }

  /* Create a linked list from file input */
  int k = 1;
  struct Node* head = NULL;
  struct Node* prev = NULL;
  struct Node* curr = NULL;

  FILE *fp = fopen(filepath, "r");
  char buffer[10]; 
  
  while (fscanf(fp, "%s", buffer) == 1){
    curr = createNode(curr, atoi(buffer));  
    if (k > 1)
    {
      prev->next = curr;
    }
    else
      head = curr;

    k++;
    prev = curr;
  }
  fclose(fp);

  int numConnected = 0;

  /* Write your code here */
  curr = head;
  while (curr){
    if(isNumInInput(curr->data,inputArr,length)==1){
      numConnected ++;
      while((curr->next!=NULL)&&(isNumInInput(curr->next->data,inputArr,length)==1)){
        curr = curr->next;
      }
    }
    curr = curr->next;
  }




	/* Do not modify below */	
  printf("%d", numConnected);

  return 0;


}


