import pandas as pd
import numpy as np
import random
import pickle as pkl
import math

class Move():
    def __init__(self, data, name):
        self.name = name
        if name in data.keys():
            data = data[name]
            self.type = data['Type']
            self.isFast = data['Category']
            self.dpse = data['DPS/E']
            self.epse = data['EPS/E']
            self.rate = data['Rate']
        else:
            self.type = None