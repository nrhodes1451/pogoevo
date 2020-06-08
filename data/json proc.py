import pandas as pd
import json
import pickle as pkl

def process_json():
    with open("../data/pokemon-data-full-en-PoGO.json") as json_file:
        data = json.load(json_file)

    def process_poke(p):
        int_fields = ['sta',
                        'atk',
                        'def',
                        'cp']
        for f in int_fields:
            p[f] = int(p[f])
        return p
    
    pokes = {p['title_1']:process_poke(p) for p in data} 
    pkl.dump(pokes, open("../data/data_full.pkl", "wb"))

    # Filter for CP >=1400
    pokes = {p:k for p,k in pokes.items() if k['cp']>=1400}
    pkl.dump(pokes, open("../data/processed_pokes.pkl", "wb"))