# Nghia Pham
# ngmpham@ucsc.edu
# programming assignment 6
# This program will ask the user to enter anyword and then it will give back the anagram of that word for the user.

def norm(s):
    """
    Returns the norm of a string obtained by alphabetizing its characters.
    """
    alpha = "".join(sorted(s))
    return alpha


# end norm()

def AnagramDictionary(f):
    """
    Returns a dictionary whose keys are the norms of the words in file f, and
    whose values are lists of words with a given norm. Thus each list contains
    a group of words in f that are anagrams of each other.
    """
    # Makes a list of all the words without newline character
    readList = f.readlines()
    D = []
    #get rid of \n
    for i in range(len(readList)):
        D.append(readList[i].strip("\n"))
    # assign values to dictionanry
    d = dict()
    for i in range(len(D)):
        if norm(D[i]) not in d:
            d[norm(D[i])] = [D[i]]
        else:
            d[norm(D[i])].append(D[i])
    return d


# end AnagramDictionary()

def printWordList(L):
    """Prints the words in L on a single line, separated by commas."""
    for i in range(len(L)):
        if i == len(L) - 1:
            print(L[i])
        else:
            print(L[i] + ", ", end="")
# end printWordList()


# main() ----------------------------------------------------------------------
def main():
    # open a word file, assemble the dictionary using words, close file
    inpu = open('scrabble.txt')
    AnaD = AnagramDictionary(inpu)
    inpu.close()

    user = str(input("\nEnter a string (or nothing to quit): "))
    while user != "":
        if norm(user) in AnaD:
            print("")
            print("The anagrams of " + user + " are:")
            printWordList(AnaD[norm(user)])
            print("")
        else:
            print("")
            print("The letters in '" + user + "' do not form a word in the dictionary")
            print("")

        user = str(input("Enter a string (or nothing to quit): "))
    print("")
    print("Bye!")
    print("")


# end main() ------------------------------------------------------------------

# -----------------------------------------------------------------------------
if (__name__ == '__main__'):
    main()

# end if ----------------------------------------------------------------------