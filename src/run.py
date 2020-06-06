import pandas as pd
import numpy as np
from poke import *
from move import *

move_data = pkl.load(open("../data/moves.pkl", "rb"))
type_data = pkl.load(open("../data/types.pkl", "rb"))