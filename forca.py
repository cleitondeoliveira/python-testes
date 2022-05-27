import random
def jogar():
    abertura_do_jogo()
    palavra_secreta = carregando_as_palavras_secretas()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print (letras_acertadas)
      
    enforcou = False
    acertou = False
    erros = 0
            
    while(not acertou and not enforcou): #Enquanto nao enforcou e nao acertou continuar jogando (loop)
        
        chute = chute_da_palavra()
               
        if(chute in palavra_secreta): 
            marcacao_do_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
                              
        enforcou = erros == 5 #termina em 5
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        
    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

#def 1   
def abertura_do_jogo():
    print("###########################################################")
    print("-----------------Bem vindo ao jogo da Forca!------------------")
    print("###########################################################")

#def 2
def carregando_as_palavras_secretas():
    arquivo = open("palavras.txt", "r") #chama o txt e o read ao mesmo tempo
    palavras = []
    for linha in arquivo:
        linha = linha.strip() #para tirar as linhas \n
        palavras.append(linha)  
    arquivo.close()
    numero = random.randrange(0,len(palavras)) #para chamar as palavras aleatoriamente
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

#def 3
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]    
    
    
#def 4  
def chute_da_palavra():
    chute = input("Qual letra? ")
    chute = chute.strip().upper() #o strip faz com que ele ignore os espaços, linhas, palavras
    return chute

#def 5
def marcacao_do_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra): #letra maiuscula e minuscula
            letras_acertadas[index] = letra #o index substitui a forma em letras acertadas
        index += 1

#def 6
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print(" _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|  XXXX     XXXX   | /   ")
    print(" |  XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                       |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("      \______/           ")

#def 7
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("       .-\\:      /-.    ")
    print("      | (|:.     |) |    ")
    print("       '-|:.     |-'     ")
    print("         \\::.     /      ")
    print("           '::.  .'        ")
    print("             ) (          ")
    print("           _.' '._        ")
    print("         '-------'       ")

#def 8
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print("  |            ")
    print(" _|___         ")
    print()

 
if(__name__ == "__main__"):
    jogar()