# Dsado array de número inteiros, retorne quantos deles são pares.
# nums = ["12", "345", "2", "6", "7896"] -> esses valores estão como números inteiros
# novo_array = [12, 345, 2, 6, 7896] -> esses valores estarão como strings

# Criar um novo array de strings que vai ter os mesmos valores do primeiro array,porém como strings.

novo_array = ["12", "345", "2", "6", "7896"]

# fazer um looping dentro do novo_array para fazer a verificação de números com digitos pares
contador = 0
for i in novo_array:
  if len(i) % 2 == 0:
    contador += 1
    

# fazer a contagem e mostrar (printar) na tela o resultado
print(contador)