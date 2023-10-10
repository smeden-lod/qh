from random import choice
from time import sleep
from Hero import Hero
from Mob import mob, ordre


class Jeu:
    
    def __init__(self):
        
        self.hero = Hero()  
        self.pvmax = self.hero.lvl * 5
        self.pv = self.pvmax
        self.lvl = self.hero.lvl
        self.xpe = self.hero.xpe
        self.slime = mob["slime"]
        self.spider = mob["spider"]
        self.squelette = mob["squelette"]
        self.monster = [self.slime, self.spider, self.squelette]
        
    def battle(self, mob, attaque):
        
            print(f"Tu es niveau {self.hero.lvl} et tu as {self.hero.pv} pv")
            print(f"Combat contre {mob.name} commence!")
            sleep(1)
            while self.pv > 0 and mob.pv > 0:
                print("Que voulez-vous faire?")
                sleep(2)
                print("1. Frappe avec ton épée")
                print("2. Frappe avec ta hache(plus puissante)")#si tu peut essayer de rajouter un cooldown pour cette attaque, genre on peut la faire tout les 2 tours
                print("3. Se soigner") #le soin marche pour le joueur mais pas pour les mobs car flemme d'avoir un mob qui se heal h24
                print("4. Quitter le combat")
                sleep(1)
                choix = input("Votre choix: ")

                if choix == "1":
                    self.hero.effectuer_attaque(mob, attaque)
                    if mob.pv > 0:
                        mob.attaquer(self.hero)
                        self.pv -= 1
                elif choix == "2":
                    self.hero.effectuer_attaque(mob, self.hero.attaque_speciale)
                    if mob.pv > 0:
                        mob.attaquer(self.hero)
                elif choix == "3":
                    self.hero.se_soigner(self.hero)
                    if mob.pv > 0:
                        mob.attaquer(self.hero)
                elif choix == "4":
                    print("Vous avez fui le combat.")
                    return
                    
                print(f"PV de {mob.name}: {mob.pv}/{mob.pvmax}")
                sleep(1)

            if self.pv > 0:
                exp_gain = mob.exp
                self.hero.gain_xp(exp_gain)
                print(f"Vous avez vaincu {mob.name} et gagné {exp_gain} XP.")
                mob.pv = mob.pvmax
            
            else:
                print(f"Vous avez été vaincu par {mob.name}.")
                mob.pv = mob.pvmax
            
            
    def run(self): 
        while self.hero.pv > 0:
            if self.hero.lvl <= len(mob):
                rencontre = choice(range(self.hero.lvl))
            else:
                rencontre = choice(range(len(mob)))
            enemy_name = ordre[rencontre]
            enemy = mob[enemy_name]
            print(f"Vous êtes tombé contre : {enemy_name}")
            self.battle(enemy, self.hero.attaque_de_base)

jeu = Jeu()
jeu.run()