#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 정수를 3진법 문자열로 변환하는 함수
void toBase3(int n, char *result) {
    int index = 0;
    while (n > 0) {
        result[index++] = (n % 3) + '0'; // 나머지를 문자로 변환하여 저장
        n /= 3;
    }
    result[index] = '\0'; // 문자열 종료
}

// 문자열을 역순으로 뒤집는 함수
void reverseString(char *str) {
    int len = strlen(str);
    for (int i = 0; i < len / 2; i++) {
        char temp = str[i];
        str[i] = str[len - i - 1];
        str[len - i - 1] = temp;
    }
}

int main(void) {
    int n;
    printf("10진법 정수를 입력하세요: ");
    scanf("%d", &n);

    // 정수를 3진법 문자열로 변환
    char base3_str[32]; // 충분한 크기의 배열 생성
    toBase3(n, base3_str);

    // 3진법 문자열을 역순으로 뒤집음
    reverseString(base3_str);

    // 역순으로 뒤집힌 3진법 문자열을 10진법 정수로 변환
    int reversed_integer = strtol(base3_str, NULL, 3);

    printf("3진법 표현: %s\n", base3_str);
    printf("역순된 정수: %d\n", reversed_integer);

    return 0;
}