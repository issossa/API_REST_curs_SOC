#!/usr/bin/python3
import json

class Ciento():
    def __init__(self, v1=0, v2=0, oper='*'):
        self._v1 = v1
        self._v2 = v2
        self._oper = oper

    @property
    def v1(self):
        self._v1
        return self._v1

    @v1.setter
    def v1(self, valor):
        self._v1 = valor

    @property
    def v2(self):
        self._v2
        return self._v2

    @v1.setter
    def v1(self, valor):
        self._v2 = valor




    def operando(self):
        if self