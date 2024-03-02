test = int(input())
for u in range(test):
    h,w = map(int,input().split())
    map_lst = [list(input()) for _ in range(h)]
    case = int(input())
    command = list(input())

    move = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
    move_p = [-1, 0, 1, 0]
    move_q = [0, 1, 0, -1]
    tank = {'^':0,'>':1,'v':2,'<':3}

    for i in range(len(map_lst)):
        for k in range(len(map_lst[i])):
            if map_lst[i][k] in tank:
                p = i
                q = k

    for i in range(len(command)):
        if command[i] == 'U':
            map_lst[p][q] = '^'
            np = p + move_p[move['U']]
            nq = q + move_q[move['U']]
            if 0<= np <h and 0<= nq <w and map_lst[np][nq] == '.':
                map_lst[p][q] = '.'
                p = np
                q = nq
                map_lst[p][q] = '^'

        if command[i] == 'R':
            map_lst[p][q] = '>'
            np = p + move_p[move['R']]
            nq = q + move_q[move['R']]
            if 0<= np <h and 0<= nq <w and map_lst[np][nq] == '.':
                map_lst[p][q]='.'
                p = np
                q = nq
                map_lst[p][q] = '>'

        if command[i] == 'D':
            map_lst[p][q] = 'v'
            np = p + move_p[move['D']]
            nq = q + move_q[move['D']]
            if 0<= np <h and 0<= nq <w and map_lst[np][nq] == '.':
                map_lst[p][q] = '.'
                p = np
                q = nq
                map_lst[p][q] = 'v'

        if command[i] == 'L':
            map_lst[p][q] = '<'
            np = p + move_p[move['L']]
            nq = q + move_q[move['L']]
            if 0<= np <h and 0<= nq <w and map_lst[np][nq] == '.':
                map_lst[p][q] = '.'
                p = np
                q = nq
                map_lst[p][q] = '<'

        if command[i] == 'S':
            sp = p
            sq = q
            shoot = tank[map_lst[p][q]]
            while True:
                sp += move_p[shoot]
                sq += move_q[shoot]

                if 0<= sp <h and 0<= sq <w and map_lst[sp][sq] == '*':
                    map_lst[sp][sq] = '.'
                    break

                elif 0<= sp <h and 0<= sq <w and map_lst[sp][sq] == '#':
                    break

                elif 0<= sp <h and 0<= sq <w and map_lst[sp][sq] == '.':
                    continue

                elif 0<= sp <h and 0<= sq <w and map_lst[sp][sq] == '-':
                    continue

    print(f"#{u+1}",end=' ')
    for i in map_lst:
        for k in i:
            print(k,end='')
        print()
