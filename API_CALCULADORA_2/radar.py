#!/usr/bin/python3

class Radar():
    def __init__(self,velocoche, velomax):
        self._velocoche=velocoche
        self._velomax=velomax
    @property
    def velocoche(self):
        return self._velocoche
    
    @velocoche.setter
    def velocoche(self,valor):
        self._velocoche=valor
    
    @property
    def velomax(self):
        return self._velomax
    
    @velomax.setter
    def velocoche(self,valor):
        self._velomax=valor


    def calcula(self):
        if self._velocoche <= self._velomax:
            return "correcte"
        
        elif self._velocoche <= 1.1*self._velomax:
            return "marge de seguretat"
        
        else:
            return "multa"