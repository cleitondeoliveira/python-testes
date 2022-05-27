import random
def jogar():
        
        print("###########################################################")
        print("Bem vindo ao jogo da adivinhação!")
        print("###########################################################")

                #variaveis
        numero_secreto = random.randrange(1,101)
        total_de_tentativas = 0
        pontos = 1000


        print("Qual nivel de dificuldade?")
        print("(1) Fácil (2) Médio (3) Difícil")
                #input ja com int incluso
        nivel = int(input("Defina o nivel de dificuldade: "))

        if(nivel == 1):
                total_de_tentativas = 20
        elif(nivel == 2):
                total_de_tentativas = 10
        else:
                total_de_tentativas = 5  

                #pode ser feito com while também
        for rodada in range (1, total_de_tentativas + 1): #laço
                print("Tentativa {} de {}".format(rodada, total_de_tentativas)) #string de interpulacao
                click_str = input("Digite seu número entre 1 e 100: ") #pede para digitar
                print("Você digitou: ", click_str)
                click = int(click_str) #declarando que é um inteiro
                
                if (click < 1 or click > 100):
                        print("Você deve digitar um número entre 1 e 100!")
                        continue
                
                acertou = numero_secreto == click
                maior = click > numero_secreto
                menor = click < numero_secreto

                if(acertou): #if e else precisa ser fechado com :
                        print("Você acertou e fez {} pontos!".format(pontos))
                        break #saiu do laço // funciona também com while
                elif(maior): #else fecha a condicional
                        print("Você errou! Seu número foi maior que o número secreto.") #elif continua a condicional
                elif(menor):
                        print("Você errou! Seu número foi menor que o número secreto.")
                
                pontos_perdidos = abs(numero_secreto - click)
                pontos = pontos - pontos_perdidos
                
                
        print("Fim do jogo!")
if(__name__ == "__main__"):
        jogar()