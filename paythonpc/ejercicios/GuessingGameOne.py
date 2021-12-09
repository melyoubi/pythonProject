import random

a = random.randint(1, 9)
userinput = input('geuss a number')
c = 0
while str(userinput) != 'exit':
    userinput = int(userinput)
    if userinput > a:
        c += 1
        print("to high")
        userinput = input('geuss a number')
    elif userinput < a:
        c += 1
        print("to low")
        userinput = input('geuss a number')
    else:
        print("exactly")
        break

print(a)
print("trie", c)

'''Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess 
the number, then tell them whether they guessed too low, too high, or exactly righ
Keep the game going until the user types “exit”t'''
