import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


mdp=""
for i in range(0,nr_letters):
  mdp+=random.choice(letters)
  
for i in range(0,nr_symbols):
  mdp+=random.choice(symbols)
  
for i in range(0,nr_numbers):
  mdp+=random.choice(numbers)
  
print(mdp)
mdplist=[]
for i in range(0,nr_letters):
  mdplist+=random.choice(letters)

for i in range(0,nr_symbols):
  mdplist+=random.choice(symbols)

for i in range(0,nr_numbers):
  mdplist+=random.choice(numbers)

mdprandom=random.shuffle(mdplist)
print(mdplist)
newmdp=""
for i in mdplist:
  newmdp+=i
print(newmdp)
