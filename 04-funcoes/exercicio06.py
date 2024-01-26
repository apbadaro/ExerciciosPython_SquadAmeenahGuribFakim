"""
Vamos contruir um jogo da forca. O programa escolherá aleatoriamente uma palavra secreta de uma lista predefinida.
A palavra secreta será representada por espaços em branco, um para cada letra da palavra.
O jogador terá um número limitado de seis tentativas. Em cada tentativa, o jogador pode fornecer uma letra.
Se a letra estiver presente na palavra secreta, ela será revelada nas posições correspondentes.
Se a letra não estiver na palavra, uma mensagem de erro deverá ser informada. Após o número máximo de erros, o jogador perde.
O jogo continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas.
Dica: Você precisará importar uma biblioteca.
"""
from random import choice

palavras = ["asteroide", "estrela", "saturno", "cometa", "telescópio"]
palavra_secreta = choice(palavras).lower()
tentativas = 6
letras_adivinhadas = []

print("==============================")
print(
    "J O G O   D A   F O R C A\nTEMA: ESPAÇO\nVOCÊ TEM 6 (SEIS) TENTATIVAS. BOA SORTE!"
)
print("==============================")


while tentativas > 0:
    for letra in palavra_secreta:
        if letra in letras_adivinhadas:
            print(letra.upper(), end="")
        else:
            print("_ ", end="")
    chute = input("\n\nDigite uma letra: ").lower()

    if chute in palavra_secreta:
        print(f"Mandou bem!")
        letras_adivinhadas.append(chute)
    else:
        tentativas -= 1
        print(f"Ih, você errou!\nVocê tem: {tentativas} tentativa(s).")
    if set(palavra_secreta) == set(letras_adivinhadas):
        print(f"Parabéns! Você adivinhou a palavra secreta: {palavra_secreta.upper()}.")
        break
    elif tentativas == 0:
        print(
            f"\nSuas tentativas acabaram! A palavra secreta era: {palavra_secreta.upper()}."
        )
        break
