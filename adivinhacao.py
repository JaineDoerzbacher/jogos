import random
import random


def jogar_adivinhacao():
    imprime_boas_vindas()
    numero_secreto = define_numero_aleatorio()
    total_de_tentativas = 0
    total_de_tentativas = define_dicifuldade()
    rodada = 1
    pontos = 1000
    while (rodada <= total_de_tentativas):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = digite_chute()

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto. E esta com {} pontos!".format(pontos))
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto E esta com {} pontos!".format(pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("Fim do jogo")


def imprime_boas_vindas():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def define_numero_aleatorio():
    numero_secreto = random.randrange(1, 101)
    return numero_secreto


def define_dicifuldade():
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))
    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    return total_de_tentativas


def digite_chute():
    chute_str = input("Digite o seu número: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)
    return chute


if (__name__ == "__main__"):
    jogar_adivinhacao()
