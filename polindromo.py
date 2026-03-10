# Receba um número e determine se ele é um polindromo (lê-se igual de frente para trás).

# 1. Receber o número do usuário
meu_numero = int(input())
  
# 2. Converter o número para string para facilitar a verificação
numero_str = str(meu_numero)

if numero_str == numero_str[::-1]:  # Verifica se a string é igual à sua inversa
    print(f"O número {meu_numero} é um palíndromo.")  
else:
    print(f"O número {meu_numero} não é um palíndromo.")
    
texto = "python"
print(texto[1:5:2])  # saída: ytho
