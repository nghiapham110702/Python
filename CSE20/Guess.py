#  Nghia Pham
#  ngmpham
#  CSE 20 Fall 2021
#  programming assignment 3
# This program will ask the user input for the Random range number and they will have to guess it.
import random
# function main() -------------------------------------------------------------
def main():
    n = int(input("\nEnter a positive integer: "))
    number = random.randint(1,n)
    print("\nTry to guess my random integer in the range 1 to "+str(n)+"\n")
    incorrect = True
    for i in range(1, n+1):
        print("Guess "+str(i)+": ",end="")
        guess = int(input())
        if guess == number:
            if i==1:
                print("  ",guess,"is correct, you found my number in 1 guess :)\n")
            else:
                print("  ", guess, "is correct, you found my number in", i, "guesses :)\n")
            incorrect=False
            break
        elif guess > number:
            print("  ",guess,"is too high")
        elif guess < number:
            print("  ",guess, "is too low")
    if incorrect:
        print("   my number was " + str(number) + ", you're out of guesses :(\n")

# end main() ------------------------------------------------------------------
# closing conditional ---------------------------------------------------------
if __name__=='__main__':
    main()
# end -------------------------------------------------------------------------
