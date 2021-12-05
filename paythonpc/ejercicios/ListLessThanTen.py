mylist = [1, 1, 2, 3, 5, 8, 3, 13, 21, 34, 55, 89, 1, 4]
listless5=[]
for i in mylist:
    if i < 5:
        print(i)
        listless5.append(i)
print(listless5)

'''
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
'''
