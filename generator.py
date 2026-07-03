import pandas as pd
import random
import utils as ut

n = ut.n #taille du dataset

nom = ut.nomf #nom de l'utilisateur

seed = sum([ord(c) for c in nom])

random.seed(seed)
match = []
svt = []
inf = []
fr = []
ang = []
hist_geo = []
id = []
participation = []
for i in range(n):
    match.append(random.randint(0, 20))
    svt.append(random.randint(0, 20))
    inf.append(random.randint(0, 20))
    fr.append(random.randint(0, 20))
    ang.append(random.randint(0, 20))
    hist_geo.append(random.randint(0, 20))
    participation.append(random.randint(0, 100))
    id.append(f"E{i}")

data = {
    "ID":id,
    "Match": match,
    "SVT": svt,
    "Informatique": inf,
    "Français": fr,
    "Anglais": ang,
    "Histoire/Géographie": hist_geo,
    "Participation": participation
}

df = pd.DataFrame(data)
df.to_csv(ut.nomf, index=False)





