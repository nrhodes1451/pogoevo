from poke import poke
import pickle as pkl
import math

pokes = pkl.load(open("../data/processed_pokes.pkl", "rb"))

ivy = poke(pokes['Ivysaur'])
mew = poke(pokes['Mew'])

def test_cp():
    assert ivy.cp == 1699
    assert mew.cp == 3265