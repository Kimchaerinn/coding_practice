#11021    # f-string 이용
t = int(input())    

for i in range(1, t+1):
    a, b = map(int, input().split())
    
    print(f'Case #{i}: {a+b}')


#11022
t = int(input())    

for i in range(1, t+1):
    a, b = map(int, input().split())
    
    print(f'Case #{i}: {a} + {b} = {a+b}')

    
#2438
n = int(input())

for i in range(1, n+1):
    print('*' * i)

    
#2439-A    
n = int(input())

for i in range(1, n+1):
    print(' ' * (n-1) + '*' * i)
    n -= 1
    i += 1

#2439-B    # 조금 더 생각하면... 코드를 간단히 짤 수 있음
n = int(input())

for i in range(1, n+1):
    print(' '* (n-i) + '*' * i)


#10952 
while True: 
    a, b = map(int, input().split())  
    sum = a + b    

    if sum != 0:
        print(sum)
    else:
        break

        
#10951
while True:    # 프로그램이 영원히 돌지 않게 하려면?
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

