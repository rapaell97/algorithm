test = int(input())
for u in range(test):
    n,m = list(map(int,input().split()))
    lst = list()

    for w in range(n):
        line=list(map(int,input().split()))
        lst.append(line)

    catch_list=list()
    for k in range(n-m+1):
        for i in range(n-m+1):
            catch=0
            for p in range(i,i+m):
                for q in range(k,k+m):
                    catch+=lst[p][q]
            catch_list.append(catch)
    print(f"#{u+1} {max(catch_list)}")




