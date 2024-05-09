#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef int element;

// 링크드 리스트의 노드 선언
typedef struct Node {
    element data;
    struct Node* link;
} Node;

// 링크드 리스트 선언
typedef struct LinkedList {
    Node* head;
    int size;
} LinkedList;

// dynamic array
element* Array_init(int size);
int Array_insertfront(element **arr, int *size, element value);
int Array_insertindex(element **arr, int *size, int idx, element value);
int Array_insertback(element **arr, int *size, element value);
element Array_deletefront(element **arr, int *size);
element Array_deleteindex(element **arr, int *size, int idx);
element Array_deleteback(element **arr, int *size);
element Array_getValue(element **arr,int *size,int idx);

// linked list
LinkedList* LinkedList_init();
int LinkedList_insertfront(LinkedList* LL, element value);
int LinkedList_insertindex(LinkedList* LL, element value, int idx);
int LinkedList_insertback(LinkedList* LL, element value, int key);
element LinkedList_deletefront(LinkedList* LL);
element LinkedList_deleteindex(LinkedList* LL, int idx);
element LinkedList_deleteback(LinkedList* LL);
element LinkedList_getValue(LinkedList* LL, int idx);


int main() {
    int Arraysize = 1024; // 크기 변경
    int idx = Arraysize / 2;
    
    element* arr = Array_init(Arraysize);
    if (!arr) return 1; // 메모리 할당 실패 확인

    printf("Dynamic Array\n");
    Array_deletefront(&arr, &Arraysize);
    Array_insertfront(&arr, &Arraysize, 9);
    Array_deleteindex(&arr, &Arraysize, idx);
    Array_insertindex(&arr, &Arraysize,idx, 9);
    Array_deleteback(&arr, &Arraysize);
    Array_insertback(&arr, &Arraysize, 9);
    Array_getValue(&arr, &Arraysize, idx);
    printf("메모리 사용량 %d\n", Arraysize*sizeof(element));
    free(arr);
    
    printf("Linked List\n");
    LinkedList* LL = LinkedList_init();
    for(int i = 0; i < Arraysize; i++) LinkedList_insertback(LL, 0, 0);
    LinkedList_deletefront(LL);
    LinkedList_insertfront(LL, 9);
    LinkedList_deleteindex(LL, idx);
    LinkedList_insertindex(LL, 9, idx);
    LinkedList_deleteback(LL);
    LinkedList_insertback(LL, 9, 1);
    LinkedList_getValue(LL, idx);
    printf("메모리 사용량 %d\n", sizeof(LinkedList)+LL->size*sizeof(Node));
    free(LL);

    return 0;
}

// 배열 초기화
element* Array_init(int size){
    element* arr = calloc(size, sizeof(element)); // (element*)malloc(size*sizeof(element));
    
    if (!arr){
        printf("메모리 할당 실패\n");
        return NULL;
    }

    return arr;
}

int Array_insertfront(element **arr, int *size, element value){
    // 측정 시간 선언
    struct timespec start, end;
    double time_taken;
    clock_gettime(CLOCK_MONOTONIC, &start);

    // 배열 크기 조정
    element *new_arr = realloc(*arr, (*size + 1) * sizeof(element));

    // 메모리 재 할당 실패
    if (!new_arr) {
        return -1; 
    }
    *arr = new_arr;

    // 요소 밀기 맨 끝에 넣을때는 동작X
    for (int i = *size; i > 0; i--) {
        (*arr)[i] = (*arr)[i - 1];
    }
    (*arr)[0] = value;
    (*size)++;

    // 시간 계산
    clock_gettime(CLOCK_MONOTONIC, &end);
    time_taken = (end.tv_sec - start.tv_sec) * 1e9;
    time_taken = (time_taken + (end.tv_nsec - start.tv_nsec)) * 1e-9;
    printf("앞 삽입 %.8f초\n", time_taken);
    return 1;
}

// 요소 삽입
int Array_insertindex(element **arr, int *size, int idx, element value){
    // 측정 시간 선언
    struct timespec start, end;
    double time_taken;
    clock_gettime(CLOCK_MONOTONIC, &start);

    // 인덱스가 음수거나 크기보다 크면 실패
    if (idx < 0 || idx > *size) { 
        return -1; 
    }

    // 배열 크기 조정
    element *new_arr = realloc(*arr, (*size + 1) * sizeof(element));

    // 메모리 재 할당 실패
    if (!new_arr) {
        return -1; 
    }
    *arr = new_arr;

    // 요소 밀기 맨 끝에 넣을때는 동작X
    for (int i = *size; i > idx; i--) {
        (*arr)[i] = (*arr)[i - 1];
    }
    (*arr)[idx] = value;
    (*size)++;

    // 시간 계산
    clock_gettime(CLOCK_MONOTONIC, &end);
    time_taken = (end.tv_sec - start.tv_sec) * 1e9;
    time_taken = (time_taken + (end.tv_nsec - start.tv_nsec)) * 1e-9;
    printf("인덱스 삽입 %.8f초\n", time_taken);
    return 1;
}

int Array_insertback(element **arr, int *size, element value){
    // 측정 시간 선언
    struct timespec start, end;
    double time_taken;
    clock_gettime(CLOCK_MONOTONIC, &start);

    // 배열 크기 조정
    element *new_arr = realloc(*arr, (*size + 1) * sizeof(element));

    // 메모리 재 할당 실패
    if (!new_arr) {
        return -1; 
    }
    *arr = new_arr;

    (*arr)[*size] = value;
    (*size)++;

    // 시간 계산
    clock_gettime(CLOCK_MONOTONIC, &end);
    time_taken = (end.tv_sec - start.tv_sec) * 1e9;
    time_taken = (time_taken + (end.tv_nsec - start.tv_nsec)) * 1e-9;
    printf("뒤 삽입 %.8f초\n", time_taken);
    return 1;
}


// 배열의 앞 요소 삭제
element Array_deletefront(element **arr, int *size){
    // 시간 측정
    struct timespec start, end;
    double time_taken;
    clock_gettime(CLOCK_MONOTONIC, &start);

    element value = (*arr)[0];
    // 삭제 연산 앞으로 밀기
    for (int i = 0; i < *size - 1; i++) {
        (*arr)[i] = (*arr)[i + 1];
    }
    element *new_arr = realloc(*arr, (--(*size)) * sizeof(element));
    
    // 메모리 재 할당 실패
    if (!new_arr) {
        return -1; 
    }
    *arr = new_arr;

    // 시간 계산
    clock_gettime(CLOCK_MONOTONIC, &end);
    time_taken = (end.tv_sec - start.tv_sec) * 1e9;
    time_taken = (time_taken + (end.tv_nsec - start.tv_nsec)) * 1e-9; 
    printf("앞 삭제 %.8f초\n", time_taken);
    
    return value;
}



// 배열의 특정 인덱스 요소 삭제
element Array_deleteindex(element **arr, int *size, int idx){
    // 시간 측정
    struct timespec start, end;
    double time_taken;
    clock_gettime(CLOCK_MONOTONIC, &start);

    // 인덱스가 음수거나 현재 크기보다 크면 실패
    if (idx < 0 || idx >= *size) { 
        printf("삭제 실패");
        return -1;
    }

    element value = (*arr)[idx];
    // 삭제 연산 앞으로 밀기 맨 뒤 삭제면 작동X
    for (int i = idx; i < *size - 1; i++) {
        (*arr)[i] = (*arr)[i + 1];
    }
    element *new_arr = realloc(*arr, (*size - 1) * sizeof(element));
    
    // 메모리 재 할당 실패
    if (!new_arr) {
        return -1; 
    }
    *arr = new_arr;
    (*size)--;

    // 시간 계산
    clock_gettime(CLOCK_MONOTONIC, &end);
    time_taken = (end.tv_sec - start.tv_sec) * 1e9;
    time_taken = (time_taken + (end.tv_nsec - start.tv_nsec)) * 1e-9; 
    printf("인덱스 삭제 %.8f초\n", time_taken);
    
    return value;
}

element Array_deleteback(element **arr, int *size){
    // 시간 측정
    struct timespec start, end;
    double time_taken;
    clock_gettime(CLOCK_MONOTONIC, &start);

    element value = (*arr)[(*size-1)];
    
    element *new_arr = realloc(*arr, (*size-1) * sizeof(element));
    
    // 메모리 재 할당 실패
    if (!new_arr) {
        return -1; 
    }
    *arr = new_arr;
    (*size)--;

    // 시간 계산
    clock_gettime(CLOCK_MONOTONIC, &end);
    time_taken = (end.tv_sec - start.tv_sec) * 1e9;
    time_taken = (time_taken + (end.tv_nsec - start.tv_nsec)) * 1e-9; 
    printf("뒤 삭제 %.8f초\n", time_taken);

    return value;
}

// 배열 접근
element Array_getValue(element **arr,int *size,int idx){
    // 시간 측정 시작
    struct timespec start, end;
    double time_taken;
    clock_gettime(CLOCK_MONOTONIC, &start);

    // 올바른 인덱스면
    if(idx >= 0 && idx < *size){
        element value = (*arr)[idx];

        // 시간 계산
        clock_gettime(CLOCK_MONOTONIC, &end);
        time_taken = (end.tv_sec - start.tv_sec) * 1e9;
        time_taken = (time_taken + (end.tv_nsec - start.tv_nsec)) * 1e-9; 
        printf("접근 %.8f초\n", time_taken);

        return value;
    }
    // 에러
    else {
        return -1; 
    }
}

// 링크드 리스트 초기화
LinkedList* LinkedList_init() {
    LinkedList* LL = (LinkedList*)malloc(sizeof(LinkedList));
    if (LL == NULL) {
        printf("메모리 할당 실패\n");
        return NULL;
    }
    LL->head = NULL;
    LL->size = 0;
    return LL;
}

int LinkedList_insertfront(LinkedList* LL, element value){
    // 시간 측정 시작
    struct timespec start, end;
    double time_taken;
    clock_gettime(CLOCK_MONOTONIC, &start);

    Node* insertNode = (Node*)malloc(sizeof(Node));
    if (insertNode == NULL) {
        return -1;
    }
    insertNode->data = value;
    insertNode->link = NULL;

    Node* currentNode = LL->head;
    // 리스트의 맨 앞에 삽입
    insertNode->link = LL->head;
    LL->head = insertNode;
    LL->size++;
    
    // 시간 계산
    clock_gettime(CLOCK_MONOTONIC, &end);
    time_taken = (end.tv_sec - start.tv_sec) * 1e9;
    time_taken = (time_taken + (end.tv_nsec - start.tv_nsec)) * 1e-9;
    printf("앞 삽입 %.8f초\n", time_taken);
    
    return 1;
}

// 요소 삽입 
int LinkedList_insertindex(LinkedList* LL, element value, int idx){
    // 인덱스 오류
    if (idx < 0 || idx > LL->size) {
        return 0;
    }

    // 시간 측정 시작
    struct timespec start, end;
    double time_taken;
    clock_gettime(CLOCK_MONOTONIC, &start);

    Node* insertNode = (Node*)malloc(sizeof(Node));
    if (insertNode == NULL) {
        return -1;
    }
    insertNode->data = value;
    insertNode->link = NULL;

    Node* currentNode = LL->head;
    // 리스트의 맨 앞에 삽입
    if (idx == 0) { 
        insertNode->link = LL->head;
        LL->head = insertNode;
    } 
    // 중간 또는 맨 뒤에 삽입
    else { 
        Node* previousNode = NULL;
        for (int i = 0; i < idx; i++) {
            previousNode = currentNode;
            currentNode = previousNode->link;
        }
        insertNode->link = currentNode;
        if (previousNode != NULL) {
            previousNode->link = insertNode;
        }
    }
    LL->size++;
    // 시간 계산
    clock_gettime(CLOCK_MONOTONIC, &end);
    time_taken = (end.tv_sec - start.tv_sec) * 1e9;
    time_taken = (time_taken + (end.tv_nsec - start.tv_nsec)) * 1e-9;
    printf("인덱스 삽입 %.8f초\n", time_taken);
    
    return 1;
}

int LinkedList_insertback(LinkedList* LL, element value, int key){
    // 시간 측정 시작
    struct timespec start, end;
    double time_taken;
    clock_gettime(CLOCK_MONOTONIC, &start);

    Node* insertNode = (Node*)malloc(sizeof(Node));
    if (insertNode == NULL) {
        printf("메모리 할당 실패\n");
        return 0;
    }
    insertNode->data = value;
    insertNode->link = NULL;

    // 리스트가 비어있으면 head에 바로 삽입
    if (LL->head == NULL) {
        LL->head = insertNode;
    } else {
        Node* currentNode = LL->head;
        while (currentNode->link != NULL) {
            currentNode = currentNode->link;
        }
        // 마지막 노드의 link를 새 노드로 연결
        currentNode->link = insertNode;
    }
    LL->size++;

    // 시간 계산
    clock_gettime(CLOCK_MONOTONIC, &end);
    time_taken = (end.tv_sec - start.tv_sec) * 1e9;
    time_taken = (time_taken + (end.tv_nsec - start.tv_nsec)) * 1e-9;
    if(key == 1) printf("뒤 삽입 %.8f초\n", time_taken); // 처음 값 넣어줄때는 출력 X
    
    return 1;
}

element LinkedList_deletefront(LinkedList* LL){
    // 시간 측정 시작
    struct timespec start, end;
    double time_taken;
    clock_gettime(CLOCK_MONOTONIC, &start);

    // 노드 삭제하고 앞 뒤 연결
    Node* currentNode = LL->head;

    LL->head = currentNode->link;

    element data = currentNode->data;
    free(currentNode);
    LL->size--;

    // 시간 계산
    clock_gettime(CLOCK_MONOTONIC, &end);
    time_taken = (end.tv_sec - start.tv_sec) * 1e9;
    time_taken = (time_taken + (end.tv_nsec - start.tv_nsec)) * 1e-9; 
    printf("앞 삭제 %.8f초\n", time_taken);
    
    return data;
}

// 노드 삭제
element LinkedList_deleteindex(LinkedList* LL, int idx){
    // 잘못된 인덱스
    if (idx < 0 || idx >= LL->size || LL->head == NULL) {
        return -1; 
    }

    // 시간 측정 시작
    struct timespec start, end;
    double time_taken;
    clock_gettime(CLOCK_MONOTONIC, &start);

    // 노드 삭제하고 앞 뒤 연결
    Node* currentNode = LL->head;
    Node* previousNode = NULL;

    if (idx == 0) {
        LL->head = currentNode->link;
    } else {
        for (int i = 0; i < idx; i++) {
            previousNode = currentNode;
            currentNode = currentNode->link;
        }
        previousNode->link = currentNode->link;
    }

    element data = currentNode->data;
    free(currentNode);
    LL->size--;

    // 시간 계산
    clock_gettime(CLOCK_MONOTONIC, &end);
    time_taken = (end.tv_sec - start.tv_sec) * 1e9;
    time_taken = (time_taken + (end.tv_nsec - start.tv_nsec)) * 1e-9; 
    printf("인덱스 삭제 %.8f초\n", time_taken);

    return data;
}

element LinkedList_deleteback(LinkedList* LL){
    // 링크드 리스트가 비었을 경우
    if (LL->head == NULL) {
        return -1;
    }
    // 시간 측정 시작
    struct timespec start, end;
    double time_taken;
    clock_gettime(CLOCK_MONOTONIC, &start);

    Node* currentNode = LL->head;
    Node* previousNode = NULL;

    // 노드 삭제하고 앞 뒤 연결
    // 마지막 노드로 이동
    while (currentNode->link != NULL) {
        previousNode = currentNode;
        currentNode = currentNode->link;
    }

    // 이전 노드가 NULL이면, 리스트에 노드가 하나만 있음
    if (previousNode == NULL) {
        LL->head = NULL;
    } else {
        previousNode->link = NULL;
    }

    element data = currentNode->data;
    LL->size--;
    free(currentNode);
    
    // 시간 계산
    clock_gettime(CLOCK_MONOTONIC, &end);
    time_taken = (end.tv_sec - start.tv_sec) * 1e9;
    time_taken = (time_taken + (end.tv_nsec - start.tv_nsec)) * 1e-9; 
    printf("뒤 삭제 %.8f초\n", time_taken);

    return data;
}

// 값 접근
element LinkedList_getValue(LinkedList* LL, int idx){
    // 잘못된 인덱스
    if (idx < 0 || idx >= LL->size || LL->head == NULL) {
        return -1; 
    }

    // 시간 측정 시작
    struct timespec start, end;
    double time_taken;
    clock_gettime(CLOCK_MONOTONIC, &start);

    Node* currentNode = LL->head;
    for (int i = 0; i < idx; i++) {
        currentNode = currentNode->link;
    }

    // 시간 계산
    clock_gettime(CLOCK_MONOTONIC, &end);
    time_taken = (end.tv_sec - start.tv_sec) * 1e9;
    time_taken = (time_taken + (end.tv_nsec - start.tv_nsec)) * 1e-9; 
    printf("접근 %.8f초\n", time_taken);

    return currentNode->data;
}