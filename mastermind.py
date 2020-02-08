from random import choice

taille = 4
color = ['jaune', 'bleu', 'rouge', 'vert']

def soluce_def():
    soluce = []
    for i in range(taille):
        soluce.append(choice(color))
    return soluce
