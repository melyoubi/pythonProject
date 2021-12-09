import random

a = random.randint(1, 9)
userinput = input('geuss a number')

while str(userinput) != 'exit':
    userinput=int(userinput)
    if userinput > a:
        print("to high")
        userinput = input('geuss a number')
    elif userinput<a :
        print("to low")
        userinput = input('geuss a number')
    else:
        print("exactly")
        break

print(a)

'''Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess 
the number, then tell them whether they guessed too low, too high, or exactly righ
Keep the game going until the user types “exit”t'''
