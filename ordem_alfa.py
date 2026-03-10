# Receba uma lista de palavras e ordene-as em ordem alfabeticas
# Solicite ao usuário que insira as palavras separadas por vírgulas
palavras_input = input("Digite uma lista de palavras separadas por vírgulas: ")
# Divida a string de entrada em uma lista de palavras
palavras = [palavra.strip() for palavra in palavras_input.split(",")]
# Ordene a lista de palavras em ordem alfabética
palavras_ordenadas = sorted(palavras)
# Exiba a lista ordenada
print("Palavras em ordem alfabética:")
for palavra in palavras_ordenadas:
    print(palavra)
    
meu_array = []

for i in range(1, 6):
  palavra = input()
  print("Palavras sendo adicionadas:")
  meu_array.append(palavra)

meu_array.sort()# Ordena o array em ordem crescente
print( meu_array)