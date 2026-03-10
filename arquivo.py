def obter_numero(mensagem):

    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido. Insira um número válido.")


def calculadora():

    while True:

        num1 = obter_numero("Insira o primeiro número: ")
        num2 = obter_numero("Insira o segundo número: ")

        operacoes = {
            1: ("Soma", lambda a, b: a + b),
            2: ("Subtração", lambda a, b: a - b),
            3: ("Multiplicação", lambda a, b: a * b),
            4: ("Divisão", lambda a, b: a / b),
        }

        print("\nEscolha uma operação:")
        for num in operacoes:
            print(f"{num} - {operacoes[num][0]}")

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

        if escolha == 4:
            while num2 == 0:
                print("Divisão por zero não é permitida.")
                num2 = obter_numero("Insira outro número: ")

        resultado = funcao(num1, num2)

        print(f"O resultado é: {resultado}")

        continuar = input("Deseja realizar outra operação? (S/N): ").strip().upper()

        if continuar != 'S':
            print("Encerrando a calculadora. Até logo!")
            break


# Executa a calculadora
calculadora()