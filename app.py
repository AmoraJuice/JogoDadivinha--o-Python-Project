# Jogo da Adivinhação

import random


def adivinhacao():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Bem-vindo ao jogo do adivinha-se!")
    print("Vou pensar em um numero entre 1 e 100. sera que consegue adivinhar?")

    while True:
        try:
            guess = int(input("Digite o seu palpite: "))
            attempts += 1

            if guess < secret_number:
                print("Muito baixo, boa sorte no novo palpite")
            elif guess > secret_number:
                print("Muito alto, boa sorte no novo palpite")
            else:
                print("Parabens! Voce acertou o numero em", attempts, "tentativas(s)!")
                break
        except ValueError:
            print("Entrada invalida amigo, digite um numero inteiro.")

adivinhacao()
