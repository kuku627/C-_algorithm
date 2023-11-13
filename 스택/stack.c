#include <stdio.h>
#include <stdlib.h>

// 스택의 최대 크기
#define MAX_SIZE 100

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

// 스택에 데이터를 추가 (push)
void push(Stack *stack, int value) {
    if (isFull(stack)) {
        printf("스택이 가득 찼습니다.\n");
    } else {
        stack->data[++stack->top] = value;
    }
}

// 스택에서 데이터를 제거하고 반환 (pop)
int pop(Stack *stack) {
    if (isEmpty(stack)) {
        printf("스택이 비어 있습니다.\n");
        return -1; // 에러를 나타내는 값 반환
    } else {
        return stack->data[stack->top--];
    }
}

// 스택의 맨 위 데이터 확인 (top)
int top(Stack *stack) {
    if (isEmpty(stack)) {
        printf("스택이 비어 있습니다.\n");
        return -1; // 에러를 나타내는 값 반환
    } else {
        return stack->data[stack->top];
    }
}

int main() {
    Stack stack;
    initStack(&stack);

    push(&stack, 1);
    push(&stack, 2);
    push(&stack, 3);

    printf("맨 위 데이터: %d\n", top(&stack));

    int popped_value = pop(&stack);
    printf("꺼낸 데이터: %d\n", popped_value);

    printf("현재 스택: ");
    while (!isEmpty(&stack)) {
        printf("%d ", pop(&stack));
    }
    printf("\n");

    return 0;
}
