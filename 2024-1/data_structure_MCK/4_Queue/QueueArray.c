// 원형 Q로 구현
#include <stdio.h>
#include <stdlib.h>

typedef int element;
int size = 10, rear = -1, front = 0;
element *queue;

int main(void){
    queue = (element*)malloc(sizeof(element) * size);
}

bool IsFullQ(){
    if((rear+1)/size == front) return 1;
    return 0;
}

bool IsEmptyQ(){
    if(front == rear) return 1;
    return 0;
}

void addQ(int front, int rear,element item){
    rear = (++rear) % size;
    if(IsFull()) return;
    queue[rear] = item;
}


void deleteQ(){
    if(IsEmptyQ()) return;
    front = (++front) % size;
    return queue[front];
}