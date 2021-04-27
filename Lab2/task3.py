import os
import sys
import itertools
import random

class theSchedule:

    def __init__(self, classes, room):
        self.room = room
        self.classes = classes


def schedule(classes, classrooms):
    if(len(classes)==0 | len(classrooms)==0):
        print("Error with classes/classrooms")
        return

    random.shuffle(classes)
    print((classrooms))
    # myScheudule = theSchedule(classes, classrooms)

    shc = []
    finallist = []
    temp = []
    index = 0

    ne = itertools.cycle(classrooms)
    for hour in hours:
        shc = []
        for i in classrooms:
            for klass in classes:
                #Checks if we have already used the class
                if (klass not in temp):
                    #Adds default 0 class to schedule.
                    if(index==0):
                        temp.append(klass)
                        shc.append([klass, hour, i])                        
                        finallist.append([klass, hour, i])                        
                        index+=1
                        break
                    #Checks if the class can go there based on the index
                    if(checkFirstdigit(klass, shc, hour)):
                        # print("class", klass)
                        temp.append(klass)
                        shc.append([klass, hour, i])    
                        finallist.append([klass, hour, i])    
                        break

    #Print function
    length=8
    print("   ", end="")
    meaninglesscounter = 0
    for n in classrooms:
        if(meaninglesscounter==2):
            print('{1:>{0}}'.format(length, n))
            break
        print('{1:>{0}}'.format(length, n), end=" ")
        meaninglesscounter+=1

    print("---------------------------------", end="")
    hour = 0
    length = 2
    for e in finallist:
        if(hour != e[1]):
            hour = e[1]
            print()
            print('{1:>{0}}'.format(length, hour), end="     ")
        print(e[0], "   ", end="")               
                        

def checkFirstdigit(input1, sch, hour):
    for input2 in sch:
        if(input1=="MT501" or input1 == "MT502"):
            return True
        if(input1[2] == input2[0][2]):
            if(hour == input2[1]):
                return False
            return False
    return True

classes = [
    "MT101",
    "MT102",
    "MT103",
    "MT104",
    "MT105",
    "MT106",
    "MT107",

    "MT201",
    "MT202",
    "MT203",
    "MT204",
    "MT205",
    "MT206",

    "MT301",
    "MT302",
    "MT303",
    "MT304",

    "MT401",
    "MT402",
    "MT403",

    "MT501",
    "MT502",
]

hours = [
    9, 10, 11, 12, 1, 2, 3, 4
]

classrooms = [
    "TP51",
    "SP34",
    "K3",
]
    
schedule(classes, classrooms)