from poke import poke
import pickle as pkl
import math

pokes = pkl.load(open("data/processed_pokes.pkl", "rb"))

ivy = Poke(pokes['Ivysaur'])
mew = Poke(pokes['Mew'])

def test_cp():
    assert ivy.cp == 1699
    assert mew.cp == 3265