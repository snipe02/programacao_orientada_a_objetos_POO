class BombaGasolina:
    def __init__(self, id_bomba, valor_litro, capacidade_bomba, quantidade_disponivel,
                 tipo_combustivel='gasolina comum'):
        self.__id_bomba = id_bomba
        self.__tipo_combustivel = tipo_combustivel
        self.__valor_litro = valor_litro
        self.__capacidade_bomba = capacidade_bomba
        self.__quantidade_disponivel = quantidade_disponivel
        self.__valor_faturado = 0
        self.__quantidade_vendida = 0

        if self.__quantidade_disponivel > self.__capacidade_bomba:
            self.__quantidade_disponivel = self.__capacidade_bomba

    @property
    def id_bomba(self):
        return self.__id_bomba

    @property
    def tipo_combustivel(self):
        return self.__tipo_combustivel

    @property
    def valor_litro(self):
        return self.__valor_litro

    @property
    def capacidade_bomba(self):
        return self.__capacidade_bomba

    @property
    def quantidade_disponivel(self):
        return self.__quantidade_disponivel

    @property
    def valor_faturado(self):
        return self.__valor_faturado

    @property
    def quantidade_vendida(self):
        return self.__quantidade_vendida

    @valor_litro.setter
    def valor_litro(self, valor):
        if valor > 0:
            self.__valor_litro = valor
            print(f'O valor do Litro da BOMBA {self.__id_bomba} é R${self.__valor_litro}.')
        else:
            print('Digite um valor válido')

    def abastecer_bomba(self):
        self.__quantidade_disponivel = self.__capacidade_bomba
        print(f'{self.__capacidade_bomba} Litros <<- QUANTIDADE DÍSPONIVEL')

    def abastecerVeiculoPorValor(self, valor):
        if (valor / self.__valor_litro) > self.__quantidade_disponivel:
            print(f'A bomba não tem combustível suficiente pra abastecer R${valor}')
        else:
            self.__quantidade_disponivel = (self.__quantidade_disponivel - (valor / self.__valor_litro))
            self.__quantidade_vendida += (valor / self.__valor_litro)
            self.__valor_faturado += valor
            print(f'Foi colocado {valor / self.__valor_litro} Litros')

    def abastecerVeiculoPorLitro(self, valor):
        if valor > 0:
            if valor > self.__quantidade_disponivel:
                print('A bomba não tem combustível suficiente')
            else:
                self.__quantidade_disponivel -= valor
                self.__valor_faturado += valor * self.__valor_litro
                self.__quantidade_vendida += valor
                print(f'O valor a ser pago é de R${valor * self.__valor_litro}.')

    def __str__(self):
        print(
            f'QUANTIDADE DISPONÍVEL ==> {self.__quantidade_disponivel} Litros\nQUANTIDADE DE LITROS VENDIDOS ==> {self.quantidade_vendida} Litros\nVALOR FATURADO ==> R${self.__valor_faturado}')


print('BOMBA1')
# BOMBA1
bomba1 = BombaGasolina(1, 5.00, 1000, 50)

bomba1.abastecer_bomba()
bomba1.abastecerVeiculoPorLitro(100)
bomba1.abastecerVeiculoPorValor(350)
bomba1.abastecerVeiculoPorLitro(8)
bomba1.abastecerVeiculoPorLitro(45)
bomba1.abastecerVeiculoPorLitro(500)
bomba1.abastecerVeiculoPorLitro(250)
bomba1.abastecerVeiculoPorLitro(30)
bomba1.abastecerVeiculoPorValor(130)
bomba1.valor_litro = 6.78
bomba1.abastecerVeiculoPorValor(5)
bomba1.valor_litro

print(' ')
print('BOMBA2')
# BOMBA2
bomba2 = BombaGasolina(2, 12, 500, 100, 'gasolina aditivada')
bomba2.abastecerVeiculoPorValor(24)
bomba2.abastecerVeiculoPorLitro(98)

print(' ')
print('BOMBA3')
# BOMBA3
bomba3 = BombaGasolina(3, 5, 100, 150, 'etanol')
bomba3.abastecerVeiculoPorLitro(30)
bomba3.valor_faturado
bomba3.abastecerVeiculoPorValor(100)
bomba3.valor_faturado
bomba3.valor_litro = 8.99
bomba3.abastecerVeiculoPorValor(9)

print(' ')
print('BOMBA4')
# BOMBA4
bomba4 = BombaGasolina(4, 7.80, 500, 700, 'diesel')
bomba4.quantidade_disponivel
bomba4.abastecerVeiculoPorValor(100)
bomba4.abastecerVeiculoPorLitro(40)
print(' ')
print('BOMBA1')
bomba1.__str__()
print(' ')
print('BOMBA2')
bomba2.__str__()
print(' ')
print('BOMBA3')
bomba3.__str__()
print(' ')
print('BOMBA4')
bomba4.__str__()

print('')
print(
    f'VALOR FINAL FATURADO DAS 4 BOMBAS ==> R${bomba1.valor_faturado + bomba2.valor_faturado + bomba3.valor_faturado + bomba4.valor_faturado:.2f}')