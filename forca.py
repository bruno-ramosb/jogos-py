import random

def jogar():

    print("**********************************")
    print("Bem vindo ao jogo da forca")
    print("**********************************")

    palavra_secreta="banana".upper()
    letras_acertadas = ["_","_","_","_","_","_"]

    tentativas = 0
    enforcou= False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual letra ?").upper().strip()

        if(chute in palavra_secreta):
            index=0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    print("Encontrado a letra {} na posição {}".format(letra,index))
                    letras_acertadas[index]= letra

                index += 1
        else:
            tentativas += 1

        enforcou = tentativas == 6
        acertou  = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou")
    else:
        print("Você perdeu !")
    print("Fim de jogo")


    print("Jogando ....")


if(__name__ == "__main__"):
    jogar()