import utils as ut    



print(f"  Moyenne    : {ut.notes_t.mean():.4f}")
print(f"  Médiane    : {ut.notes_t.median():.4f}")
print(f"  Écart-type : {ut.notes_t.std():.4f}")
print(f"  Q1 (25%)   : {ut.notes_t.quantile(0.25):.4f}")
print(f"  Q2 (50%)   : {ut.notes_t.quantile(0.50):.4f}")
print(f"  Q3 (75%)   : {ut.notes_t.quantile(0.75):.4f}")
