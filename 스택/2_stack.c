#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 10

// 스택 구조체 정의
typedef struct {
    int data[MAX_SIZE];
    int top;
} Stack;

// 스택 초기화
void initStack(Stack *stack) {
    stack->top = -1;
}

// 스택이 비어 있는지 확인
int isEmpty(Stack *stack) {
    return stack->top == -1;
}

// 스택이 가득 찼는지 확인
int isFull(Stack *stack) {
    return stack->top == MAX_SIZE - 1;
}

// 스택에 데이터 추가 (push)
void push(Stack *stack, int value) {
    if (isFull(stack)) {
        printf("스택이 가득 찼습니다.\n");
    } else {
        stack->data[++stack->top] = value;
        printf("%d을(를) 스택에 추가했습니다.\n", value);
    }
}

// 스택에서 데이터 제거하고 반환 (pop)
int pop(Stack *stack) {
    if (isEmpty(stack)) {
        printf("스택이 비어 있습니다.\n");
        return -1; // 에러를 나타내는 값 반환
    } else {
        int poppedValue = stack->data[stack->top--];
        printf("%d을(를) 스택에서 꺼냈습니다.\n", poppedValue);
        return poppedValue;
    }
}

// 스택의 현재 상태 출력
void printStack(Stack *stack) {
    if (isEmpty(stack)) {
        printf("스택이 비어 있습니다.\n");
    } else {
        printf("현재 스택: ");
        for (int i = 0; i <= stack->top; i++) {
            printf("%d ", stack->data[i]);
        }
        printf("\n");
    }
}

int main() {
    Stack stack;
    initStack(&stack);

    push(&stack, 1);
    push(&stack, 2);
    push(&stack, 3);

    printStack(&stack);

    pop(&stack);
    printStack(&stack);

    return 0;
}

