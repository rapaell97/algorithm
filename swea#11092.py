test = int(input())
for u in range(test):
    num = int(input())
    nums = list(map(int,input().split()))

    max_num = max(nums)
    min_num = min(nums)

    if nums.count(max_num) >= 2:
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == max_num:
                max_index = i
                break
    else:
        max_index = nums.index(max_num)

    if nums.count(min_num) >= 2:
        for j in range(len(nums)):
            if nums[j] ==  min_num:
                min_index = j
                break
    else:
        min_index = nums.index(min_num)

    print(f"#{u+1} {abs(max_index-min_index)}")