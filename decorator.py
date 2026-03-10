def meu_decorator(func):
    def wrapper():
        print("Antes que seja tarde de mais volte para:")
        func()
        print("Ele quer salvar você Venha ele TE AMA!")
    return wrapper
  
@meu_decorator
def minha_funcao():
    print("Jesus Cristo")
    
minha_funcao()