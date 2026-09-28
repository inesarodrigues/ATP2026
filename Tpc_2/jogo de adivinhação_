import random

print("Bem-vindo ao Jogo de Adivinhação!")
print("1 - Tu adivinhas.")
print("2 - Computador adivinha.")

modo = input("Escolha o modo (1 ou 2):").strip()

if modo == '1':
    n = random.randint(1, 100)
    t = 0
    print("Tente adivinhar o número entre 1 e 100.")
    p = int(input("Digite o seu palpite: "))
    while p!=n:

        t = t + 1
        if 1>p or p>100: #define que os números dados pelo utilizador só pode estar neste range 
            print("O número que escolheu não está na lista dada.")
            t = t - 1
        elif p < n:
            print("O número que pensei é Maior.")
        elif p > n:
            print("O número que pensei é Menor.")
        p = int(input("Digite o seu palpite: "))

    print(f"Acertou o número {p} em {t} tentativas!")
           
elif modo == '2':
    lm = 1 #limite mínimo
    lM = 100 #limite máximo
    t = 0
    
    print("Pense em um número de 1 a 100.")
    print("Responda com 'O número que pensei é Menor'(-), 'O número que pensei é Maior'(+) ou 'Acertou'(=).")
    input("Pressione ENTER quando estiver pronto...")
    
    acertou = False

    while not acertou:
        
        p = (lm + lM) // 2
        t= t+1
        print(f"O meu palpite é: {p}")
        r = input("Está correto? ").strip()
        
        if r== '=':
            print(f"Ganhei! Acertei o número {p} em {t} tentativas!")
            acertou = True
        elif r == '+':
            lm = p + 1
        elif r == '-':
            lM = p - 1
        else:
            print("Resposta inválida! Por favor, use apenas '=', '+' ou '-'.")
            t = t - 1 # Não conta como tentativa válida
        
        if lm>lM:
                t=0
                print("Resposta inválida! Vamos tentar outra vez...")
                lm=1
                lM=100

     

        
