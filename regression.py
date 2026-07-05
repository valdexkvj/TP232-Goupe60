import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Chargement des données de l'établissement
try:
    df = pd.read_csv("donnees_eleves.csv")
    print("✓ Données chargées avec succès. Nombre d'élèves :", df.shape[0])
except FileNotFoundError:
    print("Erreur : Le fichier donnees_eleves.csv est introuvable. Placez le code dans le même dossier.")
    exit()

X = df['heures_etudes']
Y = df['note']

# 2. Calculs statistiques (Analyse bivariée)
correlation = X.corr(Y)
pente, ordonnee = np.polyfit(X, Y, 1)

print("\n=========================================")
print("     RÉSULTATS DE L'ANALYSE BIVARIÉE     ")
print("=========================================")
print(f"Coefficient de corrélation de Pearson (r) : {correlation:.4f}")
print(f"Équation de la droite de régression     : note = {pente:.4f} * heures + {ordonnee:.4f}")
print("=========================================\n")

# 3. Génération du Nuage de points (Scatter Plot) avec Droite de Régression
plt.figure(figsize=(8, 5.5))
sns.set_theme(style="whitegrid")

# Nuage de points bleus et droite de régression rouge
sns.regplot(x='heures_etudes', y='note', data=df, 
            scatter_kws={'alpha':0.7, 'color': '#2b6cb0'}, 
            line_kws={'color': '#e53e3e', 'lw': 2})

plt.title("Relation entre le Temps de Travail Personnel et la Note Évaluée", fontsize=12, fontweight='bold', color='#1a365d')
plt.xlabel("heures d'étude (heures / semaine)", fontsize=10)
plt.ylabel("note obtenue (/20)", fontsize=10)
plt.xlim(df['heures_etudes'].min() - 1, df['heures_etudes'].max() + 1)
plt.ylim(0, 21)

# Insertion des métriques clés directement sur le graphique
text_stats = f"r = {correlation:.2f}\nÉquation : note = {pente:.2f} * heures + {ordonnee:.2f}"
plt.text(df['heures_etudes'].min() + 0.5, 18, text_stats, fontsize=9.5, 
         bbox=dict(boxstyle="round,pad=0.3", fc="#ebf8ff", ec="#3182ce", lw=1))

plt.tight_layout()
plt.savefig("nuage_regression_tp.png", dpi=300)
print("✓ Le graphique 'nuage_regression_tp.png' a bien été enregistré dans votre dossier.")
plt.show()