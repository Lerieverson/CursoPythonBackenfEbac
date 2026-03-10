class Animal:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    
  def emitir_som(self):
    print("O animal emitiu um som genérico.")
  
class Cachorro(Animal):
  def emitir_som(self):
    return "O cachorro latiu!"

class Gato(Animal):
  def emitir_som(self):
    return "O gato miou!"
  
cachorro = Cachorro("Lece", 3)
gato = Gato("Belo", 2)

print(f"{cachorro.nome} tem {cachorro.idade} anos e ao ouvir um barulho, {cachorro.emitir_som()}")
print(f"{gato.nome} tem {gato.idade} anos e ao pisar em seu rabo , {gato.emitir_som()}")
print("==================================================================")

meu_arrayzinho = [elemento for elemento in range(1, 11)]
print(meu_arrayzinho)
print("==================================================================")

palavras = ["Python", "Java", "C++", "JavaScript", "Ruby"]
palavras_maiusculas = [palavra.upper() for palavra in palavras]
print(palavras_maiusculas)
print("==================================================================")

palavras_maiusculas = [palavra[0] for palavra in palavras]
print(palavras_maiusculas)
print("==================================================================")

numeros = [1, 2, 3, 4, 5]
quadrados = [numero ** 2 for numero in numeros]
print(quadrados)
print("==================================================================")

quadrados_impares = [elemento**2 for elemento in range(1, 11) if elemento % 2 != 0]
print(quadrados_impares)