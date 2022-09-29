# Be sure you've done pip install z3-solver
from z3 import *


# Here's a file you can often copy as a starting 
# point on a working program to solve some problem
# of interest. Here the problem is to compute and
# return a non-negative square root of argument, n 
def sqrt(n):
    
    
    # Create z3 variable(s) representing the unknown
    # Here, the unknown, x, is the square root of n.
    t = Int('t')
    sq = Int('s')
    c = Int('c')
    
    
    # Important: This is where you express what
    # values count as solutions using propositional
    # logic, but in the slightly different syntax
    # of Z3 expressions.
    L = ((t+sq+c)==10)
    M = ((c+sq-t)==6)
    N = ((c+t-sq)==4)
    k = And(L,M,N)     # combine using logical "and"
    
    
    # Create a Z3 "SMT" solver object, and give it 
    # the overall constraint to be solved, here C.
    s = Solver()
    s.add(k)
    
    # Run the Z3 model finder, capturing "sat"
    # or "unsat" as the return value 
    isSat = s.check()
    
    # If there's a model/solution return it 
    if (isSat == sat):
        return s.model()
    # otherwise return inconsistent value for error
    return -1

# Set up and run the function and report its results
n = 17
s = sqrt(n)
if (s == -1) :
    print("There is no real square root of", n)
else :
    print("The non-negative square root of", n, " is ", s)

