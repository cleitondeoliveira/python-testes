import adivinhacao
import forca
def escolha_o_jogo():
    print("###########################################################")
    print("--------------------Escolha seu jogo!----------------------")
    print("###########################################################")
                    
    print("(1)Forca (2) Adivinhação")

    jogo = int(input("Escolha o número do seu jogo:"))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
        
    elif(jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar() #import a frente e funcao atras
if(__name__ == "__main__"):
    escolha_o_jogo()