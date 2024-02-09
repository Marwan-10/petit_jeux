import random

def choix_carte():
  cartes=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  carte=random.choice(cartes)
  return carte
  
def total(cartes):
  if sum(cartes)==21 and len(cartes)==2:
    return 0
  if 11 in cartes and sum(cartes)>21:
    cartes.remove(11)
    cartes.append(1)
  return sum(cartes)

def comparaison(totj,totpc):
  if totj>21 and totpc>21:
    return "Perdu"
  if totj==totpc:
    return "Match Null"
  elif totpc==0:
    return "Perdu, pc a un Blackjack"
  elif totj==0:
    return "Victoire, t'as un Blackjack"
  elif totj>21:
    return "Perdu, t'as passé le 21"
  elif totpc>21:
    return "Victoire, le pc a passé le 21"
  elif totj>totpc:
    return "Victoire"
  else:
    return "Perdu"
    
def jouer():
  
  
  joueur=[]
  pc=[]
  fin=False
  
  for _ in range(2):
    joueur.append(choix_carte())
    pc.append(choix_carte())
   
  
  while not fin:
    total_joueur=total(joueur)
    total_pc=total(pc)
    print(f" vos cartes: {joueur}, total: {total_joueur}")
    print(f" 1 carte du pc: {pc[0]}")
    
    if total_joueur==0 or total_pc==0 or total_joueur>21:
      fin=True
    else:
      prendre=input("Tapez 'oui' pour obtenir une autre carte, tapez 'non' pour passer: ")
      if prendre=="oui":
        joueur.append(choix_carte())
      else:
        fin=True
    
  while total_pc !=0 and total_pc <17:
    pc.append(choix_carte())
    total_pc=total(pc)
  
  print(f" Votre main finale: {joueur}, Totale finale: {total_joueur}")
  print(f" Main finale du pc: {pc}, Totale finale: {total_pc}")
  print(comparaison(total_joueur,total_pc))

while input("si vous voulez jouer a Blackjack tapez 'oui' sinon tapez 'non' ")=="oui":
  jouer()
