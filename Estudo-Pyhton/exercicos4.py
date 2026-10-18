import random
import os
import sys
def continuar():
    opcao = str(input("VOCE QUER CONTINUAR: "))
    if opcao == "S":
        os.system("clear")
    elif opcao == "N":
         os.system("clear")
         print("PROGRAMA ENCERRADO COM SUCESSO...")
         sys.exit()
         
#---QUESTAO 01---
nome = input('Me diga seu nome: ')
idade = int(input('Me diga sua idade: '))
cidade = input('Me diga cidade que voce mora: ')
lista_dados_pessoas = []
dados_pessoa = {'nome': nome,'idade': idade,'cidade': cidade}
lista_dados_pessoas.append(dados_pessoa)
for lista_dado_pessoa in lista_dados_pessoas:
        nome = lista_dado_pessoa['nome']
        idade = lista_dado_pessoa['idade']
        cidade = lista_dado_pessoa['cidade']
print(nome,idade,cidade)


#---QUESTAO 2.0---
idade_atualizada = int(input('atualiza sua idade: '))
dados_pessoa['idade'] = idade_atualizada
print(f'Sua idade agora é {idade_atualizada}')
print(lista_dados_pessoas)

#---QUESTAO 2.1---
profissao = input('Me diga sua profisao: ')
dados_pessoa.update({'profissao': profissao})
for lista_dado_pessoa in lista_dados_pessoas:
    profissao = lista_dado_pessoa['profissao']
print(f'Seu nome: {nome}, sua idade era {idade} e foi para {idade_atualizada}, morando em {cidade}, tendo como profissao {profissao}')

#---QUESTAO 2.1---
item = input('qual item voce quer excluir: ')
for lista_dado_pessoa in lista_dados_pessoas:
    if item in lista_dado_pessoa:
        lista_dado_pessoa[item] = ''
        print(f'O item do campo "{item}" removido.')
    else:
         print('Esse campo não existe.')
print(lista_dados_pessoas)

#---QUESTAO 03---
quadrados = {}
numero_inicio = int(input('qual o comeco da relacao: '))
numero_final = int(input('Qual o final da relacao: '))
for i in range(numero_inicio, numero_final + 1):
    quadrados[i] = i * i
    print(f'{i}--- O quadrado é {quadrados[i]} ({i}X{i})')
    
#---QUESTAO 04---
dicionario = {}
dicionario['esporte'] = input('Me diga seu esporte: ')
chave = input('qual chave vc procura: ')
if chave in dicionario:
   print(f"Achei! Valor: {dicionario[chave]}")
else:
    print(f'Nao foi achado a chave {chave}')
    
    
#---QUESTAO 05---
frequencia = {}
frase = input('Digite uma frase: ')
palavras = frase.lower().split()
for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1
for palavra, contagem in frequencia.items():
    print(f'{palavra}: {contagem}')