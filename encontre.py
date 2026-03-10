# Dado um array de números inteiros, cada elemento aparece duas vezes,exceto um, Encontre ele.
# nums = [4,1,2,1,2] -> nesse caso o número que aparece uma única vez é o 4

meu_arrayzinho = [4,1,2,1,2]

# Criar um dicionário para fazer a contagem de cada número no array
meu_dicionariozinho = {}
for i in meu_arrayzinho:
    if i in meu_dicionariozinho:
        meu_dicionariozinho[i] += 1
    else:
        meu_dicionariozinho[i] = 1
# Fazer a verificação de qual número aparece apenas uma vez
for chave, valor in meu_dicionariozinho.items():
    if valor == 1:
        print(chave)
        