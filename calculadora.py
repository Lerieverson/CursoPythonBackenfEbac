print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite o número da operação desejada: ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))



if opcao == "1":
    print("Resultado:", num1 + num2)
elif opcao == "2":
    print("Resultado:", num1 - num2)
elif opcao == "3":
    print("Resultado:", num1 * num2)
elif opcao == "4":
  if num2 == 0:
    print("Erro: divisão por zero não é permitida!")
  else:
    print("Resultado:", num1 / num2)
else:
    print("Opção inválida")
    
pergunta = input("Você gostaria de realizar outra operação? (s/n): ")
if pergunta == 's':
    # Aqui você poderia chamar novamente a função ou reiniciar o processo
    print("Reinicie o programa para realizar outra operação.")
    
else: 
    print("Obrigado por usar a calculadora!")
    