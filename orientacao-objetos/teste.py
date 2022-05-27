def cria_conta(numero, titular, saldo, limite): #definindo a funcao e paramentros
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "Limite": limite}
    return conta

def depositar(conta, valor): #depositar chama a o saldo
    conta["saldo"] += valor

def sacar(conta, valor): #depositar chama a o saldo
    conta["saldo"] -= valor #retira o valor
    
def extrato(conta):
    print("Saldo da conta é {}".format(conta["saldo"]))