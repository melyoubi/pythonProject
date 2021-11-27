'''To check if an item is in a list, the in operator can be used.
It returns True if the item occurs one or more times in the list, and False if it doesn't.'''
-------------------------------------------------------------------------------
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)
-------------------------------------------------------------------------------
'''The in operator is also used to determine whether or not 
a string is a substring of another string.'''
name='mohamed'
print('a'in name)
-------------------------------------------------------------------------------
'''To check if an item is not in a list, you can use the not operator in one of the following ways:'''
nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)
-------------------------------------------------------------------------------
'''cheking using if '''
list=['1','2','3','4']
if '4' in list:
    print('yes')
else:
    print('no')