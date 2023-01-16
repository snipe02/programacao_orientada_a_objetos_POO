
class Cliente:
  def __init__(self, cpf, nome, idade):
    self.__cpf = cpf
    self.__nome = nome
    self.__idade = idade
  
  @property
  def cpf(self):
    return self.__cpf
  
  @property
  def nome(self):
    return self.__nome

  @property
  def idade(self):
    return self.__idade

class Seguro:
  def __init__(self, numero_apolice, proprietario): #AQUI EU PASSO UM OBEJTO CLIENTE.
    self._numero_apolice = numero_apolice
    self._proprietario = proprietario



  def calculaValor(self):
    pass
  
  def calculaPremio(self):
    pass
  
  def __str__(self):
     pass

class SeguroVida(Seguro):
  def __init__(self, numero_apolice, proprietario, nome_beneficiario):
    super().__init__(numero_apolice, proprietario)
    self._nome_beneficiario = nome_beneficiario
    
  
  def calculaValor(self):
    if self._proprietario.idade <= 30:
      return 800
      print('Cálculo do valor a ser pago calculado')
    
    elif self._proprietario.idade >= 30 and self._proprietario.idade <= 50:
      return 1300
      print('Cálculo do valor a ser pago calculado')

    elif self._proprietario.idade > 50:
      return 1600
      print('Cálculo do valor a ser pago calculado')

  def calculaPremio(self):
    if self._proprietario.idade <= 30:
      return 50000
      print('Cálculo do prêmio a ser pago calculado')
    
    elif self._proprietario.idade >= 30 and self._proprietario.idade <= 50:
      return 30000
      print('Cálculo do prêmio a ser pago calculado')

    elif self._proprietario.idade > 50:
      return 20000
      print('Cálculo do prêmio a ser pago calculado')

  def __str__(self):
     return f'Nome do Beneficiário: {self._nome_beneficiario}, Idade:{self._proprietario.idade}, Número da Apólice: {self._numero_apolice}, Proprietário: {self._proprietario.nome}, VALOR: {self.calculaValor()}, PREMIO: {self.calculaPremio()} '

class SeguroAutomovel(Seguro):
  def __init__(self, numero_apolice, proprietario, numero_licenca, nome_modelo, ano, valor_automovel):
    super().__init__(numero_apolice, proprietario)
    self._numero_licenca = numero_licenca
    self._nome_modelo = nome_modelo
    self._ano = ano
    self._valor_automovel = valor_automovel

#Para uma apólice de seguro de automóveis,
#exigem-se o número da licença, o modelo, o ano e o valor do automóvel.
  
  def calculaValor(self):
    valor_seguro = (3/100)*self._valor_automovel
    return valor_seguro
    print('Valor Calculado')
  
  def calculaPremio(self):
    return (80/100)*self._valor_automovel
    print('Valor Calculado')

  def calculaFranquia(self):
    franquia = (40/100)*self.calculaValor()
    return franquia


  def __str__(self):
    return f'Idade:{self._proprietario.idade}, NÚMERO DA APÓLICE: {self._numero_apolice}, Proprietário: {self._proprietario.nome}, VALOR: {self.calculaValor()}, PREMIO: {self.calculaPremio()} '

class ControleSeguros():
  def __init__(self):
    self._lista_seguros = []

  def cadastrar(self, seguro):
    if isinstance(seguro, Seguro):
      self._lista_seguros.append(seguro)
    else:
      print('Instância inválida')

  def relatorio(self):
    total_premio = 0
    valor_total = 0
    for seguro in self._lista_seguros:
      print(seguro)
      total_premio += seguro.calculaPremio()
      valor_total += seguro.calculaValor()
    print(f'VALOR TOTAL DO PRÊMIO ==> {total_premio}')
    print(f'VALOR TOTAL DO SEGURO ==> {valor_total}')



cliente1 = Cliente('05277829393', 'Kleber Junior', 29)

seguro1 = SeguroVida('01', cliente1, 'Lucia')

seguro1.calculaValor()


seguro1.calculaPremio()




seguroautomovel1 = SeguroAutomovel('01', cliente1, '0901923', 'Hilux', 2022, 300000)
seguroautomovel1.calculaValor()

seguroautomovel1.calculaPremio()



seguroautomovel1.calculaFranquia()

controle1 = ControleSeguros()

controle1.cadastrar(seguroautomovel1)


controle1.relatorio()

cliente2 = Cliente('97231235123', 'Joao Barbosa', 70)

seguroautomovel2 = SeguroAutomovel('83881234', cliente2, '773412', 'Fusca', 1970, 20000)
seguroautomovel2.calculaPremio()