from replit import clear
from art import logo
print(logo)

dico={}
def ajouterBid():
  name=input("name ")
  bid=input("prize ")
  dico[name]=bid

def maxbid(dico):
  max=0
  person=""
  for maxbid in dico:
    m=int(dico[maxbid])
    if m>max:
      person=maxbid
      max=m

  print(f"max bid is {max} from {person}")
  
ajouterBid()
question=input("another bid? yes or no ")
while question != "no":
  clear()
  ajouterBid()
  question=input("another bid? yes or no ")

maxbid(dico)
