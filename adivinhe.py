import random

randomico = random.randint(1, 21)
contador = 1
print('REGRAS: \n 1- O número não pode ser maior que 21')
nome = input('Qual seu nome?')
palpite = int(input('Adivinhe o Número de 1 à 21.'))


def acertou():
    global randomico
    global palpite
    if randomico == palpite:
        print('Você acertou!')


def quase():
    global randomico
    global palpite
    if palpite >= randomico - 5 and palpite <= randomico + 5:
        print('Você está quente')
    else:
        print('Você está frio!')


while randomico != palpite:
    if randomico > palpite and palpite <= 21:
        print('Quase! O numero é maior!')
        quase()
        palpite = int(input('Tente novamente'))
        acertou()
    elif randomico < palpite and palpite <= 21:
        print('Quase! O número é menor!')
        quase()
        palpite = int(input('Tente novamente'))
        acertou()
    elif palpite > 21:
        print('o número deve ser até 21')
        contador -= 1
        palpite = int(input('Tente novamente'))
        acertou()
    contador += 1

print(f'{nome}, Foram necessárias {contador} tentativas!')
