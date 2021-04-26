import random


class Clausel():
    def __init__(self, arg):
        #Posivtive literals
        self.p = set()
        #Negative literals
        self.n = set()
        
        self.parse(arg)

    def parse(self, arg):
        a = arg.split("V")
        for var in a:
            var = var.strip()
            if("-" in var):
                var = var.strip("-")
                self.n.add(var)
            else:
                self.p.add(var)
        
        # print(self.p, self.n)

class C():
        def __init__(self, p, n):
            self.p = p
            self.n = n

def Resolution(a,b):

    #Find intersections
    cond1 = a.p & b.n
    cond2 = a.n & b.p
    
    # print("From resolution: ", (cond1), (cond2))

    if(not bool(cond1) and not bool(cond2)):
        return False

    if(bool(cond1)):
        temp = set(random.sample(cond1, 1))
        a.p = a.p - temp
        b.n = b.n - temp
    else:
        temp = set(random.sample(cond2, 1))
        # print(temp, a.p, "\n")
        b.p = b.p - temp
        a.n = a.n - temp




    c = C((a.p | b.p), (a.n | b.n))
    
    # print(c.p, c.n)
    if(bool(c.p & c.n)):
        return False
    
    
    # Do stuff
    return (c.p | c.n)
    

    
if __name__=="__main__":
    #Execute

    # This task is about to implement the resolution inference mechanism applied to formulae (called
    # clauses) in Conjunctive Normal Form (CNF) for propositional logic. In particular, you have to
    # write a program that implements:

    # 1. The resolution of two clauses in CNF. That is, given two clauses the program calculates
    # their resolvent by applying one resolution step.
    
    #Enter two Clausels 
    # C1: (A, B , C)
    # C2 : (>B, >C)
    A = Clausel("a V b V -c")
    B = Clausel("c V b")
    result = Resolution(A,B)
    print(result)

    A = Clausel("a V b v -c")
    B = Clausel("d V b V -g")
    result = Resolution(A,B)
    print(result)

    A = Clausel("-b V c V t")
    B = Clausel("-c V z V b")
    result = Resolution(A,B)
    print(result)


    # 2. The resolution mechanism applied to a given set S of clauses. Given S, the program selects
    # two arbitrary clauses from S, or any previously calculated resolvent, and calculates the
    # new resolvents2
    # . The program applies the resolution step until no new resolvent can be
    # derived.