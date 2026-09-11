# for문

# for (int i = 0; i< 10; i++)
# for i in iterable객체:

for i in range(5):
    print(i, end=" ")
print()

a = range(5)
print(a.start, a.stop, a.step)

# 1 ~ 5까지
for i in range(1, 6):
    print(i, end=" ")
print()

# 0~10 중 짝수 출력
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# 5 4 3 2 1 출력
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# 1 ~ 10까지의 합
tot = 0
for i in range(1, 11):
    tot += i
else:
    print(f"sum = {tot}")  # for else도 되네

print(sum(range(1, 11)))  # 변수면 조심, 위에 sum을 쓰면 그 이후에는 sum은 못씀

s = "hi12한글📝👾"  # 파이썬은 유니코드 써서 안깨짐

for c in s:
    print(c, end=" ")
print()

print(len(s))

# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j:<5d}", end=" ")
    print()
else:
    print("End")
