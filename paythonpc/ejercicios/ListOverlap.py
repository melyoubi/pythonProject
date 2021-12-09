a = [1, 1, 2, 3, 5, 8, 13, 21, 1, 34, 55, 13, 89]
b = [1, 2, 3, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list = []
for i in a :
    for  j in b :
        if i == j :
            list.append(i)
            break
print(list)
for k in list :
    if list.count(k) >=2 :
        list.remove(k)
        continue

print(list)


'''Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements
 that are common between the lists (without duplicates). Make sure your program works on two lists
  of different sizes.'''