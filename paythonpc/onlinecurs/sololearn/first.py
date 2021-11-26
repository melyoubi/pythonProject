a = int(input())
b = int(input())
sum = 1
if a > b:

    c = a
    a = b
    b = c
    while a < b:
        a = a + 1
        sum = sum + a
else:
    while a < b:
        a = a + 1
        sum = sum + a
print(sum)
