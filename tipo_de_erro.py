#erro:                                          Correção:
# #sempre inclua "self" como primeiro parâmetro do método
# __init__ e de outros métodos da classe.
#class Pokemon:                                  class Pokemon:
  #def __init__(name, type):                        def __init__(self, name, type):
    #self.name = name                                 self.name = name
   # self.type = type                                 self.type = type
    
#pikachu = Pokemon("Pikachu", "Elétrico")        pikachu = Pokemon("Pikachu", "Elétrico")
#print(pikachu.name)                             print(pikachu.name)