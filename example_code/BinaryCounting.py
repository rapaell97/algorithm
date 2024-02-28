# 민철이의 친구 중에 2명 이상의 친구를 선정하는 경우의 수

lst = ['a', 'b', 'c', 'd', 'e']
n = len(lst)


def get_count(tar):
    cnt = 0

    for i in range(n):
        # 1비트 1인지 확인
        if tar & 0x1:
            cnt += 1

        tar >>= 1
    return cnt


result = 0
for tar in range(1 << n):
    if get_count(tar) >= 2:
        result += 1

print(result)