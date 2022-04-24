# Nghia Pham
# ngmpham@ucsc.edu
# programming assignment 5
#This program will create the matrix NxN and with the Det function to calculate the determinant with random number.
# finally it will compute the absolute average of determinant.
#------------------------------------------------------------------
# ------------------------------------------------------------------
# Determinant.py
# ------------------------------------------------------------------
import random
def Det(M):
    '''
    Returns the determinant of a square matrix M.
    '''
    det = 1
    # This to prevent index out of range
    if M == []:
        return 1
    if type(M[0]) != list:
        return M[0]
    if len(M) != len(M[0]):
        return None
    for i in range(0, len(M)):
        for o in range(0, len(M[i])):
            if i > 0:
                break
            count = 0
            Matrix = [[]]
        #it fill up the matrix
            for k in range(0, len(M)):
                for m in range(0, len(M[i])):
                    if i > 0:
                        break
                    if o == m:
                        continue
                    elif i == k:
                        continue
                    else:
                        length = None
                        if len(Matrix[count]) == len(M[0]) - 1:
                            Matrix.append([])
                            count += 1
                            length = len(Matrix[count])
                            Matrix[count].append(M[k][m])
                        else:
                            Matrix[count].append(M[k][m])
            # This for get rid of blank list
            for l in range(len(Matrix)):
                if l>= len(Matrix):
                    break
                if Matrix[l] == []:
                    Matrix.pop(l)
            if o == 0:
                det = M[i][o] * Det(Matrix)
            elif o % 2 != 0:
                det = det + ((-1) * M[i][o]) * Det(Matrix)
            elif o % 2 == 0:
                det = det + M[i][o] * Det(Matrix)
    # print(determinant)
    return det
# end Det()
# main() ----------------------------------------------------------
def main(seed=None):
    rng = random.Random(seed)
    number = 10000
    print("")
    # print table heading
    print(" n          average of abs(det(M))")
    print("----------------------------------")
    # compute and print table body

    # for each n from 1 to 5
    for n in range(1, 6):
        S = 0
        # for each k from 1 to 10,000
        for k in range(0, number):
            # construct a random nxn matrix M
            # using rng.uniform(-5,5) to produce its entries
            # compute the absolute value of the determinant
            # of M and add it to an accumulating sum
            size = n
            # create matrix NxN
            M = [[0 for x in range(size)] for y in range(size)]
            for i in range(len(M)):
                for j in range(len(M[i])):
                    M[i][j] = rng.uniform(-5, 5)

            S = S + abs(Det(M))
        # compute the average of the absolute value of the determinants
        average = S /(k + 1)
        # print the average, formatted for the body of the table
        print(" " + str(n) + "           ", end="")
        print(f'{average:11.5f}')
    print("")
# end main() ------------------------------------------------------


# ------------------------------------------------------------------
if __name__ == "__main__":
    main()
# end if ----------------------------------------------------------
