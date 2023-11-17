#include <stdio.h>
#include <stdlib.h>

struct NODE {
    struct NODE *next;
    int data;
};

void addFirst(struct NODE *target, int data)
{
    if (target == NULL)                    // 기준 노드가 NULL 이면
        return;                            // 함수 종료
    struct NODE *newNode = malloc(sizeof(struct NODE));
    newNode->next = target->next;
    newNode->data = data;

    target->next = newNode;
}

void removeFirst(struct NODE *target)                // 기준 노드의 다음 노드를 삭제하는 함수
{
    if (target == NULL)                    // 기준 노드가 NULL 이면
        return;                            // 함수 종료

    struct NODE *removeNode = target->next;            // 기준 노드의 다음 노드 주소를 저장
    target->next = removeNode->next;                // r기준 노드의 다음 노드에 삭제할 노드의 다음 노드를 지정

    free(removeNode);            // 노드 메모리 해제
}

int main()
{
    struct NODE *head = malloc(sizeof(struct NODE));    

    head->next = NULL;

    addFirst(head, 10);
    addFirst(head, 20);
    addFirst(head, 30);

    removeFirst(head);        // 머리 노드 뒤에 있는 노드를 삭제

    struct NODE *curr = head->next;
    // 연결 리스트 순회용 포인터에 첫 번째 노드의 주소 저장
    while (curr != NULL)
    {
        printf("%d\n", curr->data);
        curr = curr->next;
    }

    curr = head->next;
    while (curr != NULL)
    {
        struct NODE *next = curr->next;
        free(curr);
        curr = next;        // 포인터에 다음 노드의 주소 저장
    }
    free(head);        // 머리노드 메모리 해제

    return 0;
}