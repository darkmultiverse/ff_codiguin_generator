import random
import csv

char = "023456789ABCDEFGHJKLMNPQRSTUVWXYZ"
opcao = 0
opcao2 = 0
num_caract = 7
print ('''    ------------------------------------------
        GERADOR DE CODIGUIN FF 0.3
    ------------------------------------------
    ''')
n = int(input("    Quantos CODIGUIN FF deseja gerar? \n"))
n +=1

while opcao != 9:
    print('''    ------------------------------------------
        SELECIONE UMA OPÇÃO:
    ------------------------------------------
    1 - AK Chama do Dragão
    2 - Calça Angelical
    3 - Passe de Elite
    4 - Incubadora M4A1
    5 - Barba do Velho
    6 - Bandeirão
    7 - Kit Angelical
    8 - Personagem Chrono
    9 - 500 Dimas BOOYAH
    10 - Iniciativa Cobra
    ------------------------------------------
    ''')
    opcao = int(input("    Qual a opcao desejada? \n"))
    print ()
    if opcao == 1:
        fivein = '6YW3L'
        break
    elif opcao == 2:
        fivein = 'UWRQ2'
        break
    elif opcao == 3:
        fivein = 'SPEHG'
        break
    elif opcao == 4:
        fivein = 'PUXW4'
        break
    elif opcao == 5:
        fivein = 'AVXTQ'
        break
    elif opcao == 6:
        fivein = 'W8TAU'
        break
    elif opcao == 7:
        fivein = 'T6XKC'
        break
    elif opcao == 8:
        fivein = 'ACDBH'
        break
    elif opcao == 9:
        fivein = 'WZ6DH'
        break
    elif opcao == 10:
        fivein = '2QEW7'
        break
    else:
        print("opcao invalida")
        break
 
def codiguin():
    if (num_caract < 0):
        return "Erro: número negativo"
    elif (num_caract == 0):
        return "Erro: Tem que ter pelo menos 1 caracter."
    else:
        codaleator = ""
    while len(codaleator) != num_caract:
        codaleator = codaleator + random.choice(char)
    if len(codaleator) == num_caract:
        return "%s%s" %(fivein, codaleator)
        
def save_txt():
    print ()
    print ("Lista de CODIGUIN FF gerados em TXT com SUCESSO!!! ")  
    print ()     
    arquivo = open("codiguin_ff.txt",'w')
    for i in range(1,n):
        arquivo.write("Codiguin: %s"%(codiguin())+"\n")  
    arquivo.close()
    
def save_csv():
    print ()
    print ("Lista de CODIGUIN FF gerados em CSV com SUCESSO!!! ")  
    print ()  
    with open("codiguin_ff.csv",'w', newline='') as codiguin_ff:
        escrever = csv.writer(codiguin_ff)   
        for i in range(1,n):
            escrever.writerow(["%s"%(codiguin())])
 
def imprimir_tela():
    print ("Lista de CODIGUIN FF gerados: ")  
    print ()     
    for i in range(1,n):
        print ("Codiguins: %s"%(codiguin()))
     
while opcao2 != 2: 
    print ('''    ------------------------------------------
        SELECIONE UMA OPÇÃO:
    ------------------------------------------  
    1 - IMPRIMIR NA TELA 
    2 - SALVAR EM CSV
    3 - SALVAR EM TXT
    4 - SAIR
    ''')
    opcao2 = int(input("    Qual a opcao desejada? \n"))
    if opcao2 == 1:
        imprimir_tela()
    elif opcao2 == 2:
        save_csv() 
    elif opcao2 == 3:
        save_txt()
    elif opcao2 == 4:
        break
    else:
        print("opcao invalida")        