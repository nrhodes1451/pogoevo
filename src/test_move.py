import pytest
from move import *

move_data = pkl.load(open("data/moves.pkl", "rb"))

def test_null_move():
    null_move = Move(move_data, "nope")
    assert null_move.type is None


def test_dpse():
    vwhip = Move(move_data, "Vine Whip")
    assert vwhip.dpse == 8.3