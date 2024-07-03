"""
Desafio

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco
deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira
versão do sistema, devemos implementar apenas 3 operações: saque, depósito e extrato.


----OPERAÇÃO DE DEPÓSITO

Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação extrato.

----OPERAÇÃO DE SAQUE

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saque devem ser armazenados em uma variável e exibidos na operação de extrato.

---OPERAÇÃO DE EXTRATO

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.

Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45

"""


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Informe o valor que deseja depositar: "))

        if valor_deposito > 0:
            saldo = saldo + valor_deposito
            extrato = extrato + f"Depósito: R$ {valor_deposito:.2f}\n"

        else:
            print("Falha na operação. O valor de depósito informado é inválido.")


    elif opcao == "s":
        if saldo > 0:
            valor_saque = float(input("Informe o valor que deseja sacar: "))

            if valor_saque > saldo:
                print("Operação falhou! Você não possui saldo suficiente.")

            elif valor_saque > limite:
                print("Operação falhou. O valor que deseja sacar excede o limite.")

            elif numero_saques >= LIMITE_SAQUES:
                print("Operação falhou! Você já excedeu seu número diário de saques.")

            elif valor_saque > 0:
                saldo = saldo - valor_saque
                extrato = extrato + f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques = numero_saques + 1

        else:
            print("Operação falhou! O valor informado é inválido.")
        

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
