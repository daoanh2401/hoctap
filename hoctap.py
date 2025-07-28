"""#Bai 1:
n = int(input())
a = 0
while n > 0:
    a += 1
    n = n // 10
print(a)
#Bai 2:
n = int(input())
daonguoc = 0
while n > 0:
    a = n % 10
    daonguoc = daonguoc * 10 + a
    n = n // 10
print(daonguoc)
#Bai 3:
n = int(input())
a = 0
for i in range(1, n):
    if n % i == 0:
        a += i
if n == a:
    print("la so hh")
else:
    print("ko la so hh")
#Bai 4: e kobt làm thầy ơi
    
#Bai 5:
n = int(input())
a = 0
for i in range(1, n+1):
    if n % i == 0:
        a += 1
if a == 2:
            print("la snt")
else:
            print("ko la snt")
#Bai 6:
#UCLN 2 số
a = int(input())
b = int(input())
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(f"UCLN 2 so a, b la: {b}")
#UCLN 3 số
c = int(input())
while b != c:
    if b > c:
        b = b - c
    else:
        c = c - b
print(f"UCLN 3 so a, b, c la: {c}")
#Bai 7: dùng if và elif đến hết
a, b, c, d, e = map(int,input().split())
if a >= b >= c >= d >= e:
    print(b)
elif a >= b >= c >= e >= d:
    print(b)
    #............
#Bai 8 :
for abc in range (100, 1000):
    a = abc // 100
    b = (abc - a*100) // 10
    c = abc % 10
    if abc == a**3 + b**3 + c**3:
        print(abc)"""
#Bai 9:
#Bai 10:
text = input()
if text == text[::-1]:
    print("la palindrome")
else:
    print("ko la palindrome")














