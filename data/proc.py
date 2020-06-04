import pandas as pd
import pickle as pkl

fp = "../database.xlsx"

types = pd.read_excel(fp, "Types")

cp = pd.read_excel(fp, "CP Mult").to_dict("records")
cp = {r['Level']:r['CP multiplier'] for r in cp}
pkl.dump(cp, open("../data/cpmults.pkl", "wb"))

base_stats = pd.read_excel(fp, "Base Stats")
base_stats = base_stats.set_index("Name").to_dict("index")

moves = pd.read_excel(fp, "Moves")
# Excluding weather ball as it's not a good enough move to warrant
# special consideration
moves = moves[moves.Move != "Weather Ball"]
moves = moves.set_index("Move").to_dict("index")
pkl.dump(moves, open("../data/moves.pkl", "wb"))

learned_moves = pd.read_excel(fp, "learned moves")
learned_moves = {k:learned_moves.move[learned_moves.name == k].tolist()
    for k in learned_moves.name.unique()}
pkl.dump(learned_moves, open("../data/learnedmoves.pkl", "wb"))

db = pd.read_excel(fp, "Database")
db = db.drop(columns=['CP', 'Product (k)', 'P/CP'])
db = db.set_index("Name").to_dict("index")
pkl.dump(db, open("../data/pogostats.pkl", "wb"))