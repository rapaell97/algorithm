h,w = map(int,input().split())
lst = [list(input()) for _ in range(h)]
result = [['x' for _ in range(w)]for _ in range(h)]
i = 0
while i < h:
    k = 0
    while k < w:
        if 