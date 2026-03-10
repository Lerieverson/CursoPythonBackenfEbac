# Dado um endereço IP válido (IPv4), retorne a classe do endereço IP com base no seu primeiro octeto.
def classe_endereco_ip(endereco_ip):
    primeiro_octeto = int(endereco_ip.split('.')[0])

    if 0 <= primeiro_octeto <= 127:
        return "Classe A"
    elif 128 <= primeiro_octeto <= 191:
        return "Classe B"
    elif 192 <= primeiro_octeto <= 223:
        return "Classe C"
    elif 224 <= primeiro_octeto <= 239:
        return "Classe D"
    elif 240 <= primeiro_octeto <= 255:
        return "Classe E"
    else:
        return "Endereço IP inválido"
      
# Exemplo de uso
endereco_ip = input("Digite um endereço IP (IPv4): ")
print(classe_endereco_ip(endereco_ip))
# Exemplo de uso
endereco_ip = input()

novo_endereco_ip = ""
for i in endereco_ip:
    if i == '.':
        novo_endereco_ip += '[.]'
    else:
        novo_endereco_ip += i
print(novo_endereco_ip)
