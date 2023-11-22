// https://www.acmicpc.net/problem/2164

#include<stdio.h>
#include<stdlib.h>

typedef struct{
    int data[500000];
    int front;
    int rear;
} Queue;

void initQueue(Queue *q){
    q->front=0;
    q->rear =-1;
} 
void enqueue(Queue *q, int card_number){
    q->rear++;
    q->data[q->rear]=card_number;
}

int dequeue(Queue *q){
    int value = q->data[q->front];
    q->front++;
    return value;
}

int main(void){
int N;
int temp;


Queue card_q;
initQueue(&card_q);
scanf("%d",&N);
for(int i=1;i<=N;i++)
    enqueue(&card_q,i);


while(card_q.front<card_q.rear){
    dequeue(&card_q);

    temp=dequeue(&card_q);
    enqueue(&card_q,temp);

}

printf("%d", card_q.data[card_q.front]);

return 0;



}