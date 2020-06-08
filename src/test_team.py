from team import *
from poke import *

data = pkl.load(open("data/dataset.pkl", "rb"))

ivy = ivy = Poke(data, 'Ivysaur')
mew = Poke(data, 'Mew')
rhydon = Poke(data, 'Rhydon')

test_team = Team([ivy, mew, rhydon])

def test_creation():
    assert len(test_team.pokes) == 3