# https://latte-is-horse.tistory.com/373
# 문자열 탐색이 아니라, 처음 1 숫자부터 시작하여 차례차례 올라가는 방식

nums = input()
i = 0
while True :
    i += 1
    num = str(i)
    while len(num) > 0 and len(nums) > 0 :
        if num[0] == nums[0] :
            nums = nums[1:]
        num = num[1:]
    if nums == '' :
        print(i)
        break