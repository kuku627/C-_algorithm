#include <iostream>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    
    int A[N][M], B[N][M], result[N][M];
    
    // 행렬 A 입력
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> A[i][j];
        }
    }
    
    // 행렬 B 입력
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> B[i][j];
        }
    }
    
    // 두 행렬 덧셈
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            result[i][j] = A[i][j] + B[i][j];
        }
    }
    
    // 결과 출력
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cout << result[i][j] << " ";
        }
        cout << endl;
    }
    
    return 0;
}

/*
제공한 C++ 코드는 행렬 A와 B를 입력 받고, 이를 더하여 결과를 출력하는 간단한 프로그램입니다. 아래에서 코드의 각 부분을 설명하겠습니다.

헤더 파일 포함:

cpp
Copy code
#include <iostream>
using namespace std;
#include <iostream>: 이 코드는 C++ 표준 라이브러리에서 입력과 출력을 위해 필요한 헤더 파일 <iostream>을 포함하고 있습니다.
using namespace std;: std 네임스페이스를 사용하겠다는 선언입니다. 이렇게 하면 cin과 cout 등의 입출력 관련 기능을 편리하게 사용할 수 있습니다.
main 함수:

cpp
Copy code
int main() {
C++ 프로그램은 main() 함수로 시작합니다. int는 함수의 반환 타입을 나타내며, main() 함수는 정수 값을 반환합니다.
변수 선언:

cpp
Copy code
int N, M;
N과 M은 행렬의 크기를 나타내는 정수형 변수입니다.
입력:

cpp
Copy code
cin >> N >> M;
cin은 C++에서 입력을 받는 객체로, >> 연산자를 사용하여 변수 N과 M에 값을 입력받습니다.
배열 선언:

cpp
Copy code
int A[N][M], B[N][M], result[N][M];
int 타입의 2차원 배열 A, B, result를 선언합니다. 이 배열들은 입력된 행렬과 결과를 저장하는데 사용됩니다.
행렬 A 입력:

cpp
Copy code
for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
        cin >> A[i][j];
    }
}
중첩된 반복문을 사용하여 A 행렬의 요소를 입력받습니다. i와 j는 반복문의 제어 변수로 사용됩니다.
행렬 B 입력:

cpp
Copy code
for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
        cin >> B[i][j];
    }
}
A와 마찬가지로 B 행렬의 요소를 입력받습니다.
두 행렬 덧셈:

cpp
Copy code
for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
        result[i][j] = A[i][j] + B[i][j];
    }
}
중첩된 반복문을 사용하여 A와 B 행렬의 같은 위치에 있는 요소들을 더한 결과를 result 배열에 저장합니다.
결과 출력:

cpp
Copy code
for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
        cout << result[i][j] << " ";
    }
    cout << endl;
}
중첩된 반복문을 사용하여 result 배열의 값을 출력합니다. cout은 C++에서 출력을 수행하는 객체로, << 연산자를 사용하여 값을 출력합니다. endl은 줄 바꿈을 나타냅니다.
프로그램 종료:
cout << result[i][j] << " ";

이 줄은 현재 행과 열의 인덱스에 해당하는 result 배열의 값을 화면에 출력합니다.
result[i][j] : 2차원 배열 result에서 i번째 행과 j번째 열에 있는 값을 가져옵니다.
<< " " : 값을 출력한 후 공백 문자를 출력합니다.
cout << endl;

현재 행의 모든 열에 대한 출력이 끝났을 때, 개행 문자(endl)를 사용하여 줄을 바꿉니다.
마지막으로, 외부 반복문이 모든 행에 대해 내부 반복문을 실행하고, 모든 행의 열을 출력한 후에 외부 반복문이 종료됩니다

cpp
Copy code
return 0;
main() 함수의 끝에 return 0;을 사용하여 프로그램이 성공적으로 종료되었음을 나타냅니다. 이 값은 프로그램의 종료 코드를 나타냅니다. 일반적으로 0은 성공을 나타냅니다.






*/
