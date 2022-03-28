import random

print("**********************************")
print("Bem vindo ao jogo de adivinhação")
print("**********************************")

numero_secreto= random.randrange(1,101) # 1 to 100 > +1 to generate till 100
total_tentativas=0

print("Qual o nível de dificuldade ?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Escolha o nível de dificuldade"))

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

    if(chute<1 or chute >100):
        print("Você deve digitar um número de 1 a 100!")
        continue
    elif(chute==numero_secreto):
        print("Você acertou !")
        break
    elif(chute>numero_secreto):
        print("Chute realizado maior que o número secreto")
    elif(chute<numero_secreto):
        print("Chute realizado menor que o número secreto")



