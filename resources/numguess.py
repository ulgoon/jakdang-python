import random


answer = random.randint(1,100)
print(answer)

name = input("What is your name? ")
guess = int(input("Hi, %s. Guess the number? " % name))
print(guess)

if guess == answer:
    print("Congrats!!")
else:
    print("Wrong! The answer was %d." % answer)
