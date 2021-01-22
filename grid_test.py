from poke import *
from team import *
from battle import *
import copy
import pickle as pkl

pokes = pkl.load(open("data/opt_stats_gl", "rb"))
del(pokes['Mew'])
pokelist = np.array([v for v in pokes.values()])

t1 = np.random.choice(pokelist, 3, False)
t2 = np.random.choice(pokelist, 3, False)

movesets = pkl.load(open("data/moveset_test_results.pkl", "rb"))
for k,v in pokes.items():
    moveset = {
        'fast': movesets.loc[movesets['poke'] == k]['fast_move'].values[0],
        'charge': movesets.loc[movesets['poke'] == k]['charge_move'].values[0]
    }
    v.moveset = v.get_moveset(moveset)


def random_team(pokelist):
    t = np.random.choice(pokelist, 3, False)
    t = Team(t.tolist())
    return t



def head_to_head():
    t1 = random_team(pokelist)
    t2 = random_team(pokelist)
    test_battle = Battle(t1, t2)
    test_battle.run_battle()
    return test_battle

