#include <stdio.h>

// Bubble Sort 함수
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) 
        for (int j = 0; j < n-i-1; j++) 

            // 현재 요소가 다음 요소보다 크면 Swap
            if (arr[j] > arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        
    }



int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr)/sizeof(arr[0]);
    // printf("bubble sort\n");
    // printf("정렬 전 배열: \n");
    for(int i=0; i<n; i++)
        printf("%d ",arr[i]);

    

  
    bubbleSort(arr, n);

    // printf("\n정렬 후 배열: \n");
    printf("\n");
    for(int i=0; i<n; i++)
        printf("%d ",arr[i]);

    

    return 0;
}

