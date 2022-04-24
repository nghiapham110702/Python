#  Nghia Pham
#  ngmpham
#  CSE 20 Fall 2021
#  programming assignment 4
#  This program will ask the user to type in any number of integer that has to be positive number. Then the program
#  will help us to identify all the number that are prime and composite in the range that you choose.
def getIndices(L, x):
    Find = []
    for i in range(1, len(L)):
        if x == L[i]:
            Find.append(i)
    #return a list that increase in order of all indices i in L for which L[i]==x
        # end if
    # end for
    return Find

def makeSieve(n):
    W = []
    for i in range(n + 1):
        W.append(True)

    y = 2
    while (y ** 2 <= n):
        #W[y] is prime if it is not multiple of previous prime number.
        if (W[y] == True):
            #it will update the rest number as false if W[y] is prime.
            for i in range(y * 2, n + 1, y):
                W[i] = False
        y += 1
    W[0] = False
    W[1] = False
    return W


def main():
    print("")
    n = int(input("Enter a positive integer: "))
    # if the user input is less than 1 then it will ask user to type in input again and it has to be
    # positive
    while n < 1:
        n = int(input("Please enter a positive integer: "))
    Sieve = makeSieve(n)
    composites = getIndices(Sieve, False)
    primes = getIndices(Sieve, True)
    primeLenght = len(primes)
    compLenght = len(composites)

    # Print the list Prime numbers
    print("\nThere are " + str(primeLenght) + " prime numbers in the range 1 to " + str(n) + ":\n")
    for i in range(primeLenght):
        if primes[i]!=0:
            print(primes[i], end=" ")
            #if it divisble by 10 then it will print new line which mean it will print 10 number in fisrt row
            #then it will go to new line and print more number
            if (i + 1) % 10 == 0:
                print("")
    if n!=1:
        print("")

    # Print the list of Composite numbers
    print("\nThere are " + str(compLenght) + " composite numbers in the range 1 to " + str(n) + ":\n")
    for i in range(compLenght):
        print(composites[i], end=" ")
        # if it divisble by 10 then it will print new line which mean it will print 10 number in fisrt row
        # then it will go to new line and print more number
        if (i + 1) % 10 == 0:
            print("")
    print("\n")


if __name__ == '__main__':
    main()