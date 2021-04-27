import random
import copy

#Should work
class Clausel():
    def __init__(self, arg, trim = False):
        #Posivtive literals
        self.p = set()
        #Negative literals
        self.n = set()
        if(not trim):
            self.parse(arg)
        
    def __hash__(self):
            return hash((frozenset(self.p), frozenset(self.n)))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.p == other.p and self.n == other.n

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
    def __str__(self):
        values = []
        for value in self.p:
            values.append(value)
        for value in self.n:
            values.append("-" + value)
        return " V ".join(values)

    def is_subset(self, other):
        return self.p.issubset(other.p) and self.n.issubset(other.n)

    def is_strict_subset(self, other):
        sub = self.is_subset(other)
        l1 = len(self.p) + len(self.n)
        l2 = len(other.p) + len(other.n)
        return sub and l1 < l2
#Should work
def Resolution(a,b):

    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    #Find intersections
    cond1 = a.p & b.n
    cond2 = a.n & b.p
    
    # print("From resolution: ", (cond1), (cond2))

    if(not bool(cond1) and not bool(cond2)):
        return False

    if(bool(cond1)):
        temp = random.sample(cond1, 1)[0]
        a.p.remove(temp)
        b.n.remove(temp)
    else:
        temp = random.sample(cond2, 1)[0]
        # print(temp)
        # print(temp, a.p, "\n")
        
        b.p.remove(temp)
        a.n.remove(temp)
        

    c = Clausel("", True)

    c.p = a.p | b.p # union
    c.n = a.n | b.n
    
    # print(c.p, c.n)
    if(bool(c.p & c.n)):
        return False
    # Do stuff
    return c

def solver(KB):
    while True:

        KB_p = copy.deepcopy(KB)
        KB = copy.deepcopy(KB)

        s = set()

        ## Add all resolutions to a set s
        my_list = list(KB)
        for i in range(len(KB)-1):
            for j in range(i+1, len(KB)):
                c = Resolution(my_list[i], my_list[j])
                if c is not False:
                    # print(c)
                    s.add(c)
        
        #Base case
        if(len(s)==0):
            return KB 

        KB = Incorporate(s, KB)
        
        #Catching another potential base case.
        if(KB_p == KB):
            return KB
   
                
def Incorporate(S, KB):
    for A in S:
        KB = Incorporate_clause(A, KB)
        KB.add(A) 
    return KB

def Incorporate_clause(A, KB):
    temp = set()

    for b in KB:
        if(is_strict_subset(A, b)):
            temp.add(b)
    #Might have to change this.
    for item in temp:
        KB.remove(item)
    return KB


def is_strict_subset(a,b):
    sub = a.is_subset(b)
    l1 = len(a.p) + len(a.n)
    l2 = len(b.p) + len(b.n)
    return sub and l1 < l2



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
    print()
    KB = set()
    KB.add(Clausel("-sun V -money V ice"))
    KB.add(Clausel("-money V ice V movie"))
    KB.add(Clausel("-movie V money"))
    KB.add(Clausel("-movie V -ice"))
    KB.add(Clausel("movie"))
    res = solver(KB)
    for item in res:
        print(item)