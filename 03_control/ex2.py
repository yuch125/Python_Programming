# 반복문 : while문, for문

# while문
# 1 ~ 10까지 반복 출력
i = 0
while i < 10:
    i += 1
    print(i)
    # if i == 5:
    #     break
else:
    print("End")

nums = [1, 3, 5, 7, 9]
target = 2
i = 0

while i < len(nums):
    if nums[i] == target:
        break
    i += 1
else:
    print("못찾음")

# 1 ~ 10까지의 합
i = 1
tot = 0

while i <= 10:
    tot += i
    i += 1
print(f"sum = {tot}")

# 1~10 까지 짝수의 합
i = 0
tot = 0

while i <= 10:
    i += 1
    if i % 2 == 1:
        continue
    tot += i

print(f"sum = {tot}")
