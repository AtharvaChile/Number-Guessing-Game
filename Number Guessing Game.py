import random
import math

# Taking Inputs
lnum = int(input("Enter Lower number:- "))
unum = int(input("Enter Upper number:- "))

# generating random number between
x = random.randint(lnum, unum)
print("\n\tYou've only ",
      round(math.log(unum - lnum + 1, 2)),
      " chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(unum - lnum + 1, 2):
    count += 1

    # taking guessing number as input
    guess = int(input("Guess a number:- "))

    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

# If Guessing is more than required guesses,
# output.
if count >= math.log(unum - lnum + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
