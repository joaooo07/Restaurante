import os
cadastro_r = [
            {'Nome' : 'Mc Donalds', 'Categoria' : 'FastFood(Hamburguer)', 'Ativo' : False}, 
              {'Nome' :'Burguer King', 'Categoria' : 'FastFood(Hamburguer)', 'Ativo' : True},
               {'Nome' : 'Cadillac', 'Categoria' : 'Hamburguer Artesanal', 'Ativo' : False} ]
def exibe_nome_programa():
    print("""
----------------
𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
----------------\n""")
def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()


def voltar_ao_menu_principal():
    input("\nDigite uma tecla para retornar ao menu: ")

def exibir_opcao():   
    op_1 = print("""
    1. Cadastrar Restaurante.
    2. Listar Restaurante.
    3. Alterar Estado do Restaurante.  
    4. Sair.\n""")

def finalizar():
    os.system('cls')
    exibir_subtitulo("Finalizando o app!")

def opcao_invalida():
    print("Digite uma opção valida!")
    voltar_ao_menu_principal()
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    exibir_subtitulo("Opção Escolhida: (1) Cadastrar restaurante.")
    nome_restaurante = str(input("Digite o nome do Restaurante: "))
    categoria = input(f"Digite a Categoria do seu Restaurante ({nome_restaurante}) :")
    dados_restaurante ={'Nome' : nome_restaurante, 'Categoria' : categoria, 'Ativo': False}
    cadastro_r.append(dados_restaurante)
    os.system('cls')
    print(f"O Restaurante {nome_restaurante} foi cadastrado com sucesso.")
    voltar_ao_menu_principal()
    main()
    

def listar_restaurante():
    os.system('cls')
    exibir_subtitulo("Opção Escolhida: (2) Listar restaurante.")
    print(f' {'Nome Do Restaurante'.ljust(21)} | {'Categoria'.ljust(22)} | {'Status'}')

    for restaurante in cadastro_r:
        nome_restaurante = restaurante['Nome']
        categoria_restaurante = restaurante['Categoria']
        ativo_restaurante = restaurante['Ativo']
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(22)} | {ativo_restaurante}')
    voltar_ao_menu_principal()
    main()

def alterar_estado_restaurante():
    exibir_subtitulo('Opção Escolhida: (3) Alterar estado do restaurante.')
    nome_restaurante = input('Digite o Nome do Restaurante que deseja Alterar o Estado: ')
    restaurante_encontrado = False
    for restaurante in cadastro_r:
        if nome_restaurante == restaurante['Nome']:
            
            restaurante_encontrado = True
           
            restaurante['Ativo'] = not restaurante['Ativo']
            mensagem = f'O Restaurante {nome_restaurante} Foi Ativado!' if restaurante['Ativo'] else f'O Restaurante {nome_restaurante} Foi Desativado!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O Restaurante não foi encontrado!')

    voltar_ao_menu_principal()
    main()

   
def escolha_opcao():
    try:
        escolha =int(input('Escolha uma opção:\n '))


        if escolha == 1:
            cadastrar_novo_restaurante()
        elif escolha == 2:
            listar_restaurante()
        elif escolha == 3:
            alterar_estado_restaurante()
        elif escolha == 4:
            finalizar()

        else: 
            opcao_invalida()
           
    except:
        opcao_invalida()
        
        
def main():
    os.system('cls')
    exibe_nome_programa()
    exibir_opcao()
    escolha_opcao()

if __name__ == '__main__':
    main()