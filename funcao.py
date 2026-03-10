def numeros_aleatorios():
  minha_lista = [10, 20, 30, 40, 50]
  for i in minha_lista:
    print(i)
    
def numeros_da_loteria():
  for i in range(1, 61):
    print(i)
    
def gerar_palavras():
  palavras = ["maçã", "banana", "laranja", "uva", "pera"]
  for palavra in palavras:
    print(palavra)
    
def process_data(data):
    processed_data = []
    for item in data:
        if isinstance(item, int) and item > 0:
            processed_data.append(item * 2)
        elif isinstance(item, str):
            processed_data.append(item.upper())
    return processed_data

data = [1, 'hello', -3, 'world', 5]
result = process_data(data)
print(result)
    
numeros_da_loteria()
gerar_palavras()   
numeros_aleatorios() 

#Vamos discutir o código passo-a-passo:

#process_data: Função que processa uma lista de dados, 
# duplicando números inteiros positivos e convertendo strings para maiúsculas.
#for item in data: Itera sobre cada item na lista de dados.
#if isinstance(item, int) and item > 0: Verifica se o item é um inteiro positivo antes de duplicá-lo.
#elif isinstance(item, str): Verifica se o item é uma string antes de convertê-lo para maiúsculas.
#print(result): Exibe a lista processada, mostrando o resultado das operações realizadas.           