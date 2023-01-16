from random import randint, seed
seed()

class Bateria:
  def __init__(self, codigo, capacidade):
    self.__codigo = codigo
    self.__capacidade = capacidade
    self.__carga_atual = randint(0,100)

  
  @property
  def codigo(self):
    return self.__codigo

  @property
  def capacidade(self):
    return self.__capacidade

  @property
  def carga_atual(self):
    return self.__carga_atual

  def carregar(self, valor):
    if valor >= 0:
      if (self.__carga_atual + valor) > 100:
        self.__carga_atual = 100
      else:
        self.__carga_atual += valor
    else:
      print('O valor da carga não pode ser negativo')
    print(f'A carga atual é de {self.__carga_atual}%')
  
  def descarregar(self, valor):
    if valor > 0:
      self.__carga_atual -= valor
      if self.__carga_atual < 0:
        self.__carga_atual = 0
      print(f'A carga atual é de {self.__carga_atual}%')
      

class Celular:
  def __init__(self, mei, bateria, WiFi, ligado=False):
    self.__mei = mei
    self.__bateria = bateria #Aqui eu torno obrigatório um celular ter uma bateria.
    self.__WiFi = WiFi
    self.__ligado = ligado

  @property
  def mei(self):
    return self.__mei
  
  @property
  def bateria(self):
    return self.__bateria

  @property
  def WiFi(self):
    return self.__WiFi
  
  @property
  def ligado(self):
    return self.__ligado

  
  def LigarDesligar(self):
    if self.__ligado == True:
      self.__ligado = False
      print('O celular foi desligado')
    elif self.__ligado == False:
      if self.__bateria != None:
        if self.__bateria.carga_atual > 0: #NESSE MOMENTO ACESSO O ATRIBUTO DA CLASSE AGREGADA(bateria.carga_atual)
            self.__ligado = True
        else:
          print('O celular não pode ser ligado, pois está com descarregado')
      else:
        self.__ligado = False
        print('O celular está sem bateria')

  def colocar_Bateria(self, bateria):
    if self.__bateria != None:
      print('O celular já possui uma bateria')
    else:
      self.__bateria = bateria
      print(f'A bateria foi instalada no celular')
    
  def retirarBateria(self):
    if self.__bateria != None:
      self.__bateria = None
    else:
      print('O celular já está sem bateria')
    
  def LigarDesligarWifi(self):
    if self.__WiFi == True:
      self.__WiFi = False
    else:
      self.__WiFi = True

  def assistirVideo(self, tempo):
    if self.__bateria == None:
      return 'Coloque a bateria para poder ligar o celular e assistir ao vídeo'
    if self.__ligado != True:
      return 'Não é possível assistir ao vídeo, pois o celular está desligado'
    elif self.__WiFi != True:
      return 'Ligue o Wi-Fi para assistir ao vídeo'
    elif self.__bateria.carga_atual <= (tempo*5):
      self.__bateria.descarregar(self.__bateria.carga_atual)
      self.__ligado = False
      print('O celular descarregou')
      
    else:
      self.__bateria.descarregar(tempo*5) #POSSO CHAMAR TRANQUILAMENTE ASSIM O MÉTODO DE OUTRA CLASSE NA CLASSE AGREGADORA(Celular)
      print('Reproduzindo vídeo...')
  
  def Carregar(self, valor):
    self.__bateria.carregar(valor)
    print('O celular está carregando...')

  def Descarregar(self, valor):
    self.__bateria.descarregar(valor)
    print(f'O celular descarregou...A quantidade atual de carga é de {self.__bateria.carga_atual}%')


bateria1 = Bateria('010101', 4000)

bateria2 = Bateria('020202', 3500)

bateria3 = Bateria('030303', 3000)

print('')
print('CELULAR1')
celular1 = Celular('2022pd22', bateria1, True)
celular1.ligado
celular1.assistirVideo(19)
celular1.retirarBateria()
celular1.bateria
celular1.LigarDesligar()
celular1.colocar_Bateria(bateria1)
celular1.LigarDesligar()
celular1.ligado
celular1.bateria.carga_atual
celular1.assistirVideo(2)
celular1.assistirVideo(10)
celular1.Descarregar(40)
celular1.Carregar(45)

print('')
print('CELULAR2')
celular2 = Celular('99iuyw7221', None, False)
celular2.assistirVideo(10)
celular2.LigarDesligar()
celular2.colocar_Bateria(bateria2) ##COMO CRIAR CRÍTICA PRA IMPEDIR QUE UMA BATERIA QUE JÁ ESTÁ SENDO USADA POR UM CELULAR SEJA IMPEDIDA DE SER COLOCADA EM OUTRO CELULAR?
celular2.ligado
celular2.LigarDesligar()
celular2.LigarDesligar()
celular2.assistirVideo(17)
celular2.LigarDesligar()
celular2.assistirVideo(2)
celular2.LigarDesligarWifi()
celular2.WiFi
celular2.assistirVideo(20)
celular2.Descarregar(20)
celular2.Carregar(29)
celular2.Carregar(89)

print('')
print('CELULAR3')
celular3 = Celular('2022yuaib5', bateria3, True, True)
celular3.ligado
celular3.bateria.carga_atual
celular3.assistirVideo(10)
celular3.retirarBateria()
celular3.LigarDesligar()
celular3.colocar_Bateria(bateria3)
celular3.Carregar(45)