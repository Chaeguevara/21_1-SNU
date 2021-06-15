
#include <stdio.h>

typedef struct nodeType LinkedNode;
typedef struct listType SLList;

struct nodeType {
    int val;
    LinkedNode *next;
};

struct listType {
    LinkedNode *first;
    int size;
};


void addFirst(SLList *LL, int x);
int getFirst(SLList *LL);
int getSize(SLList *LL);
void printSLList(SLList *LL);
LinkedNode *searchNode(SLList *LL, int x);
void deleteNode(SLList *LL, int x);



LinkedNode *createNode(int x) {
    LinkedNode *newNode;
    newNode = (LinkedNode *) malloc(sizeof(LinkedNode)); 
    newNode->val = x;
    newNode->next = NULL;
    return newNode;
}




int main(void) {
    SLList myLL = {NULL, 0};     
    addFirst(&myLL, 10);
    addFirst(&myLL, 15);
    addFirst(&myLL, 20);
    addFirst(&myLL, 17);
    printf("%d\n", getFirst(&myLL));
    getSize(&myLL);
    printSLList(&myLL);   
}

void addFirst(SLList *LL, int x) {
    LinkedNode *newFirst;
    newFirst = createNode(x);
    newFirst->next = LL->first;
    LL->first = newFirst;
    LL->size++;
}

int getFirst(SLList *LL) {
    if (LL->first != NULL)
          return LL->first->val;
    return 0;
}

int getSize(SLList *LL) {
    return LL->size;
}

void printSLList(SLList *LL) {
    LinkedNode *curr = LL->first;
    printf("size: %d, firstVal: %d, allVals: ", getSize(LL), getFirst(LL));
    while (curr != NULL) {
        printf("%d->", curr->val);
        curr = curr->next;
    }
    printf("END\n");
}
