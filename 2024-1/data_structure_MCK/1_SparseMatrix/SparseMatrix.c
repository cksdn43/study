#include <stdio.h>
#include <stdlib.h>

int count = 0;

int* make_sparse_matrix(int rows, int cols, int arr[][cols]){
    int* a = malloc(rows * cols * 3 * sizeof(int)); // 가정: 모든 원소가 0이 아니라면 최대 필요한 크기
    if(a == NULL) return NULL;

    int idx = 0;

    for(int row = 0; row < rows; row++){
        for(int col = 0; col < cols; col++){
            if (arr[row][col] != 0){
                a[idx] = row;
                a[idx+1] = col;
                a[idx+2] = arr[row][col];
                idx += 3;
                count++;
            }
        }
    }
    // 실제 사용된 메모리만큼 재할당
    a = realloc(a, idx * sizeof(int));
    return a;
}

int main(void){
    // int row = 4; int col = 4;
    // int matrix[row][col] = {{0,0,3,4},{0,0,5,7},{0,0,0,0},{0,2,6,0}};
    int row = 4; int col = 4;
    int matrix[row][col]; // 이 위치에서 선언하면 정상 작동함

    // 초기화
    matrix[0][0] = 0; matrix[0][1] = 0; matrix[0][2] = 3; matrix[0][3] = 4;
    matrix[1][0] = 0; matrix[1][1] = 0; matrix[1][2] = 5; matrix[1][3] = 7;
    matrix[2][0] = 0; matrix[2][1] = 0; matrix[2][2] = 0; matrix[2][3] = 0;
    matrix[3][0] = 0; matrix[3][1] = 2; matrix[3][2] = 6; matrix[3][3] = 0;


    int* sparse_matrix = make_sparse_matrix(row, col, matrix);
    if(sparse_matrix != NULL){
        int len = count*3;
        
        for(int i = 0; i < len; i += 3){
            printf("%d %d %d\n", sparse_matrix[i], sparse_matrix[i+1], sparse_matrix[i+2]);
        }





        free(sparse_matrix);
    }

    return 0;
}
