#97
h, w = map(int, input().split())
n = int(input())
ldxy = [list(map(int, input().split())) for _ in range(n)]
arr = [[0 for _ in range(w)] for _ in range(h)]

for l, d, x, y in ldxy:
  x -= 1
  y -= 1
  for row in range(h):
    for col in range(w):
      if x == row and y == col:
        if d == 0:
          for i in range(l):
            arr[x][y+i] += 1
        if d == 1:
          for i in range(l):
            arr[x+i][y] += 1
for item in arr:
  print(*item)

