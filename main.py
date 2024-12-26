import pandas as pd

# Lire le fichier CSV
df = pd.read_csv("actions.csv")

data_dict = df.to_dict(orient='records')
for action in data_dict:
    action["Calculated benefit"] = float(action["Calculated benefit"].replace(",", "."))

# Tri des actions par ordre décroissant de bénéfice
actions_sorted = sorted(data_dict, key=lambda x: x['Calculated benefit'])
print(actions_sorted)

