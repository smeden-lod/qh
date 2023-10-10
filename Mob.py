from Attaque import attaque_de_base, attaque_frappe

"""
Tout les monstres sont stocker ici.
Avec leurs noms, pv, experiences et leur attaque venant du Attaque.py  
"""

class Mob:
    
    def __init__(self, name, pv, exp, attaque):
        self.name = name
        self.pv = pv
        self.exp = exp
        self.attaque = attaque
        self.pvmax = self.pv
        self.attaque_de_base = attaque_de_base

    def attaquer(self, other):
        other.pv -= self.attaque.degats
        print(f"{self.name} t'attaque, il te reste {other.pv} pv")

mob = {
    "slime": Mob("Slime", 3, 50, attaque_de_base),
    "spider": Mob("Spider", 3, 75, attaque_de_base),
    "squelette": Mob("Squelette", 5, 100, attaque_frappe)
}

ordre = ["slime", "spider", "squelette"]