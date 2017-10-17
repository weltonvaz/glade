# -*- coding: UTF-8 -*-
class Conta(object):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def calcular_imposto(self):
        self.saldo = self.saldo * 0.10
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, titular, saldo):
        super(ContaCorrente, self).__init__(titular, saldo)

    def calcular_imposto(self):
        return super(ContaCorrente, self).calcular_imposto() + 20
