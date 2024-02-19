M , N = map(int,input().split())
shop = int(input())
shop_lst = [list(map(int,input().split())) for _ in range(shop)]
dong = list(map(int,input().split()))

ans = 0
for i in range(len(shop_lst)):
    if dong[0] == 1 or dong[0] == 2:
        if shop_lst[i][0] == 1 or shop_lst[i][0] == 2:
            if shop_lst[i][0] == dong[0]:
                temp = abs(shop_lst[i][1] - dong[1])
                ans += temp
            if shop_lst[i][0] != dong[0]:
                temp1 = (shop_lst[i][1] + N + dong[1])
                temp2 = (M - shop_lst[i][1]) + N + (M - dong[1])
                ans += min(temp1,temp2)
        else:
            if dong[0] == 1:
                if shop_lst[i][0] == 3:
                    temp = shop_lst[i][1] + dong[1]
                    ans += temp
                if shop_lst[i][0] == 4:
                    temp = (M - dong[1]) + shop_lst[i][1]
                    ans += temp
            if dong[0] == 2:
                if shop_lst[i][0] == 3:
                    temp = (N-shop_lst[i][1]) + dong[1]
                    ans += temp
                if shop_lst[i][0] == 4:
                    temp = (M - dong[1]) + (M - shop_lst[i][1])
                    ans += temp

    if dong[0] == 3 or dong[0] == 4:
        if shop_lst[i][0] == 3 or shop_lst[i][0] == 4:
            if shop_lst[i][0] == dong[0]:
                temp = abs(dong[1] - shop_lst[i][1])
                ans += temp
            if shop_lst[i][0] != dong[0]:
                temp1 = (dong[1] + M + shop_lst[i][1])
                temp2 = (N - dong[1]) + M + (N - shop_lst[i][1])
                ans += min(temp1,temp2)
        else:
            if dong[0] == 3:
                if shop_lst[i][0] == 1:
                    temp = shop_lst[i][1] + dong[1]
                    ans += temp
                if shop_lst[i][0] == 2:
                    temp = (N - dong[1]) + shop_lst[i][1]
                    ans += temp
            if dong[0] == 4:
                if shop_lst[i][0] == 1:
                    temp = M - shop_lst[i][1] + dong[1]
                    ans += temp
                if shop_lst[i][0] == 2:
                    temp = (M - shop_lst[i][1]) + (N - dong[1])
                    ans += temp

print(ans)