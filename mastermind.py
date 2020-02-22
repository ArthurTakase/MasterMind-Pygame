from random import choice

def soluce_def(color):
    soluce = []
    for i in range(4):
        soluce.append(choice(color))
    return soluce
