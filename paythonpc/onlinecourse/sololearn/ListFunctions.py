'''The append method adds an item to the end of an existing list. '''
list=[7,8,0,9]
print(list)
list.append(5)
print(list)
'''------------------------------------------------------------------------'''
'''To get the number of items in a list, you can use the len function.'''
listt=[7,8,0,9,9,8,7,8,9]
print(len(listt))
'''--------------------------------------------------------------------------'''
'''The insert method is similar to append, except that it allows
 you to insert a new item at any position in the list, 
 as opposed to just at the end.'''
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)
