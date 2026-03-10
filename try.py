try:
  nome = input("Digite seu nome: ")
  idade = int(input("Digite sua idade: "))
  print(f"Olá, {nome}! Você tem {idade} anos.")
except ValueError:
  print("Por favor, digite um número válido para a idade.")
  