correr=True
while correr:
    print("1: Criar uma turma;")
    print("2: Inserir um aluno na turma;")
    print("3: Listar a turma;")
    print("4: Consultar um aluno por id;")
    print("8: Guardar a turma em ficheiro;")
    print("9: Carregar uma turma dum ficheiro;")
    print("0: Sair da aplicação")
    op = int(input("Opção:"))

    if op == 1:
        turma = []
        print(f"A turma foi criada:{turma}")

    elif op == 2:
        print("Insira os dados do aluno:")
        nome = input("Nome: ")
        id = input("Id: ")
        notaTPC = float(input("Nota TPC: "))
        notaProj = float(input("Nota Projeto: "))
        notaTeste = float(input("Nota Teste: "))
        aluno = (nome, id, [notaTPC, notaProj, notaTeste])
        turma.append(aluno)
        print("Aluno inserido.")

    elif op == 3:
         if len(turma) == 0:
            print("A turma está vazia.")
         else:
            for aluno in turma:
                print(aluno)

    elif op == 4:
        encontrado = True
        while encontrado:
            id = input("Id a consultar: ")
            if aluno[1] == id:
                print(aluno)
                encontrado = False
            else:
                print("Aluno não encontrado.")

    elif op == 8:
        def guardarTurma(turma, fnome):
            file = open(fnome,"w") 
            for termo in turma:
                    nome, id, notaTPC, notaProj, notaTeste = termo
                    file.write(f"{nome}#{id}#{notaTPC}#{notaProj}#{notaTeste}|")
                    file.write("\n")
            file.close()
        guardarTurma(turma,"turma.txt")

    elif op == 9:
        def recuperarTurma(fnome):
            turma = []
            file = open(fnome,"r")
            for line in file:
                aluno=[]
                inf = line.split("|") 
                for t in inf[-1]:
                    nome, id, notaTPC, notaProj, notaTeste = t.split("#")
                    termo = ((nome),(id),float(notaTPC),float(notaProj),float(notaTeste))
                    aluno.appende(termo)
                turma.append(aluno)
            file.close()
            return turma
        print(recuperarTurma("turma.txt") )

    elif op == 0:
        print("Fim da aplicação.")
        correr = False

    else: 
        print("Opção inválida")

