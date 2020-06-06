from team import *
from poke import *

pokes = pkl.load(open("../data/processed_pokes.pkl", "rb"))

ivy = ivy = Poke(pokes['Ivysaur'])
mew = Poke(pokes['Mew'])
rhydon = Poke(pokes['Rhydon'])

test_team = Team([ivy, mew, rhydon])

def test_creation():
    assert len(test_team.pokes)==3