#include <stdio.h>
#include <stdlib.h>

typedef int element;

typedef struct listNode{
    element data;
    listNode* link;
}listNode;

void delete(listNode** first,int idx){
    if(*first == NULL) return;
    listNode *deleteNode = *first;
    listNode *beforeNode = NULL;
    
    for(;idx > 0; idx--){
        beforeNode = deleteNode;
        deleteNode = deleteNode->link;
    }
    if (beforeNode){
        beforeNode->link = deleteNode->link;
    }else{
        *first = deleteNode->link;
    }
    before->link = deleteNode->link;
    free(deleteNode);
}

void insert(listNode* first,element value ,int idx){
    listNode* insertNode = (listNode*)malloc(sizeof(listNode));
    insertNode->data = value;
    if(first == NULL){
        fisrt = insertNode;
        return;
    }
    listNode* currentNode = first;
    for(;idx > 1; idx--){
        currentNode = currentNode->link;
    }
    insertNode->link = currentNode->link;
    currentNode->link = insertNode;
    return;
}

void getNode(listNode* first, int idx){

}


int main(void){
    return 0;
}