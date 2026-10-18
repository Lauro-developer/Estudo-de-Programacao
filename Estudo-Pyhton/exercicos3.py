## ESTUDAR MAIS SOBRE WHILE E FOR

import random
import os
import sys
def continuar():
    opcao = str(input("VOCE QUER CONTINUAR: "))
    if opcao == "S":
        os.system("cls")
    elif opcao == "N":
         os.system("cls")
         print("PROGRAMA ENCERRADO COM SUCESSO...")
         sys.exit()

#---QUESTAO 01---
numero = [1,2,3,4,5,6,7,8,9,10]
nome = ["claudio","maria","jorge","carlos"]
anoN = input("Qual ano que voce nasceu: ")
anoA = input("Qual ano estamos atualmente: ")
ano_geral = [anoN,anoA]
print(numero)
print(nome)
print(ano_geral)
continuar()

#---QUESTAO 02---
numeros = [4,5,10,3,2,12,6]
i = 1
for numero in numeros:
    print(f"{i}.---{numero}")
    i+=1
continuar()

#---QUESTAO 03---
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)
continuar()

#---QUESTAO 04---
for i in range(10, -1, -1):
    print(i)
continuar()

    
#---QUESTAO 05---
numero = int(input("ME FALE UM NUMERO: "))
inicio = int(input("QUAL O COMECO: "))
fim = int(input("QUAL O FINAL: "))
for i in range(inicio, fim + 1):
    multi = i * numero
    print(f"{i} X {numero} = {multi}")
continuar()

#---QUESTAO 06---
soma_geral = 0
try:
    numero = int(input("QUANTOS NUMEROS VOCE QUER: "))
    for i in range(0,numero + 1):
        print(i)
        soma_geral += i
    print(soma_geral)
except:
    print("Erro: Por favor, digite apenas números válidos!")
continuar()

#---QUESTAO 07---
media_geral = 0
soma_geral = 0
inicial = int(input("Qual numero inicial da lista: "))
final = int(input("Qual numero final da lista: "))
try:
    for i in range (inicial,final + 1):
            lista_gerada = random.randint(inicial , final + 1)
            soma_geral += lista_gerada
            print(f"{i}--{lista_gerada}")
    media_geral = soma_geral / i
    print(f"A MEDIA DOS {i} NUMEROS É: {media_geral} ")
except ValueError :
        print("Nao foi possivel calcular, tente novamente [VOCE COLOCOU LETRA EM VEZ DE NUMERO]")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
         print(f"Ocorreu um erro: {e}")
sys.exit()