#include <iostream>
#include <string>

int main() {
    int n;
    std::cout << "10진법 정수를 입력하세요: ";
    std::cin >> n;

    if (n < 0) {
        std::cout << "음수는 처리하지 않습니다." << std::endl;
        return 1;
    }

    std::string base_3_str = "";

    while (n > 0) {
        base_3_str = std::to_string(n % 3) + base_3_str;
        n /= 3;
    }

    std::string reversed_base_3_str = base_3_str;
    std::reverse(reversed_base_3_str.begin(), reversed_base_3_str.end());

    int reversed_integer = std::stoi(reversed_base_3_str, 0, 3);

    std::cout << "3진법 표현: " << base_3_str << std::endl;
    std::cout << "역순된 정수: " << reversed_integer << std::endl;

    return 0;
}