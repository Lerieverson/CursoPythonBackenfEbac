def main():
    nome = "Leri"
    idade = 50
    print(f"Meu nome é {nome} e eu tenho {idade} anos.")
main()

def operadores():
    a = 10
    b = 5
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b
    divisao_inteira = a // b
    potencializacao = a ** b
    print(f"Soma: {soma}, Subtração: {subtracao}, Multiplicação: {multiplicacao}, Divisão: {divisao}, Divisão Inteira: {divisao_inteira}, Potencialização: {potencializacao}")
operadores()

def calcular_area_retangulo(largura, altura):
  return largura * altura

largura = 5
altura = 10
area = calcular_area_retangulo(largura, altura)
print(f"A área do retângulo é: {area}")
