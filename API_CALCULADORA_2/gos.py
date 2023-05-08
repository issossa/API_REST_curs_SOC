#!/usr/bin/python3

# import json solo si lo necesitas!!!

class Gos():
    def __init__(self, edat):
        self._edat=edat

    @property 
    def edat(self):
        return self._edat
    
    @edat.setter
    def edat(self,valor):
        self._edat=valor
    
    def calcula(self):
        if self._edat<=2:
            return self._edat*10.5
        else:
            return (self._edat-2)*4 + 21