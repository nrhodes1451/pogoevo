from poke import *

class Team():
    def __init__(self, pokes):
        self.pokes = pokes
        self.lead = self.pokes[0]