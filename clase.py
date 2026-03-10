# Ela é um molde que usarei para criar pokemons diferentes.
# Posso ter tipos de pokemons diferentes;
# Poderes diferentes;
# Atributos diferentes;
# Tipos diferentes;
# Forças diferentes;
# Moldes diferentes para cada tipo de pokemon.

# Uma classe é um molde;
# Vamos usar esse molde em coisas que tenham o mesmo padrão.

# -> Nome --> Pikachu
# -> HP --> 100;
# -> Tipo --> Elétrico
# -> Ataque --> Choque eletrico;
# -> Altura --> 0,4m;
# -> Peso --> 6kg;

class MoldePokemon:
  def __init__(self, nome, hp, tipo, ataque, defesa, altura, peso):
    self.nome = nome
    self.hp = hp
    self.tipo = tipo
    self.ataque = ataque
    self.defesa = defesa
    self.altura = altura
    self.peso = peso
    
  def mostrar_nome_pokemon(self):
    print(f"O nome do pokemon é {self.nome}")
  def mostrar_hp_pokemon(self):
    print(f"O HP do pokemon é {self.hp}")
  def mostrar_defesa_pokemon(self):
    print(f"A defesa do pokemon é {self.defesa}") 
  def mostrar_ataque_pokemon(self):
    print(f"O ataque do pokemon é {self.ataque}")
  def mostrar_tipo_pokemon(self):
    print(f"O tipo do pokemon é {self.tipo}")
  def mostrar_altura_pokemon(self):
    print(f"A altura do pokemon é {self.altura}")
  def mostrar_peso_pokemon(self):
    print(f"O peso do pokemon é {self.peso}")
    
pikachu = MoldePokemon("Pikachu", 100, "Elétrico", "Choque elétrico", 50, 0.4, 6)
charizard = MoldePokemon("Charizard", 200, "Fogo/Voador", "Lança-chamas", 80, 1.7, 90)
baubasaur = MoldePokemon("Bulbasaur", 120, "Planta/Veneno", "Chicote de cipó", 60, 0.7, 6.9)  
  
pikachu.mostrar_nome_pokemon()
charizard.mostrar_nome_pokemon()
baubasaur.mostrar_nome_pokemon()
  