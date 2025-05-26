
from TipiDidati import *
from datetime import date

class Impiegato:
    _name:str
    _lastname:str 
    _nascita:date
    _stipendio:RealGEZ
    def __init__(self, nome:str, cognome, nascita):
        self.set_nome(nome)
        self.set_lastname(cognome)
        self._nascita = nascita
    def name(self)->str:
        return self._name
    def set_nome(self, name)->None:
        self._name = name
    
    def lastname(self) ->str:
        return self._lastname 
    def set_lastname(self, last) ->None:
        self._lastname = last
    def nascita(self) -> set:
        return self._nascita
    def stipendio(self)->RealGEZ:
        return self._stipendio
    def set_stipendio(self, gimmie_money:RealGEZ) ->None:
        self._stipendio = gimmie_money


class Dipartimento: 
    _name:str
    _telefono:Telefono
    _indirizzo: Indirizzo
    def __init__(self, name, telefono, indirizzo):
        self.set_nome(name)
        self.set_telefono(telefono)
        self._indirizzo = None
    def nome(self)->str:
        return self._name
    def set_name(self, name):
        self._name = name
    def telefono(self)->frozenset[Telefono]:
        return frozenset(self._telefono)
    def set_telefono(self, t: Telefono):
        self._telefono = t
    def add_telefono(self, t:Telefono)->None:
        self._telefono.add(t)
    def remove_telefono(self, t:Telefono)->None:
        self._telefono.remove(t)
    def indirizzo(self):
        return self._indirizzo
    def set_indirizzo(self, i:Indirizzo):
        self._indirizzo = i 

class Progetto: 
    _name:str
    _budget:RealGEZ
    def __init__(self, name, budget):
        self.set_nome(name)
        self.set_budget(budget)
    def nome(self):
        return self._name
    def set_nome(self, name):
        self._name = name
    def budget(self):
        return self._budget
    def set_budget(self, b):
        self._budget = b