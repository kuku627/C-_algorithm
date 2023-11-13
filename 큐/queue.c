#include <stdio.h>

#define MAX_QUEUE_SIZE 5

// 큐 구조체 정의
typedef struct {
    int front, rear;
    int elements[MAX_QUEUE_SIZE];
} Queue;

// 큐 초기화 함수
void initQueue(Queue *q) {
    q->front = -1;
    q->rear = -1;
}

// 큐가 비어있는지 확인하는 함수
int isEmpty(Queue *q) {
    return q->front == -1;
}

// 큐가 가득 찼는지 확인하는 함수
int isFull(Queue *q) {
    return (q->rear + 1) % MAX_QUEUE_SIZE == q->front;
}

// 큐에 데이터 추가 (Enqueue) 함수
void enqueue(Queue *q, int data) {
    if (isFull(q)) {
        printf("Queue is full. Cannot enqueue.\n");
        return;
    }

    if (isEmpty(q)) {
        q->front = 0;
    }

    q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
    q->elements[q->rear] = data;
    printf("Enqueued: %d\n", data);
}

// 큐에서 데이터 제거 (Dequeue) 함수
int dequeue(Queue *q) {
    if (isEmpty(q)) {
        printf("Queue is empty. Cannot dequeue.\n");
        return -1;
    }

    int data = q->elements[q->front];

    if (q->front == q->rear) {
        // 큐에 마지막 원소가 제거되면 큐를 비움
        initQueue(q);
    } else {
        q->front = (q->front + 1) % MAX_QUEUE_SIZE;
    }

    printf("Dequeued: %d\n", data);
    return data;
}

int main() {
    Queue myQueue;
    initQueue(&myQueue);

    enqueue(&myQueue, 10);
    enqueue(&myQueue, 20);
    enqueue(&myQueue, 30);

    dequeue(&myQueue);
    dequeue(&myQueue);

    enqueue(&myQueue, 40);
    enqueue(&myQueue, 50);

    return 0;
}

