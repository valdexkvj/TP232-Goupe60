import pandas as pd
import random
import utils as ut

n = ut.n #taille du dataset

nom = ut.nomf #nom de l'utilisateur

seed = sum([ord(c) for c in nom])

random.seed(seed)
maths = []
ids = []
heures = []
series = []

for i in range(n):
    s = random.choices(["scientifique", "littéraire"], weights=[0.3,0.7],k=1)[0]
    series.append(s)

    if s == "scientifique":
        if random.random() < 0.7:
            heures.append(random.randint(10, 100))
            maths.append(random.randint(8, 20))
            
        else:
            heures.append(random.randint(0, 25))
            maths.append(random.randint(0, 15))          
       
    else:
        if random.random() < 0.8:
            heures.append(random.randint(0, 30))
            maths.append(random.randint(0, 11))
            
        else:
            heures.append(random.randint(20, 100))
            maths.append(random.randint(8, 20))
            
    ids.append(f"E{i}")

data = {
    "ID":ids,
    "Maths": maths,
    "series": series,
    "Heures_d_etude": heures,
}

df = pd.DataFrame(data)
df.to_csv(ut.nomf, index=False)





