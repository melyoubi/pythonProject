def printwithexclam(word):
    print(word + "!!!")
printwithexclam("spam")
printwithexclam("eggs")

'''THIS OTHER FUNCTION WITH ARGUMENT'''
def print_double(x):
   print(2 * x)
print_double(3)

'''OTHER FUNCION WITH MORE THEN ONE ARGUMENT'''
def summe (x,y):
    print(x+y)
summe(5,4)

'''SUM USING FUNCTION FROM INPUT'''
def sumefrominput(x,y):
    print(x+y)

print('here i will sum values from input')
sumefrominput(int(input()),int(input()))