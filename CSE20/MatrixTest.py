#------------------------------------------------------------------------------
#  MatrixTest.py
#------------------------------------------------------------------------------
from matrix import *

# main() ----------------------------------------------------------------------
def main():

   s = '1 2 3\n4 5 6'                     # 2x3
   t = '1 2 3 4\n5 6 7 8\n2 0 2 1'        # 3x4
   L = [[3,1],[4,2],[-1,5],[3,-2]]        # 4x2

   A = Matrix.from_string(s)              # 2x3
   B = Matrix.from_string(t)              # 3x4
   C = Matrix(L)                          # 4x2
   
   I2 = Matrix.identity(2)                # 2x2
   I3 = Matrix.identity(3)                # 3x3
   I4 = Matrix.identity(4)                # 4x4

   D = A.mult(B)                          # 2x4
   E = B.mult(C.scale(1.5))               # 3x2
   F = C.mult(A)                          # 4x3

   G = A.add(E.trans())                   # 2x3
   H = B.trans().sub(F)                   # 4x3
   J = E.add(A.trans())                   # 3x2

   K = G.mult(J)                          # 2x2
   M = E.mult(G)                          # 3x3
   N = F.mult(H.trans())                  # 4x4 

   # check arithmetic
   print()
   print('A =', A, sep='\n')
   print()
   print('B =', B, sep='\n')
   print()
   print('C =', C, sep='\n')
   print()
   print('D = A*B =', D, sep='\n')
   print()
   print('E = B*(1.5)C =', E, sep='\n')
   print()
   print('F = C*A =', F, sep='\n')
   print()
   print('G = A + E**T =', G, sep='\n')
   print()
   print('H = B**T - F =', H, sep='\n')
   print()
   print('J = E + A**T =', J, sep='\n')
   print()
   print('K = G*J = ', K, sep='\n')
   print()
   print('M = E*G =', M, sep='\n')
   print()   
   print('N = F*H**T =', N, sep='\n')
   print()
   print()

   # check Exceptions
   try:
      A.add(B)
   except ValueError as e:
      print('ValueError:', e, end='')
      print('continuing without interruption')
      print()
   # end try-except
   try:
      D.sub(E)
   except ValueError as e:
      print('ValueError:', e, end='')
      print('continuing without interruption')
      print()
   # end try-except
   try:
      G.mult(H)
   except ValueError as e:
      print('ValueError:', e, end='')
      print('continuing without interruption')
      print()
   # end try-except
   try:
      P = Matrix([[1,2,3],[4,5]])
   except ValueError as e:
      print('ValueError:', e)
      print('continuing without interruption')
      print()
   # end try-except
   try:
      Q = Matrix.from_string('1 2 3\n4 5\n')
   except ValueError as e:
      print('ValueError:', e)
      print('continuing without interruption')
      print()
   # end try-except
   print()

   # check associative law: (AB)C==A(BC), etc.
   print( A.mult(B).mult(C)==A.mult(B.mult(C)) )  # 2x2
   print( B.mult(C).mult(A)==B.mult(C.mult(A)) )  # 3x3
   print( C.mult(A).mult(B)==C.mult(A.mult(B)) )  # 4x4
   print()

   # check multiplication by identity matrices
   print( I2.mult(A).mult(I3)==A )
   print( I4.mult(F.mult(I3))==F )
   print( I2.mult(D).mult(I4)==D )
   print()
   print()

   help(Matrix)

# end main() ------------------------------------------------------------------

#------------------------------------------------------------------------------
if __name__=="__main__":

   main()

# end if ----------------------------------------------------------------------



