# Construa um programa que leia três números inteiros e mostre qual deles é o segundo maior.

numero1, numero2, numero3 = map(int, input().split())

# 2. criar uma logica para ver quem é o segundo maior

meu_array = []
meu_array.append(numero1) # Adiciona o primeiro número ao array
meu_array.append(numero2)
meu_array.append(numero3)

print(meu_array)

meu_array.sort() # Ordena o array em ordem crescente

print(meu_array)

print("O segundo maior número é:", meu_array[1])