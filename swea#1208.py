for u in range(10):
    dump = int(input())
    box = list(map(int, input().split()))

    i =
    maxindex = 0
    minindex = 0

    while i <= dump:
        maxbox = 0
        minbox = 100
        for j in range(len(box)):
            if box[j] >= maxbox:
                maxbox = box[j]
                maxindex = j
        for j in range(len(box)):
            if box[j] <= minbox:
                minbox = box[j]
                minindex = j
        # print(box[maxindex], box[minindex])
        if maxbox - minbox == 0 or maxbox - minbox == 1:
            print(f"#{u+1} {box[maxindex] - box[minindex]}")
            break

        else:
            box[maxindex] -= 1
            box[minindex] += 1
        i += 1

    print(f"#{u+1} {box[maxindex] - box[minindex]}")
    # print(box[maxindex],box[minindex])



