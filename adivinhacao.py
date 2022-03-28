import random

def jogar():
    print("**********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("**********************************")

    numero_secreto= random.randrange(1,101) # 1 to 100 > +1 to generate till 100
    total_tentativas=0
    pontos=1000

    print("Qual o nível de dificuldade ?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Escolha o nível de dificuldade: "))

    if(nivel==1):
        total_tentativas=20
    elif(nivel==2):
        total_tentativas=10
    else:
        total_tentativas=5

    for rodada in range(1,total_tentativas+1):
        print("Tentativa {} de {}".format(rodada,total_tentativas))
        chute_str = input("Digite um numero entre 1 e 100")
        print("Você digitou ",chute_str)
        chute=int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número de 1 a 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos !".format(pontos))
            break
        else:
            if(maior):
                print("Chute realizado maior que o número secreto")
            elif(menor):
                print("Chute realizado menor que o número secreto")
                pontos_perdidos = abs(numero_secreto - chute) #40 - 30 > perde 10 , 60-80 = -20 > para arrendodar => abs
                pontos = pontos - pontos_perdidos
    print("Fim de jogo")

if(__name__ == "__main__"): # se o ponto de entrada for em adivinhacao ele chama a funcao
    jogar()