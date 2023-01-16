class ContaCorrente:
    def __init__(self, numero, saldo=0):
        self._numero = numero
        self._saldo = saldo
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
      return self._numero
     

    def creditar(self, valor):
        self._saldo += valor
        print('O crédito foi efetuado')

  
    def debitar(self, valor):
        if valor < self._saldo:
            self._saldo -= valor
            print('O valor foi debitado')
        else:
            print('Não é possível debitar um valor menor do que o saldo existente')


    def transferir(self, valor, conta):
        if self._saldo >= valor:
            self._saldo -= valor
            conta._saldo += valor
            print(f'Valor transferido com sucesso. Você agora tem R${self._saldo}')
            print(f'A conta que foi efetuada o saque, agora possui R${conta._saldo}')
        else:
            print('Você não tem saldo suficiente')
  
    def __str__(self):
        return 'CONTA ==> '+ str(self._numero) + f' // saldo: R${self._saldo},00'
  
class ContaPoupanca(ContaCorrente):
  def __init__(self, numero, tx_juros, saldo=0):
    super().__init__(numero, saldo)
    self._tx_juros = tx_juros

  @property
  def tx_juros(self):
    return self._tx_juros

  def render_juros(self):
    if self._saldo != 0:
      self._saldo += ((self._tx_juros/100)*self._saldo)
      print(f'O juros rendeu. Seu saldo agora é R${self._saldo},00')
    else:
      print('Impossível fazer o seu dinheiro render, invista primeiro!')

  def __str__(self):
    return super().__str__()+ f' // tx juros:{self._tx_juros}%' #AQUI COM O super(). CHAMO O __str__() da classe ContaCorrente


class ContaImposto(ContaCorrente):
  def __init__(self, numero, percentual_imposto, saldo=0):
    super().__init__(numero, saldo)
    self._percentual_imposto = percentual_imposto
  
  @property
  def percentual_imposto(self):
    return self._percentual_imposto
  
  
  def calcula_imposto(self):
    self._saldo -= self._saldo*(self._percentual_imposto/100)
    print(f'O valor do atual do saldo é {self._saldo}')

  def __str__(self):
    return super().__str__()+  '\n' f'O seu percentual de desconto foi de {self._percentual_imposto}%'

print(' ')
print('CONTA CORRENTE'+'\nCONTA01 & CONTA02')
c1_cc = ContaCorrente('01cc')
c2_cc = ContaCorrente('02cc')
print('OPERAÇÕES ENTRE AS DUAS CONTAS CORRENTES')
c1_cc.transferir(1000, c2_cc)
c1_cc.creditar(2000)
c1_cc.transferir(1500, c2_cc)
c2_cc.debitar(5000)
c2_cc.debitar(1450)
print(c1_cc)
print(c2_cc)

print(' ' + '\n--------------------------------------------------------------------------' + '\nCONTA POUPANÇA'+'\nCONTA01 & CONTA02')
c1_cp = ContaPoupanca('01cp', 10)
c2_cp = ContaPoupanca('02cp', 5, 1000)
print('OPERAÇÕES ENTRE AS DUAS CONTAS POUPANÇAS E CONTAS DAS OUTRAS CLASSES')
c1_cp.render_juros()
c2_cp.transferir(500, c1_cc)
c2_cp.transferir(250, c1_cp)
c1_cp.render_juros()
c2_cp.creditar(750)
c2_cp.render_juros()
c2_cp.transferir(50, c1_cc)
c1_cp.debitar(200)
print(c2_cp.saldo)
print(c1_cp)
print(c2_cp)

print(' ' + '\n--------------------------------------------------------------------------' + '\nCONTA POUPANÇA'+'\nCONTA01 & CONTA02')
c1_ci = ContaImposto('01ci', 10, 10000)
c2_ci = ContaImposto('02ci', 5, 50000)
print('OPERAÇÕES ENTRE AS DUAS CONTAS IMPOSTOS E CONTAS DAS OUTRAS CLASSES')
c2_ci.calcula_imposto()
c2_ci.debitar(5000)
print(c1_cc.saldo)
c2_ci.transferir(10000, c1_cc)
print(c2_ci.saldo)
print(c1_ci.saldo)
c1_ci.calcula_imposto()
print(c1_ci.percentual_imposto)
print(c1_ci)
print(c2_ci)
print(f'{c1_cp.tx_juros}%')