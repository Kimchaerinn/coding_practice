#11654
print(ord(input()))


#11720-A
n = int(input())
num = input()
sum = 0

for i in range(n):
    sum += int(num[i])

print(sum)

#11720-B    # sum() 사용
n = int(input())
nums = map(int, input())

print(sum(nums))


#10809-A
word = list(input())
alphabet = [(ord("a")+i) for i in range(26)]

for i in range(26):
    if chr(alphabet[i]) in word:
        print(word.index(chr(alphabet[i])), end=' ')

    else:
        print(-1, end=' ')

#10809-B    # 아스키코드, find() 이용
word = input()

for i in range(97, 123):    # 아스키코드 미리 지정
    print(word.find(chr(i)), end=' ')    # find()... 가장 처음 나타나는 인덱스 찾기


#2675-A
t = int(input())

for i in range(t):
    r, s = input().split()
    word = list(s)
    for j in range(len(s)):
        print(word[j]*int(r), end='')
    print()

#2675-B    # 굳이 range 안 쓴다면
for i in range(int(input())):
    r, s = input().split()
    for chr in s:
        print(chr*int(r), end='')
    print()
    
