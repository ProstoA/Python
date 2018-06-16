class animals:
  food='plant'
  growth=True
  reproduction=True
  noise="wow"
  def wow(self):
    print(self.noise)

class artiodactyls(animals):
  hoof=True

class birds(animals):
  wing=True

class cows(artiodactyls):
  give_milk=True

class goats(artiodactyls):
  give_milk=True

class sheep(artiodactyls):
  give_meat=True

class pigs(artiodactyls):
  give_meat=True

class Ducks(birds):
  give_meat=True
  noise="crya-crya"

class chickens(birds):
  give_meat=True

class geese(birds):
  give_meat=True
  def wow(self):
    print("GA-GA")

g1=Ducks()
g1.wow()
a1=animals()
a1.wow()

#print(geese.__dict__)
#print(animals.__dict__)
