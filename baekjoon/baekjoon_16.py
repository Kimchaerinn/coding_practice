#25083
print('''         ,r'"7
r`-_   ,'  ,/
 \. ". L_r'
   `~\/
      |
      |''')


#3003-A
piece = list(map(int, input().split()))
set = [1, 1, 2, 2, 2, 8]
need = []

for i in range(6):    # 6 대신 len(piece)라고 표현할 수도
    need.append(set[i] - piece[i])    # 'need' 집합 없이 바로 출력한다면?
                                      # > print(set[i] - piece[i], end=' ')
print(*need)

#3003-B    # 결과에만 초점을 둔다면...
a, b, c, d, e, f = map(int, input().split())

print(1-a, 1-b, 2-c, 2-d, 2-e, 8-f)


#2444
n = int(input())

for i in range(1, n):
     print(' '*(n-i) + '*'*(2*i-1))

for i in range(n, 0, -1):
     print(' '*(n-i) + '*'*(2*i-1))