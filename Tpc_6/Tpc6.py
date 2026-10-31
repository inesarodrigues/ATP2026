correr=True

tabMeteo1=[]

n=int(input("Quantos dias tem a sua lista:"))

for i in range(1, n + 1):
    dia = int(input(f"Qual foi o dia do {i} registo:"))
    mes = int(input(f"Qual foi o mês do {i} registo:"))
    ano = int(input(f"Qual foi o ano do {i} registo:"))
    TempMin = float(input("Qual foi a temperatura mínima registada nesse dia?"))
    TempMax = float(input("Qual foi a temperatura máxima registada nesse dia?"))
    p = float(input("Qual foi a precepitação resgistada nesse dia?"))
    
    Data = dia, mes, ano
    
    Dados = Data,TempMin,TempMax,p
    
    tabMeteo1.append(Dados)

def medias(tabMeteo): 
            res=[]
            for tabMeteo in tabMeteo1:
                Data,TempMin,TempMax, *_ = tabMeteo
                media = (TempMax + TempMin)/2
                res.append((Data, media))
            return res

def guardaTabMeteo(t, fnome):
        file = open(fnome,"w") 
        for dias in t:
            Data,TempMin,TempMax,Precipitacao = dias
            ano, mes, dia = Data
            file.write(f"{ano}-{mes}-{dia}|{TempMin}|{TempMax}|{Precipitacao}\n")
        file.close()

def carregaTabMeteo(fnome):
    res = []
    file = open(fnome,"r")
    for linha in file:
        data, tmin, tmax, p =linha.split("|") 
        ano,mes,dia = data.split("-")
        data=(int(ano),int(mes),int(dia))
        res.append(((int(ano),int(mes),int(dia)),float(tmin),float(tmax),float(p)))
    file.close()
    return res    


def minMin(tabMeteo):
    menor = tabMeteo[1]
    for e in tabMeteo:
        if e < menor:
            menor = e
    return menor

def amplTerm(tabMeteo):
    res = []
    for tabMeteo in tabMeteo1:
        Data,TempMin,TempMax, *_ = tabMeteo
        ampl = TempMax - TempMin
        res.append((Data, ampl))     
    return res 

def maxChuva(tabMeteo):
    max = tabMeteo[3]
    max_data = tabMeteo[0]
    for e in tabMeteo:
        if e > max:
            max = e

    return (max_data, max)

while correr:
    print("1: Calcula a média da temperatura.")
    print("2: Guardar dados num ficheiro.")
    print("3: Carregar os dados do ficheiro.")
    print("4: Calcular Temperatura Mínima.")
    print("5: Calcular Amplitude.")
    print("6: Calcular Precipitação Máxima.")
    print("7:")
    print("8:")
    print("9:")
    print("0: Sair da aplicação")
    op = int(input("Opção:"))

    if op == 1:
        print(medias(tabMeteo1))

    elif op == 2:
        guardaTabMeteo(tabMeteo1, "meteorologia.txt")
        print("Dados guardados.")

    elif op == 3:
        tabMeteo = carregaTabMeteo ("meteorologia.txt")
        print(tabMeteo)

    elif op == 4:
         print(minMin(tabMeteo1))

    elif op == 5:
         print(amplTerm(tabMeteo1))

    elif op == 6:
         print(maxChuva(tabMeteo1))
         
    elif op == 0:
        print("Fim da aplicação.")
        correr = False