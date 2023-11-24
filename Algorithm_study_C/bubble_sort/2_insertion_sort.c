#include <stdio.h>

// Insertion Sort 함수
void insertionSort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        // 현재 요소보다 큰 원소를 찾아서 오른쪽으로 이동
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}



int main() {
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    printf("insertion sort\n");
    printf("정렬 전 배열: \n");
    for(int i=0; i<n; i++){
        printf("%d ",arr[i]);

    }

    // Insertion Sort 호출
    insertionSort(arr, n);

    printf("\n정렬 후 배열: \n");
    for(int i=0; i<n; i++){
        printf("%d ",arr[i]);

    }
    return 0;
}
