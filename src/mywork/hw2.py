# Be sure you've done pip install z3-solver
from z3 import *

# - In the Python file you will turn in, translate each rule as given
# here into a proposition in Z3 and assign that proposition to a 
# Python variable called Cn, where n is 1-19 corresponding to the
# enumeration below. For example, C3 = (Implies(And(X, Y), X). Note: 
# translate each context into a conjunction of its elements, and then
# translate ⊢ into propositional logic as →. For example, you can 
# translate the "and introduction" rule below into X ∧ Y → X ∧ Y.  
# - Below each such assignment, in comment, translate the rule into 
# English. For example, for the first rule you could write, "If X ∧ Y 
# is true, then it must be that X is true, as well." You might find it
# helpful to express X → Y as "whenever X is true, Y must be true."
# For example, you might translate "Raining → Wet" as "whenever it's
# raining, it's also wet," or "IF it's raining, THEN it's wet."
# -  State whether you believe the rule to be valid or not valid.
# - Use Z3 to check each rule for validity. If Z3 confirms that your 
# rule is valid, you're done. Your program should print "Cn is valid"
# for that rule, where n is the rule number.
# - For any rule that's not valid, have Z3 return a counterexample, 
# and translate the formal counter-example into a concrete example 
# in English and explain why it doesn't make sense. Put each such
# English language translation in a comment under the statement of
# the rule in Python.
# -/

# 1. X ∨ Y, X ⊢ ¬Y             -- affirming the disjunct
# 2. X, Y ⊢ X ∧ Y              -- and introduction
# 3. X ∧ Y ⊢ X                 -- and elimination left
# 4. X ∧ Y ⊢ Y                 -- and elimination right
# 5. ¬¬X ⊢ X                   -- negation elimination 
# 6. ¬(X ∧ ¬X)                 -- no contradiction
# 7. X ⊢ X ∨ Y                 -- or introduction left
# 8. Y ⊢ X ∨ Y                 -- or introduction right
# 9. X → Y, ¬X ⊢ ¬ Y           -- denying the antecedent
# 10. X → Y, Y → X ⊢ X ↔ Y      -- iff introduction
# 11. X ↔ Y ⊢ X → Y            -- iff elimination left
# 12. X ↔ Y ⊢ Y → X            -- iff elimination right
# 13. X ∨ Y, X → Z, Y → Z ⊢ Z  -- or elimination
# 14. X → Y, Y ⊢ X             -- affirming the conclusion
# 15. X → Y, X ⊢ Y             -- arrow elimination
# 16. X → Y, Y → Z ⊢ X → Z     -- transitivity of → 
# 17. X → Y ⊢ Y → X            -- converse
# 18. X → Y ⊢ ¬Y → ¬X          -- contrapositive
# 19. ¬(X ∨ Y) ↔ ¬X ∧ ¬Y       -- DeMorgan #1 (¬ distributes over ∨)
# 20. ¬(X ∧ Y) ↔ ¬X ∨ ¬Y       -- Demorgan #2 (¬ distributes over ∧)



x,y,z = Bools('x y z')


# 1. ((x\/y)/\x)->!y    
C1 =Implies(And(Or(x,y),x),Not(y))
#I beleive it is not valid since x and y could be both true and would make x or y true
#if x or y is true and x is true, y is false

# 2. X, Y -> X /\ Y   
# #if x and y are true seperately, x and y is true
#I think this rule is valid
C2 = Implies(And(x,y),And(x,y))

# 3. X /\ Y -> X  
# if x and y are true, x is true
#I think this rule is valid
C3 = Implies(And(x,y),x)

# 4. X /\ Y -> Y
# if x and y are true, y is true
#I think this rule is valid
C4 = Implies(And(x,y),y)

# 5. !!X -> X 
# if not not x is true, x is true
#I think this rule is valid
C5 = Implies(Not(Not(x)),x)

# 6. !(X /\ !X) 
# x and not x is false 
#I think this is valid
C6 = Implies(x,Not(And(x,Not(x))))

# 7. X -> X \/ Y
# if x is true, x or y is true
#I think this is valid
C7 = Implies(x,Or(x,y))

# 8. Y -> X \/ Y  
#if y is true, x or y is true
#I think that this is valid
C8 = Implies(y,Or(x,y))

# 9. X → Y, !X ⊢ ! Y   
# if x implies y and x is false, y is false
#I do not think this is valid because if x is false y could be true and the implies expression be true
C9 = Implies((And(Implies(x,y),Not(x))),Not(y))

# 10. X -> Y, Y -> X then -> X ↔ Y 
#if x implies y and y implies x, then x is true if and only if y is true
#I think that this will be valid
C10 = Implies(And(Implies(x,y),Implies(y,x)),(x==y))

# 11. X <=> Y -> (X -> Y )
#if x is true if and only if y is true, then x implies y 
# this is valid
C11 = Implies((x==y),Implies(x,y))

# 12. X <=> Y -> (Y -> X)
# if x is true if and only if y is true, then y implies x
# this is valid     
C12 = Implies((y==x),Implies(y,x)) 

# 13. X \/ Y, X → Z, Y → Z ,-> Z  -- or elimination
# if x or y and x implies z and y implies z, then z is true
# this will be valid
C13 = Implies(And(Or(x,y),Implies(x,z),Implies(y,z)), z)

# 14. X -> Y, Y -> X             -- affirming the conclusion
#if x implies y and y is true, then x is true
# when y is true and x is false, this is not valid
C14 = Implies(And(Implies(x,y),y),x)

# 15. X -> Y, X -> Y
# if x implies y and x is true, then y is true
#this is valid
C15 = Implies(And(Implies(x,y),x),y)           

# 16. X → Y, Y → Z --> X → Z  
# if x implies y and y implies z, then x implies z
# this is valid
C16 = Implies(And(Implies(x,y),Implies(y,z)),Implies(x,z))

# 17. X → Y --> Y → X        
#if x implies y, then y implies x
# this is not valid when y equals true and x is false
C17 = Implies(Implies(x,y),Implies(y,x))

# 18. X → Y ⊢ ¬Y → ¬X 
# if x implies y, then not y implies not x
#this is valid
C18 = Implies(Implies(x,y),Implies(Not(y),Not(x)))

# 19. !(X ∨ Y) <=> !X ∧ !Y       -- DeMorgan #1 (¬ distributes over ∨)
#  not(x or y) is true if and only if not or not y is true
# this is valid
C19 = (Not(Or(x,y))==And(Not(x),Not(y)))

# 20. !(X ∧ Y) <=> !X ∨ !Y       -- Demorgan #2 (¬ distributes over ∧)
# not(x and y) is true if and only if not x or not y is true
#this is valid
C20 = (Not(And(x,y))==Or(Not(x),Not(y)))

def inference(C):
    # x,y,z = Bools('x y z')
    s = Solver()
    

    s.add(Not(C))
    
    
    r = s.check()
    
    # If there's a model/solution return it 
    if (r==unsat):
        print("C is valid")
    else:
        print("Here's a counter-example: " , s.model())
    
    s.reset()

inference(C1)
inference(C2)
inference(C3)
inference(C4)
inference(C5)
inference(C6)
inference(C7)
inference(C8)
inference(C9)
inference(C10)
inference(C11)
inference(C12)
inference(C13)
inference(C14)
inference(C15)
inference(C16)
inference(C17)
inference(C18)
inference(C19)
inference(C20)
