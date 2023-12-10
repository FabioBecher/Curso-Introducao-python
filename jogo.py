import forca
import adivinhacao

print("*********************************")
print("********Escolha seu Jogo!********")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Escolha o jogo " +
                 '>>> '))
if (jogo == 1):
    print("Você escolheu o jogo da Forca")
    forca.jogar()
if (jogo == 2):
    print("Você escolheu o jogo de Adivinhação")
    adivinhacao.jogar()