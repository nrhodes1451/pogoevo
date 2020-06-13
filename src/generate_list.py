from poke import *
from team import *
from battle import *
import copy

data = pkl.load(open("../data/dataset.pkl", "rb"))

def optimise_stats(species, cp=1500):
    p = Poke(data, species)
    if p.cp < 1400:
        return None
    elif p.cp < 1500:
        return p
    else:
        level = 40
        while p.cp > 1500:
            level -= 1
            p = Poke(data, species, level=level)
        level = level + 1
        atk = 15
        defn = 15
        sta = 15
        p = Poke(data, species, level = level)
        while p.cp > 1500:
            stats = p.stats.copy()
            if sta == 0:
                stats['sta'] = 0
            if defn == 0:
                stats['def'] = 0
            if atk == 0:
                stats['atk'] = 0
            if (stats['def'] > stats['atk'] 
                and stats['def'] > stats['sta']):
                defn -= 1
            elif (stats['sta'] > stats['atk'] 
                and stats['sta'] > stats['def']):
                sta -= 1
            else:
                atk -= 1
            p = Poke(data, species, level = level, ivs = [atk, defn, sta])
    return p

great_league = {
    p:optimise_stats(p) for p in data['pokes'].keys()
}

test_battle = Battle(
    Team([
        great_league['Blissey']
    ]),
    Team([
        great_league['Mewtwo']
    ])
)
test_battle.run_battle()

print(p1.hp)
print(p2.hp)
test_battle.generate_report()