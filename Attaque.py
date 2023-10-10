"""
Toutes les attaques sont stockées ici Joueur et Mobs compris.
Les attaques ont un nom et des dégâts définis
"""


class Attaque:
    def __init__(self, nom, degats):
        self.nom = nom
        self.degats = degats

attaque_de_base = Attaque("Coup d'épée testé", 1)
attaque_frappe = Attaque("Coup de hache", 5)
