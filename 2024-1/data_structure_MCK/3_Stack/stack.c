#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef int element;

int top = 0;
int max = 5;
element* stack;

element IsEmpty(void);
element IsFull(void);
element pop(void);
void printall(void);
void push(element value);


int main() {
	stack = (element*)malloc(sizeof(element) * max);
	char words[30] = {""};
	int value = 0;
	int popvalue = 0;
	while (1) {
		printf("명령어: ");
		gets(words);
		strupr(words);
		
		if (!strcmp(words, "EXIT")) {
			break;
		}
		else if (!strcmp(words, "POP")) {
			popvalue = pop();
			if (popvalue != -1)
				printf("%d\n", popvalue);
			else printf("빔\n");
		}
		else if (!strcmp(words, "PUSH")) {
			printf("값: ");
			scanf_s("%d", &value);
			push(value);
			getchar(); 
			printf("완\n");
		}
		else if (!strcmp(words, "PRINTALL")) {
			printall();
		}
		else {
			printf("실패\n");
		}
	}
	free(stack);
	stack = NULL;
	return 0;
}


element IsEmpty(void) {
	if (top <= 0) return 1;
	else return 0;
}


element IsFull(void) {
	if (top >= max) return 1;
	else return 0;
}


void push(element value) {
	if (IsFull()) {
		max = max + 5;
		stack = realloc(stack, sizeof(element) * max); 
		if (stack == NULL) {
			exit(1); 
		}
	}
	stack[top++] = value;
}

element pop(void) {
	if (IsEmpty())  return -1;
	element a = stack[--top];
	return a;
}



void printall(void) {
	for (int i = top; i >= 0; i--) printf("%d\n", stack[i]);
}