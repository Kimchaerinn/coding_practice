#1330
a, b = map(int, input().split())

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")


#9498
score = int(input())

if 90 <= score <= 100:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


#2753
year = int(input())

if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print("1")
    else:
        print("0")
else:
    print("0")

    
#14681-A
x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print("1")
    else:
        print("4")
else:
    if y > 0:
        print("2")
    else:
        print("3")

#14681-B    # A에 비해 가독성이 좋고 단순함
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
else:
    print("4")

