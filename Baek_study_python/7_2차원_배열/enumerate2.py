my_list = ['apple', 'banana', 'cherry']
# 요소와 인덱스를 함께 얻음
print(*enumerate(my_list))
print(my_list)
print(*my_list)

for index, value in enumerate(my_list):
    print(f"{index}  {value}")

# 시작 인덱스를 지정할 수 있음
for index, value in enumerate(my_list, start=1):
    print(f"{index}  {value}")

