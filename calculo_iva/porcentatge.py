#!/usr/bin/python3
import json

class Porcentatge():
    def __init__(self, v1=0, v2=0):
        self._valor_1 = v1
        self._valor_2 = v2


    @property
    def valor_1(self):
        return self._valor_1

    @valor_1.setter
    def v1(self, valor):
        self._valor_1 = valor

    @property
    def valor_2(self):
        return self._valor_2

    @valor_2.setter
    def valor_2(self, valor):
        self._v2 = valor

    def calcula(self):
        base_imponible = self._valor_1
        tipo_aplicado = self._valor_1*self._valor_2/100
        importe_total = base_imponible + tipo_aplicado
        resultado = {
            "base_imponible": base_imponible, "tipo_aplicado": tipo_aplicado, "importe_total":importe_total
        }
        return resultado