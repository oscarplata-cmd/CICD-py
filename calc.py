import os
class Calculadora:

    def sum(self, a: float,b: float) -> float:
        return float(a) + float(b)
    
    def mul(self, a: float,b: float) -> float:
        return float(a) * float(b)


print(Calculadora().mul(1,2))