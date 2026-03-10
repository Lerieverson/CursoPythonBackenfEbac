class animal:
  def __init__(self, nome):
    self.nome = nome
  def comer(self):
    print(f"{self.nome} está comendo.")
    
class cachorro(animal):
  def latir(self):
    print(f"{self.nome} está latindo: Au au!")
    
class gato(animal):
  def miar(self):
    print(f"{self.nome} está miando: Miau miau!")
    
class passarinho(animal):
  def cantar(self):
    print(f"{self.nome} está cantando: Piu piu!")
    
meu_cachorrinho = cachorro("Rex")
meu_cachorrinho.comer()
meu_cachorrinho.latir()
print("\n")
meu_gatinho = gato("Mimi")
meu_gatinho.comer()
meu_gatinho.miar()
print("\n")
meu_passarinho = passarinho("Piu")
meu_passarinho.cantar()
meu_passarinho.comer()
