def check(a,b):
    while a < b:
        sum = 1
        a = a + 1
        sum = sum + a
        return

a = int(input())
b = int(input())
sum = 1
if a > b:
    c = a
    a = b
    b = c
    total=check(a,b)
    print(total)
else:
    total = check(a, b)
    print(total)