#include <stdio.h>
#include <stdlib.h>

#define N 5  // 디스크의 개수, 입력에 따라 조정 가능

typedef struct {
    int capacity;
    int size;
    int *elements;
} Stack;

Stack* createStack(int capacity) {
    Stack *stack = (Stack *)malloc(sizeof(Stack));
    stack->capacity = capacity;
    stack->size = 0;
    stack->elements = (int *)malloc(sizeof(int) * capacity);
    return stack;
}

void push(Stack *stack, int element) {
    if (stack->size < stack->capacity) {
        stack->elements[stack->size++] = element;
    }
}

int pop(Stack *stack) {
    if (stack->size == 0) return -1;
    return stack->elements[--stack->size];
}

int top(Stack *stack) {
    if (stack->size == 0) return -1;
    return stack->elements[stack->size - 1];
}

void moveDisk(Stack *src, Stack *dest, char s, char d) {
    int pole1TopDisk = pop(src);
    int pole2TopDisk = pop(dest);

    if (pole1TopDisk == -1) {
        push(src, pole2TopDisk);
        printf("Move disk %d from %c to %c\n", pole2TopDisk, d, s);
    } else if (pole2TopDisk == -1) {
        push(dest, pole1TopDisk);
        printf("Move disk %d from %c to %c\n", pole1TopDisk, s, d);
    } else if (pole1TopDisk > pole2TopDisk) {
        push(src, pole1TopDisk);
        push(src, pole2TopDisk);
        printf("Move disk %d from %c to %c\n", pole2TopDisk, d, s);
    } else {
        push(dest, pole2TopDisk);
        push(dest, pole1TopDisk);
        printf("Move disk %d from %c to %c\n", pole1TopDisk, s, d);
    }
}

void iterativeHanoi(int num_of_disks, Stack *src, Stack *aux, Stack *dest) {
    int i, total_moves;
    char s = 'A', a = 'B', d = 'C';
    if (num_of_disks % 2 == 0) {
        char temp = d;
        d = a;
        a = temp;
    }
    total_moves = (1 << num_of_disks) - 1;

    for (i = num_of_disks; i >= 1; i--)
        push(src, i);

    for (i = 1; i <= total_moves; i++) {
        if (i % 3 == 1) {
            moveDisk(src, dest, s, d);
        } else if (i % 3 == 2) {
            moveDisk(src, aux, s, a);
        } else if (i % 3 == 0) {
            moveDisk(aux, dest, a, d);
        }
    }
}

int main() {
    Stack *src, *aux, *dest;

    src = createStack(N);
    aux = createStack(N);
    dest = createStack(N);

    iterativeHanoi(N, src, aux, dest);

    free(src->elements);
    free(aux->elements);
    free(dest->elements);
    free(src);
    free(aux);
    free(dest);

    return 0;
}
