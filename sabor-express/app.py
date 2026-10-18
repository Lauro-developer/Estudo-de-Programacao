## FAZER UMA VALIDCAO SE FOR NUMERO NO CADASTRO DE RESTAURANTES;
## FAZER UMA VALIDACAO CASO O USUARIO NAO DIGITE NADA NO CADASTRO;
## AJUSTAR A ATIVACAO DOS RESTAURENTES
import os
lista_restaurantes = [{'nome': 'MAMMA JAMMA','tipo':'Italiano','verificado':True}] 

def voltar_tela_inicial():
    '''Sempre que a apliacao for para um caminho que o usuario nao deveria, ela volta a tela iniclal'''
    input("\nAPERTE QUALQUER TECLA PARA VOLTAR AO MENU PRINCIPAL: ")
    main()

def lista_nome_restaurante():
    '''Funcao para listar os nomes dos restaurantes'''
    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(22)} | {'Status'}')
    i = 1 
    for lista_restaurante in lista_restaurantes:
            l_nome_restaurante = lista_restaurante['nome']
            l_categoria_restaurante = lista_restaurante['tipo']
            l_ativo_restaurante = 'ativado' if lista_restaurante['verificado'] == True else 'desativado'
            print(f"{i}-{l_nome_restaurante.ljust(20)} | {l_categoria_restaurante.ljust(22)} | {l_ativo_restaurante}")
            i+=1
            
def setar_apliacao(texto=""):
    '''funcao chamada para restaurar a pagina sempre que voltar para menu ou tiver um menu para opcoes'''
    os.system("clear")
    print ("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░l░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)
    print(texto)
       
def opcao():
    '''lista das opcoes'''
    print("\n 1 Cadastrar Restaurante")
    print("\n 2. Listar Restaurantes")
    print("\n 3. Estado do Restaurante")
    print("\n 4. Sair\n")

def opcao_invalida():
    '''Caso a opcao seja invalida'''
    setar_apliacao("OPÇÃO INVALIDA\n")
    voltar_tela_inicial()

def finalizar_app():
        '''Para a ultima opcao, para encerrar o app'''
        setar_apliacao("ENCERRENDO O APP...\n")

def cadastrar_restaurante():
    '''funcao que cadastra os restaurantes, caso acha seu restaurante, e'''
    setar_apliacao("BEM VINDO AO CADASTRO DE NOVOS RESTAURANTES\n")
    restaurante = input("Nome do restaurante: ").upper()
    categoria = input(f"Qual categoria do restaurante {restaurante}: ").upper()
    dados_do_restaurente = {'nome': restaurante,
                            'tipo': categoria,
                            'verificado': False }
    lista_restaurantes.append(dados_do_restaurente)
    setar_apliacao()
    print(f"O RESTAURANTE {restaurante} FOI CADASTRADO COM SUCESSO\n")
    escolha = input("CONTINUAR OU PARAR: ").upper()
    if escolha == "CONTINUAR":
        cadastrar_restaurante()
    elif escolha == "PARAR":
        if (len(lista_restaurantes) > 1):
            setar_apliacao("SEUS RESTAURANTES FORAM CADASTRADOS COM SUCESSO \n")
            voltar_tela_inicial()
        else:
            setar_apliacao("SEU RESTAURANTE FOI CADASTRADO COM SUCESSO \n")
            voltar_tela_inicial()
    else:
        opcao_invalida()

def listar_restaurantes():
    '''funcao que lista os restaurantes cadastrados, caso nao tenha cadastrado nenhum, a funcao pede para cadastrar'''
    setar_apliacao("BEM VINDA A LISTA DE RESTAURANTES:\n")
    try:
        if lista_restaurantes == []:
            print("VOCE PRECISA CADASTRAR RESTAURANTES PARA LISTAR ELES!\nVOLTE A OPCAO NUMERO 1 PARA VER A LISTA DE RESTAURANTES CADASTRADOS\n")
            escolha = int(input("DIGITE 0 PARA VOLTAR AO MENU PRINCIPAL OU DIGITE 1 PARA CADASTRAR RESTAURANTES: "))
            if (escolha == 0):
                main()
            elif (escolha == 1):
                cadastrar_restaurante()
            else:   
                opcao_invalida()
        else:
                lista_nome_restaurante()
                voltar_tela_inicial()
    except:
        main()

def alternar_estado_restaurante():
    '''funcao que alterá o estado do restaurante para ativo ou desativado, caso nao ache o restaurente ele informa e pede para voltar ao menu para cadastrar'''
    if len(lista_restaurantes) > 1:
        setar_apliacao("BEM VINDA A VERIFICACAO DE ESTADO DE SEUS RESTAURANTES \n")
    else:
        setar_apliacao("BEM VINDA A VERIFICACAO DE ESTADO DO SEU RESTAURANTE \n")
    escolher_nome_restaurante = input("Digite o nome do Restaurante que deseja verificar: ").upper()
    setar_apliacao()
    restaurante_encontrado = False
    for lista_restaurante in lista_restaurantes:
        if escolher_nome_restaurante == lista_restaurante['nome']:
            restaurante_encontrado = True
            print(f'{escolher_nome_restaurante} FOI ENCONTRADO')
        try:
            if lista_restaurante['verificado'] == False:
                ativacao = int (input('PORÉM NAO ESTÁ ATIVO: DIGITE [0] PARA ATIVAR: '))
                setar_apliacao()
                if ativacao == 0:
                    lista_restaurante['verificado'] = not lista_restaurante['verificado']
                    ativacao = lista_restaurante['verificado']
                    ativacao = ('ativado')
                    print(f"Seu restaurente agora está {ativacao}")
            else:
                desativar = int(input(f'SEU RESTAURANTE ESTÁ ATIVADO, DIGITE [1] PARA DESATIVA OU [0] PARA VOLTAR AO MENUR PRINCIPAL: '))
                if desativar == 1:
                    lista_restaurante['verificado'] = not lista_restaurante['verificado']
                    desativar = lista_restaurante["verificado"]
                    desativar = ('desativado')
                    print(f"Seu restaurente agora está {desativar}")
                elif desativar == 0 :
                    main()
                else:
                    opcao_invalida()
        except:
            setar_apliacao()
            print("NAO É PERMITIDO LETRA OU SIMBOLOS!")
            voltar_tela_inicial()
    if not restaurante_encontrado:
            print(f'O RESTAURANTE {escolher_nome_restaurante} NAO FOI ENCONTRADO , VERIFIQUE O NOME E TENTE NOVAMENTE\n')
            y = int(input('ESCOLHA [0] PARA VOLTAR AO "Estado Restaurante" E [1] PARA IR AO "Cadastrar Restaurante": '))
            if y == 0:
                alternar_estado_restaurante()
            else:
                cadastrar_restaurante()
    voltar_tela_inicial()
            
def escolher_opcao():
    '''funcao criada para escolher a opcao da lista de opcoes'''
    try:
        opcao_escolhida = int(input("Escolha a opcao desejada:"))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            setar_apliacao()
            print("NECESSARIO ESCOLHER UMA DESSAS OPÇÕES!")
            opcao()
            escolher_opcao()
    except:
        setar_apliacao()
        print("NAO É PERMITIDO LETRA OU SIMBOLOS!")
        voltar_tela_inicial()

def main():
    '''funcao que deixar a aplicacao na tela inicial'''
    setar_apliacao()
    opcao()
    escolher_opcao()  

if __name__ == "__main__":  
    main()




    
