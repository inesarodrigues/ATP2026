import random

print("Bem-vindo à Corrida dos 100!")
print("1 - Tu começas primeiro")
print("2 - Computador começa primeiro")
modo = int(input("Escolha o modo (1 ou 2): "))

total = 0
vez_pc = (modo == 2)

while total < 100:
    if vez_pc: 
        jogada = (100 - total) % 11
        if jogada == 0:
            jogada = random.randint(1, 10)  # posição perdida: nenhuma jogada é melhor, joga ao acaso
        total = total + jogada
        print("Computador soma", jogada, "-> total =", total)
    else:
        jogada = int(input("A tua jogada (1 a 10): "))
        while jogada < 1 or jogada > 10 or total + jogada > 100:
            jogada = int(input("Inválida. A tua jogada (1 a 10): "))
        total = total + jogada
        print(f"Jogador soma {jogada} -> total ={total}")
    vez_pc = not vez_pc # para trocar entre o else e o if

if vez_pc:
    print("Venceste!")
else:
    print("O computador venceu!")