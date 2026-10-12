
import random
 
lista = []
op = True
 
while op:
    
    print("(1) Criar Lista")
    print("(2) Ler Lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) estaOrdenada por ordem crescente")
    print("(8) estaOrdenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) Sair")
    opcao = int(input("Opção: "))
 
    if opcao == 1:
        n = int(input("Quantos elementos? "))
        lista = []
        for i in range(n):
            lista.append(random.randint(1, 100))
        print("Lista criada:", lista)
 
    elif opcao == 2:
        n = int(input("Quantos elementos? "))
        lista = []
        for i in range(n):
            lista.append(int(input("Elemento: ")))
        print("Lista guardada:", lista)
 
    elif opcao == 0:
        print("Fim da aplicação. Lista guardada:", lista)
        op = False
 
    elif opcao >= 3 and opcao <= 9 and len(lista) == 0:
        print("A lista está vazia. Use primeiro a opção 1 ou 2.")
 
    elif opcao == 3:
        print("Soma:", sum(lista))
 
    elif opcao == 4:
        print("Média:", sum(lista) / len(lista))
 
    elif opcao == 5:
        print("Maior:", max(lista))
 
    elif opcao == 6:
        print("Menor:", min(lista))
 
    elif opcao == 7:
        if lista == sorted(lista):
            print("Sim")
        else:
            print("Não")
 
    elif opcao == 8:
        if lista == sorted(lista, reverse=True): # para fazer na ordem decrescente 
            print("Sim")
        else:
            print("Não")
 
    elif opcao == 9:
        x = int(input("Elemento a procurar: "))
        if x in lista:
            print("Posição:", lista.index(x))
        else:
            print("Posição:", -1)
 
    else:
        print("Opção inválida.")
