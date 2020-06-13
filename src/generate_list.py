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
            if (p.stats['def'] > p.stats['atk'] 
                and p.stats['def'] > p.stats['sta']):
                defn -= 1
            elif (p.stats['sta'] > p.stats['atk'] 
                and p.stats['sta'] > p.stats['def']):
                sta -= 1
            else:
                atk -= 1
            p = Poke(data, species, level = level, ivs = [atk, defn, sta])


# Winner
p1 = Poke(data, 'Blissey', 
    level = 19,
    ivs = [15,15,15],
    moveset = {
        'fast': 'Pound',
        'charge': 'Psychic'
    }
)
p1.cp
p1.energy = -10000

p2 = Poke(data, 'Blissey',
    level = 20,
    ivs = [15,0,8],
    moveset = {
        'fast': 'Pound',
        'charge': 'Psychic'
    }
)
p2.cp
p2.energy = -10000

test_battle = Battle(Team([p1]), Team([p2]))
test_battle.run_battle()
print(p1.hp)
print(p2.hp)
test_battle.generate_report()