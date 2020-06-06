from poke import *
from battle import *
from team import *

pokes = pkl.load(open("../data/processed_pokes.pkl", "rb"))

ivy = ivy = Poke(pokes['Ivysaur'])
mew = Poke(pokes['Mew'])
rhydon = Poke(pokes['Rhydon'])

test_team_1 = Team([Poke(pokes['Ivysaur']),
                    Poke(pokes['Mew']),
                    Poke(pokes['Rhydon'])])
test_team_2 = Team([Poke(pokes['Blastoise']),
                    Poke(pokes['Wartortle']),
                    Poke(pokes['Charizard'])])

test_battle = Battle(test_team_1, test_team_2)