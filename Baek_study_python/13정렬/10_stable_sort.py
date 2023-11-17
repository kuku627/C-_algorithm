n = int(input())
members = []

# 회원 정보 입력
for _ in range(n):
    age, name = input().split()
    members.append((int(age), name))

# # 정렬 함수를 사용하여 나이, 가입 순으로 정렬
sorted_members=sorted(members,key=lambda x: (x[0],x[1]))

# # 결과 출력
for member in sorted_members:
    print(member[0], member[1])

# for i in range(n):
#     print(members)

# x = [1, 2, 3]
# y = x  # y도 x와 같은 객체를 참조

# print(id(x))  # x 객체의 메모리 주소 출력
# print(id(y))  # y 객체의 메모리 주소 출력
