import re
from typing import Self, Any
from enum import *
from datetime import date
class CodiceFiscale(str):
    __pattern = re.compile(r"^[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}$")
    def __new__(cls, new_pattern:str)->Self:
        new_pattern = new_pattern.upper()
        # Controlla che new_pattern rispetti il pattern della variabile __pattern
        #Se ciò non accade solleva un errore
        if not cls.__pattern.match(new_pattern):
            raise ValueError(f"Il codice fiscale inserito non è valido: {new_pattern}")
        # Se il pattern è valido ritorna l'istanza come sottoclasse
        return super().__new__(cls, new_pattern)


class PartitaIva(str):
    __pattern_2 = re.compile(r"\d{11}+")
    def __new__(cls, iva:str):
        if not cls.__pattern_2.match(iva):
            raise ValueError (f"Valore non valido: {iva}")
        return super().__new__(cls, iva)


class CAP(str):
    def __new__(cls, cap:str) ->Self:
        if re.fullmatch(r'^\d{5}$', cap):
            return super().__new__(cls,cap)
        raise ValueError(f"La stringa '{cap}' non è un CAP italiano valido!")

class RealGEZ(float):
    # Tipo di dato specializzato reale >=0
    def __new__(cls, v: float|int|str|bool|Self):
        n :float = super().__new__(cls, v) #prova a convertire v in float
        if n >=0:
            return n
        raise ValueError(f"Il valore {n} è negativo!")
    
    


class IntGEZ(int):
    def __new__(cls, value:int|float|str|bool|Self):
        n:int = super().__new__(cls,value)
        if n >=0:
            return n 
        raise ValueError(f"Il valore {n} è negativo")
    


class IntDate(date):
    def __new__(cls, year, month, day):
        y:date = super().__new__(cls,year, month, day)
        if y.year > 1900:
            return y.year
        raise ValueError(f"L'anno {y.year} è minore o uguale 1900")
class Valuta(str):
    def __new__(cls, v:str)->Self:
        if re.fullmatch(r'^[A-Z]{3}$', v):
            return super().__new__(cls, v)
        raise ValueError(f"La stringa'{v}' non è un codice valido per una valuta!")

class Denaro:
    """
    Rappresenta il tipo di dato concettuale composto
    con i seguenti campi:
        - importo: Reale
        - valuta: Valuta
    """  
    _importo: float
    _valuta: float
    def __init__(self, imp: float, val:Valuta):
        self._importo = imp
        self._valuta = val
        def importo(self) -> float:
            return self._importo
        def valuta(self)->Valuta:
            return self._valuta
        def __str__(self)-> str:
            return f"{self.importo()} {self.valuta()}"
        def __repr__(self) ->str:
            return f"Denaro: {self.importo()} unità di valuta {self.valuta()}"
        def __hash__(self)-> int:
            return hash((self.importo(), self.valuta()))
        def __eq__(self, other: Any) ->bool:
            if not isinstance(other, type(self)) or \
                hash(self) == hash(other):
                return False
            return self.importo() == other.importo() and \
            self.valuta() == other.valuta()

def  add(self,other: Self) ->Self:
    """
    Somma self ad un'altra istanza di Denaro, ma solo se la valuta è la stessa.
    Restituisce una nuova istanza di Denaro
    """    
    if self.valuta() !=other.valuta():
        raise ValueError (f"Non posso sommare importi di valute diverse {self.valuta()} e {other.valuta()}")
    somma:float = self.importo() + other.importo()
    return Denaro(somma, self.valuta())

def __sub__(self, other:Self)->Self:
    return self + FloatDenaro(-other, other.valuta())

"""
Gli oggetti denaro li volgio usare come float qualsiasi
è il tipo di dato denaro basato sul float: essendo l'istanza di Denaro con la valuta eredita float e in più ha un campo valuta,
e in più 
"""
class FloatDenaro(float): 
    valuta: Valuta
    def __new__(cls, imp: float, val: Valuta)->Self:
        d = super().__new__(cls, imp)
        d.valuta = val
        return d
    def importo(self)-> float:
        return self.real
    def valuta(self)->Valuta:
        return self._valuta
    def __str__(self):
        return f"{self.importo()} {self.valuta()}"
    def __repr__(self):
        return f"Denaro: {self.importo()} unità di valuta {self.valuta()}"
    

class Email(str):
    __pattern_3 = re.compile(r"[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}")
    def __new__(cls, mail:str):
        if not cls.__pattern_3.match(mail):
            raise ValueError (f"Valore non valido: {mail}")
        return super().__new__(cls, mail)



class Telefono(str):
    __patern_4 = re.compile(r"\+[0-9]{10}")
    def __new__(cls, phone:str):
        if not cls.__patern_4.match(phone):
            raise ValueError(f"Valore non valido: {phone}")
        return super().__new__(cls, phone)
    

class StatoOrdine(StrEnum):
    in_preparazione = auto()
    inviato = auto()
    da_saldare = auto()
    saldato = auto()

class Indirizzo:
    _via: str 
    _civico: int 
    __cap_pattern = re.compile(r"\d{5}")
    def __init__(self, via: str, civico: int, cap: str) -> None:
        if not self.__cap_pattern.match(cap):
            raise ValueError (f"Il CAP fornito non è valido: {cap}")
        self._via = via
        self._civico = civico
        self._cap = cap
    def via(self) -> str:
        return self._via
    def civico(self) -> int:
        return self._civico
    def cap(self)-> str:
        return self._cap
    def __hash__(self) -> int:
        return hash((self._via, self._civico))
    def __eq__(self, other: Any) -> bool:
        if other is None or \
        not isinstance(other, type(self)) or \
        hash(self) != hash(other):
            return False
        return self._via == other._via and self._civico == other._civico and self._cap == other._cap

if __name__=="__main__":
    cf1: CodiceFiscale = CodiceFiscale("RSSMRA85M01H501Z")
    print(cf1, type(cf1))
    cf_2: CodiceFiscale = CodiceFiscale("DAATRF77U02H501B")
    cf_3: CodiceFiscale = CodiceFiscale("DAATRF77U02H501B")
    print(f"Test tra {cf1} e {cf_2} ")
    print(cf1 == cf_2)
    print(hash(cf1)==hash(cf_2))
    print(cf1 is cf_2)
    print("-------------------")
    print(f"Test tra {cf_2} e {cf_3} ")
    print(cf_2 == cf_3)
    print(hash(cf_2)==hash(cf_3))
    print(cf_2 is cf_3)
    
    print("\nTest PartitaIva")
    p_iva:PartitaIva = PartitaIva("12345678901")
    p_iva_2:PartitaIva = PartitaIva("12345678901")
    p_iva_3:PartitaIva = PartitaIva("34235678901")
    p_iva_4:PartitaIva = PartitaIva("45678901230")
    
    print(p_iva, type(p_iva))
    print(f"Test tra {p_iva} e {p_iva_2}")
    print(p_iva == p_iva_2)
    print(hash(p_iva)==hash(p_iva_2))
    print(p_iva is p_iva_2)
    email: Email = Email ("marco.pierleo@gmail.com")
    
    email_2:Email = Email ("leonardo.piccolo@outlook.com")
    email_3: Email = Email ("marco.pierleo@gmail.com")
    email_4:Email = Email ("leonardo.piccolo@outlook.com")
    print(f"Prima email:{email}\nSeconda Email: {email_2}")
    print(email, type(email) )
    print(f"\nPrimo test tra {email} e {email_2}")
    print(email == email_2)
    print(hash(email)==hash(email_2))
    print(email==email_2)
    print(email is email_2)
    print(f"\nSecondo test tra {email} e {email_3}")
    print(email==email_3)
    print(hash(email) == hash(email_3))
    print(email is email_3)
    print(f"Terzo test tra {email_2} e {email_4}")
    print(email_4 == email_2)
    print(hash(email_4)==hash(email_2))
    print(email_4==email_2)
    print(email_4 is email_2)
    
    print(f"\nTest degli oggetti della classe StatoOrdine:")
    print(StatoOrdine.da_saldare)
    print(f"\n{StatoOrdine.in_preparazione}")
    print(f"\n{StatoOrdine.inviato}")
    print(f"\n{StatoOrdine.saldato}")
    
    i1:Indirizzo = Indirizzo("Largo Arenula", civico=2, cap="00185")
    i2:Indirizzo = Indirizzo("Largo Arenula", civico=2, cap="00185")
    print(i1, i2)
    print(f"\nTest tra ")
    print(i1 == i2)
    print(hash(i1)==hash(i2))
    print(i1 is i2)
    
    y_1:IntDate = IntDate(1901, 2, 5 )
    # y_2:IntDate = IntDate(1899, 4, 20)
    
    print(y_1)
    
    num_1:IntGEZ = IntGEZ(1)
    num_2:IntGEZ = IntGEZ(0)
    num_3:IntGEZ = IntGEZ(-1)
    
    print(num_1)
    print(num_2)
    print(num_3)


