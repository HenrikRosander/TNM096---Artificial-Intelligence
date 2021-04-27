
from lab3_t1_t2 import *


# There was a robbery in which a lot of goods were stolen. The robber(s) left in
# a truck. It is known that:
# 1. Nobody else could have been involved other than A, B and C.
# 2. C never commits a crime without A’s participation.
# 3. B does not know how to drive.
# So, is A innocent or guilty?

mySet = set()
# 1. Nobody else could have been involved other than A, B and C.
mySet.add(Clausel("A V B V C"))
# These might not be nessacery
mySet.add(Clausel("A"))
mySet.add(Clausel("A V C"))
# 2. C never commits a crime without A’s participation.
mySet.add(Clausel("A V -C"))
# 3. B does not know how to drive.
mySet.add(Clausel("dA V dC"))
mySet.add(Clausel("-dB"))

solved = solver(mySet)
for n in solved:
    print(n)

# => A always needs to be guilty for the riddle to work.