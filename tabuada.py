# tabuada receba um número e exiba a tabuada de multiplicação desse número de 1 a 10
numero = int(input("Digite um número para ver a tabuada: "))
print(f"Tabuada de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


numero_qualquer = int(input())
soma = 2
for i in range(1, numero_qualquer +1):
    soma += 1
print(soma)