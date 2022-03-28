import random



def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta().upper()

    letras_acertadas = inicializa_campos_da_forca(palavra_secreta)
    print(letras_acertadas)

    tentativas = 0
    max_tentativas = 6
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

        enforcou = tentativas == max_tentativas
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

def imprime_mensagem_abertura():
    print("**********************************")
    print("Bem vindo ao jogo da forca")
    print("**********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper().strip()
    return palavra_secreta

def inicializa_campos_da_forca(palavra):
    return ["_" for letra in palavra]

