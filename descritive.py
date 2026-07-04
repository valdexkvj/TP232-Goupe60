import utils as ut    

try:
    notes = ut.pd.read_csv(ut.nomf)
except FileNotFoundError:
    print(f"Le fichier {ut.nomf} n'existe pas. Veuillez exécuter generator.py pour générer le dataset.")
    exit(1)


print(f"  Moyenne    : {notes['Maths'].mean():.2f}")
print(f"  Médiane    : {notes['Maths'].median():.2f}")
print(f"  Écart-type : {notes['Maths'].std():.2f}")
print(f"  Q1 (25%)   : {notes['Maths'].quantile(0.25):.2f}")
print(f"  Q2 (50%)   : {notes['Maths'].quantile(0.50):.2f}")
print(f"  Q3 (75%)   : {notes['Maths'].quantile(0.75):.2f}")
print()
print(f"  Heures d'étude - Moyenne    : {notes['Heures_d_etude'].mean():.2f}")   
print(f"  Heures d'étude - Médiane    : {notes['Heures_d_etude'].median():.2f}")   
print(f"  Heures d'étude - Écart-type : {notes['Heures_d_etude'].std():.2f}")   
print(f"  Heures d'étude - Q1 (25%)   : {notes['Heures_d_etude'].quantile(0.25):.2f}")
print(f"  Heures d'étude - Q2 (50%)   : {notes['Heures_d_etude'].quantile(0.50):.2f}")
print(f"  Heures d'étude - Q3 (75%)   : {notes['Heures_d_etude'].quantile(0.75):.2f}")