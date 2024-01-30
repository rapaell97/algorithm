test = int(input())
for u in range(test):
    x = int(input())
    nums = input()
    counts = [0 for _ in range(10)]

    for i in nums:
        counts[int(i)] += 1

    max_cnt = 0
    max_num = 0
    for i in range(len(counts)):
        if counts[i] >= max_cnt:
            max_cnt = counts[i]
            max_num = i

    print(f"#{u+1} {max_num} {max_cnt}")

