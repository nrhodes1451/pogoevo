from poke import *
from battle import *
from team import *

data = pkl.load(open("data/dataset.pkl", "rb"))

test_team_1 = Team([
    Poke(data, 'Ivysaur'),
    Poke(data, 'Rhydon'),
    Poke(data, 'Blastoise')])
test_team_2 = Team([
    Poke(data, 'Skarmory'),
    Poke(data, 'Charmeleon'),
    Poke(data, 'Kadabra')])

test_battle = Battle(test_team_1, test_team_2)

def test_turn():
    test_battle.turn()
