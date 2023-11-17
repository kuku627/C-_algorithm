// C++ 코드 예시
#include <iostream>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    int arr[N][M];
    int maxVal = -1;
    int maxI, maxJ;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> arr[i][j];
            if (arr[i][j] > maxVal) {
                maxVal = arr[i][j];
                maxI = i;
                maxJ = j;
            }
        }
    }

    cout << "최댓값은 " << maxVal << "이며, 위치는 (" << maxI << ", " << maxJ << ")입니다." << endl;

    return 0;
}