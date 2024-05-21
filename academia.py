#em construção
def menu():
    menu = """
    ********** BEM VINDO A ACADEMIA **********
    1 - Ver planos
    2 - Cadastro
    3 - Login
    4 - Sair
    """
    return input(menu)

def ver_planos():
    print("""
            [1] Diária - R$39,90
            [2] Mensal - R$129,90
            [3] Trimestral - R$100,00          
          """)


def cadastrar(usuarios):
    cpf = input("Informe o CPF (somento números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nEsse CPF já está cadastrado!")
        return
    
    else:
        nome = input("Insira o nome completo: ")
        data_nascimento = input("Insira a data de nascimento (dd-mm-aaaa): ")
        ver_planos()
        plano = input("Informe o plano desejado: ")

        if plano == "1":
            plano == "Diário"
        elif plano == "2":
            plano == "Mensal"
        elif plano == "3":
            plano == "Trimestral"
        else:
            print("Opção invpalida")

        forma_pagamento = input("Escolha a forma de pagamento:\n1 - Cartão de Crédito\n2 - Pix\n3 - Boleto")

        if forma_pagamento == "1":
            forma_pagamento == "Cartão de Crédito"
        elif forma_pagamento == "2":
            forma_pagamento == "Pix"
        elif forma_pagamento == "3":
            forma_pagamento == "Boleto\n"
        else:
            print("Opção inválida.")
            

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "forma_pagamento": forma_pagamento, "plano": plano})

        print("Usuário criando com sucesso, agora você EXISTE NO SISTEMA meu amigo.")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def listar_usuarios(usuarios):
    for usuario in usuarios:
        linha = f"""
                    Nome:\t{usuario['nome']}
                    CPF:\t{usuario['cpf']}
                    Forma de pagamento:\t{usuario['forma_pagamento']}
                    Plano:\t
                """
        print("=" * 100)
        print(linha)


def main():

    usuarios = []

    while True:
        opcao = menu()

        if opcao == "1":
            ver_planos()

        elif opcao == "2":
            cadastrar(usuarios)

main()
