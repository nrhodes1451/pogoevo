from poke import *
import pickle as pkl
import math

data = pkl.load(open("data/dataset.pkl", "rb"))

ivy = Poke(data, 'Ivysaur')
mew = Poke(data, 'Mew')

def test_cp():
    assert ivy.cp == 1699
    assert mew.cp == 3265