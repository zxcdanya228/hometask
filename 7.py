n = int(input())

for i in range(n, 0, -1):
    m = i
    for _ in range(0, i + 1):
        print(_, end=' ')
    print()