from datetime import datetime
import pytz
from random import randint

class ContaCorrente():
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes

    Atributos:
        nome (str): Nome do Cliente
        cpf(str): CPF do Cliente. Deve ser inserido com pontos e traços (xxx.xxx.xxx-xx)
        agencia(str): Número da agência
        num_conta(str): Número da Conta Corrente do Cliente
        saldo: Saldo disponivel pelo Cliente
        Limite: Limite de cheque especial daquele Cliente
        transacoes: Histórico de Transações do Cliente
    """

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self._cartoes = []

    def consultar_saldo(self):
        print(f"Seu saldo atual é de R${self._saldo:,.2f}")
        pass
    
    def depositar_dinheiro(self, valor):
        self._saldo += valor
        self._transacoes.append(("Depósito: ",valor,"Saldo: ",self._saldo, ContaCorrente._data_hora()))
        pass
 
    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print("Você não tem saldo suficiente para sacar esse valor!")
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append(("Saque: ",valor, "Saldo: ",self._saldo, ContaCorrente._data_hora()))
        pass

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append(("Transferir: ", -valor,"Saldo: ",self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))

    def consultar_historico_transacoes(self):
        print("Historico de Transações: ")
        for transacao in self._transacoes:
            print(transacao)

class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint(10000000000000000, 99999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0,9), randint(0,9), randint(0,9))
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente._cartoes.append(self)