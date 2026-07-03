import pandas as pd
from random import random


nom = "joyeux"
n = 200 #taille du dataset

def nom_f(nom):
    for c,i in zip(nom, range(len(nom))):
        if(c==" "):
            nom = nom[:i] + "_" + nom[i+1:]
    return nom
nomf = f"data/{nom_f(nom)}.csv"

try:
    notes = pd.read_csv(nomf)
except FileNotFoundError:
    print(f"Le fichier {nomf} n'existe pas. Veuillez exécuter generator.py pour générer le dataset.")
    exit(1)

# tableau moy scientifiques
notes_s = []
# tableau moy littéraires
notes_l = []
# note totale
notes_t = []
#fct qui fait la moyenne des notes 
def moyenne(notes):
    for i in range(n):
        ns = notes[["Match", "SVT", "Informatique"]].mean(axis=1)[i]
        nl = notes[["Français", "Anglais", "Histoire/Géographie"]].mean(axis=1)[i]
        notes_s.append(ns)
        notes_l.append(nl)
        notes_t.append((ns + nl) / 2)

moyenne(notes)

notes_s = pd.Series(notes_s)
notes_l = pd.Series(notes_l)    
notes_t = pd.Series(notes_t)    