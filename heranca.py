# Classe Veiculo
class Veiculo:
  def __init__(self, rodas, marca):
    self.rodas = rodas
    self.marca = marca

  def ligar(self):
    print("Vrummmm!")

class Carro(Veiculo):
  def __init__(self, rodas, marca, teto_solar):
    super().__init__(rodas, marca)
    self.teto_solar = teto_solar
    