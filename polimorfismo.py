#polimorfismo
class Colaborador:
  def contratar_novo_colaborador(self):
     pass
  
class Estagiario(Colaborador):
  def contratar_novo_colaborador(self):
    return "Estagiário contratado com sucesso!"
  
class Diretor(Colaborador):
  def contratar_novo_colaborador(self):
    return "Diretor contratado com sucesso!"
  
class Gerais(Colaborador):
  def contratar_novo_colaborador(self):
    return "Gerais contratado com sucesso!"
  
Colaborador = [Estagiario(), Diretor(), Gerais()]
for colaborador in Colaborador:
  print(colaborador.contratar_novo_colaborador())