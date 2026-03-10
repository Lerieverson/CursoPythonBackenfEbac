bola = 0
if bola == 0:
    print("A bola está parada.")
elif bola ==1:
  print("O caminho escolhido foi o x.")
elif bola == 2:
  print("O caminho escolhido foi o y.")
elif bola == 3:
  print("O caminho escolhido foi o z.")
else:
  print("A bola está em movimento.")
  
email = "leri@gmail.com"
senha = "123456"


if email == "leri@gmail.com" or senha == "123456":
  print("Login bem-sucedido!")
else:
  print("Email ou senha incorretos.")

  # and-> Ambos os casos precisam acontecer
  # or -> Apenas um dos casos precisa acontecer
  
# Lista de dicionários representando o banco de dados de usuários
usuarios = [
    {"email": "leri@gmail.com", "senha": "123456"},
    {"email": "joao@gmail.com", "senha": "abcde"},
    {"email": "maria@gmail.com", "senha": "789"}
]

email_digitado = input("Digite seu email: ")
senha_digitada = input("Digite sua senha: ")

login_valido = False

# Percorre a lista para verificar cada cadastro
for usuario in usuarios:
    # IMPORTANTE: Usamos 'and' pois ambos devem estar corretos para o mesmo usuário
    if email_digitado == usuario["email"] and senha_digitada == usuario["senha"]:
        login_valido = True
        break  # Interrompe o loop se encontrar o usuário

if login_valido:
    print("Login bem-sucedido!")
else:
    print("Email ou senha incorretos.")
    
    
    
    
usuarios = [
    {"email": "leri@gmail.com", "senha": "123456"},
    {"email": "joao@gmail.com", "senha": "abcde"}
]

# 1. Identificar qual usuário quer mudar os dados (simulando um login)
email_atual = input("Digite seu email atual para segurança: ")
senha_atual = input("Digite sua senha atual: ")

usuario_encontrado = None

for usuario in usuarios:
    if usuario["email"] == email_atual and usuario["senha"] == senha_atual:
        usuario_encontrado = usuario
        break

# 2. Se o usuário for encontrado, solicita os novos dados
if usuario_encontrado:
    print("\nUsuário autenticado! Vamos alterar seus dados.")
    novo_email = input("Digite o novo email: ")
    nova_senha = input("Digite a nova senha: ")
    
    # Atualiza os valores dentro do dicionário na lista
    usuario_encontrado["email"] = novo_email
    usuario_encontrado["senha"] = nova_senha
    
    print("\nDados atualizados com sucesso!")
    print(f"Lista atualizada: {usuarios}")
else:
    print("\nFalha na autenticação. Não foi possível alterar os dados.")


# Listas para armazenar e-mails e senhas de vários cadastros
emails = ["usuario1@exemplo.com", "usuario2@exemplo.com"]
senhas = ["senha123", "minhasenha"]

email_digitado = input("Digite seu e-mail: ")
senha_digitada = input("Digite sua senha: ")

if email_digitado in emails:
    indice = emails.index(email_digitado)
    if senha_digitada == senhas[indice]:
        print("Login realizado com sucesso!")
    else:
        print("Senha incorreta!")
else:
    print("E-mail não cadastrado!")
#Esse exemplo permite comparar o e-mail e a senha inseridos com
