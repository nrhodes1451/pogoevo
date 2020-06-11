import pandas as pd
import numpy as np
import random
import pickle as pkl
import math

class Poke():
    def __init__(self,
                 data,
                 species,
                 ivs = [15, 15, 15],
                 level = 40,
                 moveset = None):
        self.data = data
        self.cp_mults = data['cp']
        self.species = data['pokes'][species]
        self.type = self.get_type()
        self.ivs = ivs
        self.level = level
        self.moveset = self.get_moveset(moveset)
        self.stats = self.calculate_stats()
        self.cp = self.calculate_cp()
        self.hp = self.stats['sta']
        self.fainted = False
        self.energy = 0
        self.cooldown = 0
        self.active_attack = None
        self.is_shadow = False


    def calculate_stats(self):
        stats = {
            'atk': self.species['atk']+self.ivs[0],
            'def': self.species['def']+self.ivs[1],
            'sta': self.species['sta']+self.ivs[2]
        }
        return stats


    def calculate_cp(self):
        return max(10, math.floor((self.stats['atk'] * 
                 self.stats['def']**0.5 *
                 self.stats['sta']**0.5 *
                 self.cp_mults[self.level]**2)/10))


    def get_moveset(self, moveset):
        if moveset is None:
            fast = self.species['field_primary_moves'].split(", ")
            charge = self.species['field_secondary_moves'].split(", ")
            
            fname = random.choice(fast)
            cname = random.choice(charge)
            
            fast = self.data['moves'][fname]
            charge = self.data['moves'][cname]

            fast['NAME'] = fname
            charge['NAME'] = cname

            return {
                'fast': fast,
                'charge': charge
            }
        else:
            return moveset


    def get_type(self):
        types = self.species['field_pokemon_type']
        types = [t[:3] for t in types.split(", ")]
        return types

    
    def attack(self, opponent):
        if self.active_attack is None:
            if self.charged():
                self.active_attack = self.moveset['charge']
                self.cooldown = self.active_attack['TURNS']
                return
            else:
                self.active_attack = self.moveset['fast']
                self.cooldown = self.active_attack['TURNS']

        self.cooldown = self.cooldown - 1
        
        # Attack opponent
        if self.cooldown <=0 and self.active_attack is not None:
            self.damage(self.active_attack, opponent)
            self.active_attack = None


    def charged(self):
        return self.energy >= self.moveset['charge']['ENG']


    def damage(self, move, opponent):
        power = move['PWR']
        attack = self.stats['atk']
        defense = opponent.stats['def']
        stab = 1 + 0.2*(move['TYPE'] in self.type)
        ptype = np.prod([
            self.data['types'][move['TYPE']][t] 
            for t in opponent.type])
        trainer = 1.3
        charge = 1

        modifier = (ptype * 
                    stab *
                    trainer * 
                    charge)
        
        damage = int(0.5 *
                  power * 
                  attack * 
                  modifier /
                  defense) + 1

        opponent.hp += -damage