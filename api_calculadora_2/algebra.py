#!/usr/bin/python3
import json

class Algebra():
    def __init__(self, v1=0, v2=0, op='+'):
        self._valor_1 = v1
        self._valor_2 = v2
        self._operador = op


    @property
    def valor_1(self):   # propiedad/atributo de la clase
        self._valor_1
        return self._valor_1

    @valor_1.setter
    def valor_1(self, valor):
        self._valor_1 = valor


    @property
    def valor_2(self):   # propiedad/atributo de la clase
        self._valor_2
        return self._valor_2

    @valor_2.setter
    def valor_2(self, valor):
        self._valor_2 = valor
    
    @property
    def operador(self):   # propiedad/atributo de la clase
        return self._operador

    @operador.setter
    def operador(self, valor):
        self._operador= valor

    def opera(self):
        if self._operador == "+":
            return self._valor_1 + self._valor_2
        if self._operador == "-":
            return self._valor1  - self._valor2

    def __str__(self):
        resultat = {"resultat": self.opera()}
        return json.dumps(resultat)