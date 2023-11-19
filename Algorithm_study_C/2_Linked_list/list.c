
//이해.
struct node {
	char *data; /*데이터 필드 : 하나의 문자열 저장 */
	struct node *next; /*링크 필드 : 다음 노드의 주소 저장 */
}

typedef struct node Node;
Node *head = NULL; /* 첫 번째 노드의 주소를 저장할 포인터 */


int main() {
	/* 첫번째 노드 추가 & head에 연결 */
	head = (Node *)malloc(sizeof(Node));
	head->data = "Tuesday";
	head->next = NULL;

	/* 두번째 노드 추가 & 첫번째 노드에 연결 */
	Node *q = (Node *)malloc(sizeof(Node));
	q->data = "Thursday";
	q->next = NULL;
	head->next = q;

	/* Tuesday 노드 앞에 Monday 노드 연결(새로운 첫번째 노드)*/
	q = (Node *)malloc(sizeof(Node));
	q->data = "Monday";
	q->next = head;
	head = q;

	/* 세 개의 노드를 순서대로 출력하기 */
	Node *p = head;
	while (p!=NULL) {
		printf("%s\n", p->data); //p가 현재 가리키고있는 노드를 출력한다.
		p = p->next; //p가 다음 노드를 가리키도록 한다. (next에는 다음 노드의 주소가 담겨있음)

		/* 다음 노드가 없다면, p==NULL이 되기 때문에 반복문이 종료된다 */
	}

/* 첫번째 노드를 가리키는 포인터 head가 전역변수인 경우 */
void add_first(char *item) {
	Node *tmp = (Node *)malloc(sizeof(Node));
	tmp->data = item;
	tmp->next = head;
	head = tmp;
}


	return 0;
}
