import pandas as pd
import itertools


# Define a class action
class Action:
    def __init__(self, nom, prix, benefit_2y):
        self.nom = nom
        self.prix = prix
        self.benefit_2y = benefit_2y

    def __str__(self):
        return f"Action('{self.nom}', {self.prix}, {self.benefit_2y})"


# Read CSV file and put content into action object
def read_csv_file():
    actions = []
    df = pd.read_csv("actions.csv", index_col=False)
    df["Calculated benefit"] = (
        df["Calculated benefit"].str.replace(",", ".").astype(float).astype(int)
    )

    for index, row in df.iterrows():
        action = Action(
            nom=row["Actions"], prix=row["Cost"], benefit_2y=row["Calculated benefit"]
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
"""


def bruteforce_simple(actions, budget_max):
    best_combo = None
    max_gains = 0

    for r in range(len(actions) + 1):
        for combo in itertools.combinations(actions, r):
            cout = sum(action.prix for action in combo)
            gains = sum(action.benefit_2y for action in combo)

            if cout <= budget_max and gains > max_gains:
                best_combo = combo
                max_gains = gains

    return best_combo


# Define maximal budget
budget_max = 250

# Read the file content to get action
actions = read_csv_file()

# Get the best combo after passing actions to brute_force
best_combo = bruteforce_simple(actions, budget_max)

# Display the best combi
if best_combo:
    print("Meilleure combinaison :")
    for action in best_combo:
        print(f"{action.nom}: Prix={action.prix}," f" Bénéfice={action.benefit_2y}")
else:
    print("Aucune combinaison valide trouvée.")
