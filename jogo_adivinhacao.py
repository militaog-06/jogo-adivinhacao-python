import random

def adivinha_numero():
    numero_secreto = random.randint(1, 10)
    tentativas_restantes = 3

    for tentativa in range(3):
        while True:
            try:
                palpite = int(input('Tente adivinhar o número secreto: '))

                if palpite < 1 or palpite > 10:
                    print('Digite um número de 1 a 10!')
                    continue

                break

            except ValueError:
                print('Digite apenas números!')

        if palpite > numero_secreto:
            print('O número secreto é menor!')

        elif palpite < numero_secreto:
            print('O número secreto é maior!')

        else:
            print('Você acertou!')
            return

        tentativas_restantes -= 1

        print(f'Você ainda tem {tentativas_restantes} tentativa(s).')

    print(f'Você perdeu! O número secreto era {numero_secreto}.')


adivinha_numero()