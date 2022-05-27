
class Conta: 
    #funcoes __#__ com significado especial (construtoras)
    def __init__(self, numero, titular, saldo, limite):
         print ("Construindo objeto --- {}".format(self))
         self.numero = numero
         self.titular = titular
         self.saldo = saldo
         self.limite = limite
        
    