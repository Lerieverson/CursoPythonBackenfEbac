meu_array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5]
meu_dicionario = {}
for i in meu_array:
  if i not in meu_dicionario:
    meu_dicionario[i] = 1
  else:
    meu_dicionario[i] += 1

soma_das_chaves = 0
for chave, valor in meu_dicionario.items():
  if valor == 1:
    soma_das_chaves += chave
print(soma_das_chaves)


meu_array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5]
meu_dicionario = {}
for i in meu_array:
  if i not in meu_dicionario:
    meu_dicionario[i] = 1
  else:
    meu_dicionario[i] += 1

soma_das_chaves = 0
for chave, valor in meu_dicionario.items():
  if valor == 1:
   print(chave)