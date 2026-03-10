def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido! Por favor, insira um número válido.")


def calculadora():
    while True:
        # Solicita os números
        num1 = obter_numero("Insira o primeiro número: ")
        num2 = obter_numero("Insira o segundo número: ")

        # Dicionário com operações usando lambda
        operacoes = {
            1: ("Soma", lambda a, b: a + b),
            2: ("Subtração", lambda a, b: a - b),
            3: ("Multiplicação", lambda a, b: a * b),
            4: ("Divisão", lambda a, b: a / b),
        }

        # Menu dinâmico usando list comprehension
        print("\nEscolha uma operação:")
        [print(f"{num} - {operacoes[num][0]}") for num in operacoes]

        try:
            escolha = int(input("Digite o número da operação desejada: "))
            if escolha not in operacoes:
                print("Operação inválida!")
                continue
        except ValueError:
            print("Entrada inválida! Digite um número correspondente à operação.")
            continue

        nome_operacao, funcao = operacoes[escolha]
        print(f"Você escolheu: {nome_operacao}")

        # Tratamento especial para divisão por zero
        if escolha == 4:
            while num2 == 0:
                print("Divisão por zero não é permitida.")
                num2 = obter_numero("Por favor, insira outro número: ")

        # Calcula o resultado
        resultado = funcao(num1, num2)
        print(f"O resultado é: {resultado}")

        # Pergunta se deseja continuar
        continuar = input("Deseja realizar outra operação? (S/N): ").strip().upper()
        if continuar != 'S':
            print("Encerrando a calculadora. Até logo!")
            break


# Executa o programa
calculadora()