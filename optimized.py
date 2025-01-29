import pandas as pd
import itertools
import time

start_section = time.time()
# Define a class action
class Action:
    def __init__(self, name, price, benefit_2y):
        self.name = name
        self.price = price
        self.benefit_2y = benefit_2y

    def __str__(self):
        return f"Action('{self.name}', {self.price}, {self.benefit_2y})"


def clean_data(df):
    df= df[df["Calculated benefit"] >= 5]
    print(df)
    return df


# Read CSV file and put content into action object
#O(n)
def read_csv_file():
    actions = []
    df = pd.read_csv("actions.csv", index_col=False)
    df["Calculated benefit"] = (
        df["Calculated benefit"].str.replace(",", ".").astype(float).astype(int)
    )
    data = clean_data(df)
    for row in data.to_dict('records'):
        action = Action(
            name=row["Actions"], price=row["Cost"], benefit_2y=row["Calculated benefit"]
        )
        actions.append(action)
    return actions



"""
Function to get the best combi
Goal of itertools.combinations:
Go though each combinations following r value
Get the cost and gains
check the constraints 
Add to best_combo , same for gains
Same will be done , until we get more good combi

Utiliser une méthode différente de itertools et un autre type
d'algo
Big o annotation
reduire le volume de données qui n'apporte pas grand chose
est ce que le resultat est unique
n complexité de l'algo... à comprendre
lignes de code qui sont les plus couteuse  en terme de complexité
faire une diapo

O(2n)= ligne couteuse

def bruteforce_optimise(actions, budget_max):
    best_combo = None
    max_gains = 0

    # Trier les actions par ratio bénéfice/coût pour optimiser
    actions = sorted(actions, key=lambda x: x.benefit_2y / x.price, reverse=True)

    for r in range(len(actions) + 1):
        for combo in itertools.combinations(actions, r):
            # Vérifier le coût d'abord pour éviter des calculs inutiles
            cout = sum(action.price for action in combo)
            if cout > budget_max:
                continue  # Passe directement à la combinaison suivante

            gains = sum(action.benefit_2y for action in combo)
            if gains > max_gains:
                best_combo = combo
                max_gains = gains
    return best_combo
"""


def bruteforce_binary(actions, budget_max):
    n = len(actions)
    best_combo = None
    max_gains = 0

    # Utilise les nombres binaires pour représenter les combinaisons
    for i in range(2 ** n):
        combo = []
        cout = 0
        gains = 0

        # Vérifie chaque bit
        for j in range(n):
            if i & (1 << j):  # Si le bit j est 1
                action = actions[j]
                cout += action.price
                gains += action.benefit_2y
                combo.append(action)

        if cout <= budget_max and gains > max_gains:
            max_gains = gains
            best_combo = combo

    return best_combo


# Define maximal budget
budget_max = 250

# Read the file content to get action
actions = read_csv_file()

# Get the best combo after passing actions to brute_force
best_combo = bruteforce_binary(actions, budget_max)

# Display the best combi
if best_combo:
    print("Meilleure combinaison :")
    for action in best_combo:
        print(f"{action.name}: Prix={action.price}," f" Bénéfice={action.benefit_2y}")
else:
    print("Aucune combinaison valide trouvée.")

end_section = time.time()
section_time = end_section - start_section
print(f"Temps pour cette section : {section_time} secondes.")