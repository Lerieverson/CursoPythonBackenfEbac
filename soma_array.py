# Dada um array de número inteiros, retorne a soma do menor número e do maior número do array.

meu_arrayzinho = [3, 5, 1, 9, 7, 88, -2, 6, 99, 75, 23]
# 1. Se eu ordenar o array, o menor número será o primeiro e o maior será o último.
print(meu_arrayzinho)

meu_arrayzinho.sort()

print(meu_arrayzinho)

# 2. Efetuar a soma do menor com o maior número do array.
primeiro_valor = meu_arrayzinho[0]
ultimo_valor = meu_arrayzinho[-1]
soma = primeiro_valor + ultimo_valor
print(soma)