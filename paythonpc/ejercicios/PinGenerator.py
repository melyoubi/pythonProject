import random
'''3 PIN '''
print(" PIN CODE")
for i in range(1,4):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    pinlist = [a, b, c, d]
    print(pinlist)
'''3 PUK'''
print(" PUK CODE")
for i in range(1, 4):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    e = random.randint(0, 9)
    f = random.randint(0, 9)
    j = random.randint(0, 9)
    k = random.randint(0, 9)
    puklist = [a, b, c, d, e, f, j, k]
    print(puklist)