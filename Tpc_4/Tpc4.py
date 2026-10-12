### TPC4 (dia 5 de Outubro não há aula teórica): Aplicação para manipulação de listas de inteiros
#- Crie uma aplicação em Python que coloca no monitor o seguinte menu:
    #* (1) Criar Lista 
    #* (2) Ler Lista
    #* (3) Soma
    #* (4) Média
    #* (5) Maior
    #* (6) Menor
    #* (7) estaOrdenada por ordem crescente
    #* (8) estaOrdenada por ordem decrescente
    #* (9) Procura um elemento
    #* (0) Sair

#- O utilizador irá escolher uma das opções introduzindo o número correspondente;
#- Se a opção não for sair, a aplicação executa a operação pretendida, apresenta o resultado e a seguir apresenta de novo o menu;
#- Se a opção for sair, a aplicação termina colocando uma mensagem no monitor.

#* No desenvolvimento da aplicação deverá ter em atenção o seguinte:
    #- A aplicação terá uma variável interna para guardar uma lista de números;
    #- Na opção 1, deverá ser criada uma lista de números aleatórios entre 1 e 100 que será guardada na variável interna;
    #- Na opção 2, deverá ser criada uma lista com números introduzidos pelo utilizador, que será guardada na variável interna;
    #- Nestas primeiras opções, se a variável interna já tiver uma lista, esta será sobreposta/apagada pela nova lista;
    #- Na opção 3, será calculada a soma dos elementos na lista no momento;
    #- Na opção 4, será calculada a média dos elementos na lista no momento;
    #- Na opção 5, será calculado o maior elemento da lista no momento;
    #- Na opção 6, será calculado o menor elemento da lista no momento;
    #- Na opção 7, a aplicação deverá indicar (Sim/Não) se a lista está ordenada por ordem crescente;
    #- Na opção 8, a aplicação deverá indicar (Sim/Não) se a lista está ordenada por ordem decrescente;
    #- Na opção 9, a aplicação irá procurar um elemento na lista, se o encontrar deverá devolver a sua posição, devolverá -1 se o elemento não estiver na lista;
    #- Se o utilizador selecionar a opção 0, a aplicação deverá terminar mostrando a lista que está nesse momento guardada.

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
