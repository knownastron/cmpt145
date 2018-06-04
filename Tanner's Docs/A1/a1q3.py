
n = int(input())
if n > 0:
    sq = []
    for i in range(n):
        line = input()
        row = [int(c) for c in line.rstrip().split()]
        sq.append(row)

    for r in range(n):
        for v in range(n):
            if (v+1) not in sq[r]:
                print('no')
                exit()
                
    for c in range(n):
        col = [sq[r][c] for r in range(n)]
        for v in range(n):
            if (v+1) not in col:
                print('no')
                exit()
                
    print('yes')
else:
    print('no')

