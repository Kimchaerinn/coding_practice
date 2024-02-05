#95
d = []    # d = [[0 for j in range(20)] for i in range(20)]            
for i in range(20): 
    d.append([])
    for j in range(20):
        d[i].append(0)

n = int(input()) 
for i in range(n):
    x, y = map(int, input().split())
    d[x][y] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()

#96
d = []
for _ in range(19):
   d.append(list(map(int, input().split())))

n = int(input())
for _ in range(n):
  x, y = map(int, input().split())
  for i in range(19):
    d[x-1][i] = 0 if d[x-1][i] == 1 else 1
    d[i][y-1] = 0 if d[i][y-1] == 1 else 1
    
for row in d:
  print(*row)   # *... 리스트 요소 한 번에 출력
