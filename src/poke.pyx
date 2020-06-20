import numpy as np
import pandas as pd
import random
import pickle as pkl
import math

class Poke():
    def __init__(object self,
                 dict data,
                 str species,
                 list ivs = [15, 15, 15],
                 int level = 40,
                 dict moveset = None,
                 int shields = 0):
        self.data = data
        self.species = data['pokes'][species]
        self.name = species
        self.type = self.get_type()
        self.ivs = ivs
        self.level = level
        self.moveset = self.get_moveset(moveset)
        self.cp_mult = data['cp'][self.level]
        self.shields = shields
        self.calculate_stats()
        self.fainted = False
        self.energy = 0
        self.cooldown = 0
        self.active_attack = None
        self.is_shadow = False
        self.is_active = False
        self.damage_dealt = 0
        self.turns_taken = 0


    def calculate_stats(object self):
        self.stats = {
            'atk': self.species['atk']+self.ivs[0],
            'def': self.species['def']+self.ivs[1],
            'sta': self.species['sta']+self.ivs[2]
        }
        self.cp = max(10, math.floor((self.stats['atk'] * 
                 self.stats['def']**0.5 *
                 self.stats['sta']**0.5 *
                 self.cp_mult**2)/10))
        self.stats = {
            k:v * self.cp_mult for k,v in self.stats.items()
        }
        self.hp = int(self.stats['sta'])


    def calculate_cp(object self):
        return max(10, math.floor((self.stats['atk'] * 
                 self.stats['def']**0.5 *
                 self.stats['sta']**0.5 *
                 self.cp_mult**2)/10))


    def get_moveset(object self, dict moveset):
        cdef str fname = ''
        cdef str cname = ''
        if moveset is None:
            fast = self.species['field_primary_moves'].split(", ")
            charge = self.species['field_secondary_moves'].split(", ")
            
            fname = random.choice(fast)
            cname = random.choice(charge)
        else:
            fname = moveset['fast']
            cname = moveset['charge']
        
        fast = self.data['moves'][fname]
        charge = self.data['moves'][cname]

        fast['NAME'] = fname
        charge['NAME'] = cname

        return {
            'fast': fast,
            'charge': charge
        }


    def get_type(object self):
        cdef list types = [t[:3] for t in self.species['field_pokemon_type'].split(", ")]
        return types

    
    def attack(object self, object opponent):
        self.turns_taken += 1
        if self.cooldown <= 0 and self.active_attack is None:
            if self.charged():
                # Charge attack
                self.active_attack = self.moveset['charge']
                self.energy -= self.active_attack['ENG'] 
                self.cooldown = 1
                return
            else:
                # Fast attack
                self.active_attack = self.moveset['fast']
                self.energy += self.active_attack['ENG']
                self.energy = min(100, self.energy)
                self.cooldown = self.active_attack['TURNS']

        self.cooldown = self.cooldown - 1
        
        # Attack opponent
        if self.cooldown <=0 and self.active_attack is not None:
            damage = self.get_damage(self.active_attack, opponent)
            opponent.hp -= damage
            self.damage_dealt += damage
            if opponent.hp <= 0:
                opponent.fainted = True
            if self.active_attack['CAT'] == 'charge':
                self.cooldown = 1
            self.active_attack = None


    def charged(object self):
        return self.energy >= self.moveset['charge']['ENG']


    def get_damage(object self, dict move, object opponent):
        cdef int power = move['PWR']
        cdef int attack = self.stats['atk']
        cdef int defense = opponent.stats['def']
        cdef float stab = 1 + 0.2 * (move['TYPE'] in self.type)
        cdef float ptype = np.prod([
            self.data['types'][move['TYPE']][t] 
            for t in opponent.type])
        cdef float trainer = 1.3
        cdef int charge = 1

        cdef float modifier = (ptype * 
                    stab *
                    trainer * 
                    charge)
        
        cdef float damage = int(0.5 *
                  power * 
                  attack * 
                  modifier /
                  defense) + 1
        return damage


    def simulate(self, opponent, turns = 24):
        mfast = self.moveset['fast']
        mcharge = self.moveset['charge']
        iters = turns / mfast['TURNS']
        damage = iters * self.get_damage(mfast, opponent)
        energy = iters * mfast['ENG']
        damage += mcharge['PWR'] * (energy // mcharge['ENG'])
        return damage


    def compare(self, opponent, turns = 24):
        return ((self.simulate(opponent, turns) * self.hp) /
                (opponent.simulate(self, turns) * opponent.hp))