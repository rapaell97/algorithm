def biFind(arr,x):
    start = 0
    end = len(arr)-1
    cnt = 0
    while start <= end:
        mid = (start+end)//2
        cnt += 1
        if arr[mid] == x:
            return cnt
        elif arr[mid] > x:
            end = mid
        else:
            start = mid
    return cnt

test = int(input())
for u in range(test):
    book, a, b = map(int, input().split())
    lst = [x for x in range(1,book+1)]

    if biFind(lst,a) < biFind(lst,b):
        print(f"#{u+1} A")
    elif biFind(lst,a) > biFind(lst,b):
        print(f"#{u+1} B")
    else:
        print(f"#{u+1} 0")

