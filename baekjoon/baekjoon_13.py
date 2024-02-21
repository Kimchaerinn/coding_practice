#1546-A
n = int(input())
scores = sorted(list(map(int, input().split())))
sum = 0

for i in range(n):
    new = (scores[i]/scores[-1])*100
    sum += new

print(sum/n)


#1546-B
n = int(input())
scores = list(map(int, input().split()))
print(sum(scores)/max(scores)*100/n)   # sum(), max() 이용... 굳이 sort 안 써도 됨


#27866
S = input()
i = int(input())

print(S[i-1])


#2743
print(len(input()))


#9086-A    # 모든 입력 받은 후 한 번에 출력
t = int(input())
letter = []

for i in range(t):
    word = input()
    first, last = word[0], word[-1]
    letter.append(first+last)

for i in range(t):
    print(letter[i])


#9086-B    # 입력 한 번 받고 바로 출력(이래도 되는 줄 몰랐음...)
t = int(input())

for i in range(t):
    word = input()
    print(word[0]+word[-1])



