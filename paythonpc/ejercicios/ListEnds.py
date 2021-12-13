#definetion the function
def listend(list):
    print(len(list))
    print(list[0] + list[len(list) - 1])
    mylist=[list[0], list[len(list) - 1] ]
    print(mylist)

#####################################################
print('hola tap yes to start')
start=input()
list=[1, 3, 4, 5, 6, 7, 8, 0, 4, 3, 2, 34, 5, 6]
#call the fynction
listend(list)


'''Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
 and makes a new list of only the first and last elements of the given list. For practice,
  write this code inside a function.'''