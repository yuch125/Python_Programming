# 입출력

a = input()
print(a, end="")
print(type(a))
print(a, type(a), sep=",")

a = int(a)
print(a, type(a))

a = int(input())
print(a, type(a))

b = float(input())
print(b, type(b))

a = int(input())
b = int(input())

# 100스페이스200 하면 안됨 왜냐면 스페이스를 인트로 못바꿔서, 한줄로 입력하려면 다른방식으로 써야한다.

# 100 200 입력하고 싶으면
a = input().split()
print(a, type(a))

# map
# map(함수, List 객체) -> list 각각의 인자에 함수를 적용한다.
a, b, c = map(int, input().split())
print(a, b, c)

# 리스트 변환
a = list(map(int, input().split()))
print(a, type(a))
