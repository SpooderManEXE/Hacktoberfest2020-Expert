for i in range(int(input())):
    n, k, s = list(map(int, input().split()))
    total = k * s
    count = 0
    val = False
    m = 0
    for j in range(1, s + 1):
        if (j % 7) != 0:
            count += n
            m += 1
        else:
            continue
        if count >= total:
            val = True
            break
    if val:
        print(m)
    else:
        print(-1)