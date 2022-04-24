# ------------------------------------------------------------------------------
#  matrix.py
# ------------------------------------------------------------------------------
# Nghia Pham
# ngmpham@ucsc.edu
# programming assignment 7
# this program is where we use list and dictionary to create the classs matrix where we can do add, substract, or multiplication in matrix
from random import uniform


class Matrix:
    """Class representing a rectangular matrix."""

    # built-in methods ---------------------------------------------------------

    def __init__(self, L=[]):
        """
        Initialize a Matrix object from a list of lists. If the list is empty,
        the resulting Matrix is empty (size 0x0).
        """

        # get number of rows and columns
        n = self.numRows = len(L)
        m = self.numCols = (len(L[0]) if n > 0 else 0)
        self.elements = {}
        if n == 0:
            return
        # end if

        # build dictionary
        if n > 0:
            for i in range(n):
                if len(L[i]) != m:
                    msg = f'could not create Matrix from ragged list:\n{L}'
                    raise ValueError(msg)
                # end if
                for j in range(m):
                    self.elements[(i + 1, j + 1)] = L[i][j]
                # end for
            # end for
        # end if

    # end __init__()

    def __str__(self):
        """Return string representation of self."""
        forma = ""
        for i, k in self.elements:
            if self.numCols == k:
                forma += '%9s' % (str(("%.2f" % self.elements[i, k])) + "\n")
            else:
                forma += '%9s' % (str(("%.2f" % self.elements[i, k])) + " ")
        return forma[:-1]

    def __eq__(self, other):
        """Return True if self==other, False otherwise."""
        u = self.elements
        v = other.elements
        return u == v

    # Matrix instance methods --------------------------------------------------

    # fix up ValueError text to be more specific

    def add(self, other):
        """Return sum of self with other."""
        if self.numCols != other.numCols or self.numRows != other.numRows:
            raise ValueError("add(): incompatible matrix sizes:\n"+str(self.numRows)+"x"+str(self.numCols)+":\n"+str(self)+"\n"+str(other.numRows)+"x"+str(other.numCols)+":\n"+str(other)+"\n")
        list = []
        for i in range(1, self.numCols + 1):
            j = []
            for k in range(1, self.numRows + 1):
                j.append(self.elements[k, i] + other.elements[k, i])
            list.append(j)

        return Matrix(list).trans()

    def sub(self, other):
        """Return difference of self with other."""
        if self.numCols != other.numCols or self.numRows != other.numRows:
             raise ValueError("sub(): incompatible matrix sizes:\n"+str(self.numRows)+"x"+str(self.numCols)+":\n"+str(self)+"\n"+str(other.numRows)+"x"+str(other.numCols)+":\n"+str(other)+"\n")
        list = []
        for i in range(1, self.numCols + 1):
            j = []
            for k in range(1, self.numRows + 1):
                j.append(self.elements[k, i] - other.elements[k, i])
            list.append(j)
        return Matrix(list).trans()

    def scale(self, c):
        """Return the scalar product of self with c."""

        list = []
        for i in range(1, self.numCols + 1):
            k = []
            for j in range(1, self.numRows + 1):
                k.append(self.elements[j, i] * c)
            list.append(k)

        return Matrix(list).trans()

    def trans(self):
        """Return the transpose of self."""
        list = []
        for j in range(1, self.numCols + 1):
            k = []
            for i in range(1, self.numRows + 1):
                k.append(self.elements[i, j])
            list.append(k)

        return Matrix(list)

    def mult(self, other):
        """Return product of self by other."""
        if self.numCols == other.numRows or self.numRows == other.numCols:
            list = []
            for row in range(1, self.numRows + 1):
                k = []
                for col in range(1, other.trans().numRows + 1):
                    V = 0
                    for i in range(1, self.numCols + 1):
                        V= V + self.elements[row, i] * other.elements[i, col]
                    k.append(V)
                list.append(k)
            return Matrix(list)
        else:
           raise ValueError("mult(): incompatible matrix sizes:\n"+str(self.numRows)+"x"+str(self.numCols)+":\n"+str(self)+"\n"+str(other.numRows)+"x"+str(other.numCols)+":\n"+str(other)+"\n")
    # Matrix class methods -----------------------------------------------------

    def from_string(s=''):
        """Return the Matrix represented by the string s. If s is empty, the
        resulting Matrix is empty (size 0x0)."""
        L = s.split("\n")
        P = []
        list = []

        for i in range(len(L)):
            P.append(L[i].split(" "))
        
        for i in range(len(L)):
            if P[i] == [""]:
                P.pop(i)

        for i in range(len(P)):
            k = []
            for j in range(len(P[i])):
                k.append((int(P[i][j])))
            list.append(k)

        for i in range(len(list) - 1):
            if len(list[i]) != len(list[i + 1]):
                raise ValueError("from_string(): could not create Matrix from ragged string:\n"+repr(s))
        return Matrix(list)

    def identity(n):
        """Return the nxn identity Matrix."""
        list = []
        for i in range(n):
            j = []
            for k in range(n):
                if k == i:
                    j.append(1)
                else:
                    j.append(0)
            list.append(j)
        return Matrix(list)

    def randMatrix(n, m, a, b):
        """Return an nxm Matrix with random elements x, uniformly distributed over
        the interval a<=x<=b."""
        list = []

        for i in range(n):
            k = []
            for j in range(m):
                k.append(uniform(a, b))  
            list.append(k)

        return Matrix(list)

# end class Matrix ------------------------------------------------------------
