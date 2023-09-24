saldo = 0.0
limite_diario_saque = 3
extrato = ""
sair_do_sistema = False
escolha = 0

def mostrar_menu():
    menu = """

        Bem vindo à Dio Bank

        1 - deposito
        2 - saque
        3 - extrato
        4 - sair

        """
    print(menu)
    numero_operacao = receber_numero_de_escolha()
    escolher_operacao(numero_operacao)    

def mostrar_mensagem_de_despedida():
    print(f"Muito obrigado por acessar a Dio Bank! tenha uma excelente semana S2")

def receber_numero_de_escolha():
    global sair_do_sistema

    numero_str = input("Por favor, selecione uma opção: ")
    numero_int = int(numero_str)

    if numero_int == 4:
        sair_do_sistema = True

    return numero_int

def escolher_operacao(numero):
    global sair_do_sistema

    if (numero == 1):
        valor_str = input("Informe o valor de depósito: ")
        valor_float = float(valor_str)
        depositar(valor_float)
    elif (numero == 2):
        valor_str = input("Informe o valor de saque: ")
        valor_float = float(valor_str)
        sacar(valor_float)
    elif (numero == 3):
        imprimir_extrato()
    elif (numero == 4):
        mostrar_mensagem_de_despedida()
        sair_do_sistema = True

def depositar(valor):
    global saldo

    valor_float = float(valor)

    if(valor_float >= 0):
        saldo += valor_float

def sacar(valor):
    global saldo
    global limite_diario_saque

    if(saldo < valor):
        print("Não há saldo suficiente")
    elif limite_diario_saque == 0:
        print("Limite diário de operações de saque já foi atingido")
    elif valor >=  500.0:
        print("Valor superior ao limite de saque permitido")
    else:
        saldo -= valor
        limite_diario_saque -= 1

def imprimir_extrato():
    global saldo
    print(f"Saldo atual de R$ {saldo:.2f}")

try:

    while (not sair_do_sistema):
        mostrar_menu()

except:
   print("Favor verificar os dados de entrada")