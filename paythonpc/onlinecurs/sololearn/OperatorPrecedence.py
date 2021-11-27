

'''The below code shows that == has a higher precedence than or'''
print(False == False or True)

print(False == (False or True))

print((False == False) or True)

'''Python's order of operations is the same as that of normal mathematics:
 parentheses first, then exponentiation, then multiplication/division, 
 and then addition/subtraction.'''
