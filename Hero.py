"""
La class Hero est la plus importante,
elle permet de définir tout le personnage utiliser durant toute l'aventure
"""

from Attaque import attaque_de_base, attaque_frappe


class Hero:
    
    def __init__(self):
        self.pv = 5
        self.pvmax = self.pv #j'ai rajouter les pvmax dans le Hero pour le heal
        self.atk = 2
        self.xp = 0
        self.lvl = 1
        self.xpe = 50
        self.attaque_de_base = attaque_de_base
        self.attaque_speciale = attaque_frappe
        
    def effectuer_attaque(self, mob, attaque):
        degats = attaque.degats
        mob.pv -= degats
        print(f"Vous avez utilisé {attaque.nom} et infligé {degats} dégât à {mob.name}.")
    
    def se_soigner(self, attaque): #tu peut quand même overheal genre si tu est a 4/5 pv tu gagne 3 pv et pas 1
        if self.pv < self.pvmax:
            self.pv += 4 # monte de 3 pv vu que le slime m'attaque juste après
        else:
            print("tu ne peut pas te heal")
        
    def gain_xp(self, amount):
        self.xp += amount
        while self.xp >= self.xpe:
            self.level_up()

    def level_up(self):
        self.lvl += 1
        self.xp = 0
        self.xpe = int(self.xpe * 1.5)
        self.pv = self.lvl * 5
        print(f"Vous avez atteint le niveau {self.lvl} ! Vos PV ont été augmentés à {self.pv}.")