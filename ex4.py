valor = float(input("Informe o valor de seu carro:"))
opcao = 0
while opcao != 3:
    print("""Menu
    1. À vista
    2. Tabela
    3. Sair""")
    opcao = int(input("Escolha sua opção:"))

    if opcao == 1:
        valoravista = valor - valor * 1 / 5
        print(f"O valor à vista é:", valoravista)
    if opcao == 2:
        opcaoparcelas = int(input("Escolha o número de parcelas (6, 12, 18, 24, 30, 36, 42, 48, 54 e 60): "))
        if opcaoparcelas == 6 or opcaoparcelas == 6 or opcaoparcelas == 12 or opcaoparcelas == 18 or opcaoparcelas == 24 or opcaoparcelas == 30 or opcaoparcelas == 36 or opcaoparcelas == 42 or opcaoparcelas == 48 or opcaoparcelas == 54 or opcaoparcelas == 60:
            if opcaoparcelas == 6:
                valor *= 1.03
            if opcaoparcelas == 12:
                valor *= 1.06
            if opcaoparcelas == 18:
                valor *= 1.09
            if opcaoparcelas == 24:
                valor *= 1.12
            if opcaoparcelas == 30:
                valor *= 1.15
            if opcaoparcelas == 36:
                valor *= 1.18
            if opcaoparcelas == 42:
                valor *= 1.21
            if opcaoparcelas == 48:
                valor *= 1.24
            if opcaoparcelas == 54:
                valor *= 1.27
            if opcaoparcelas == 60:
                valor *= 1.30
            print(f"O valor do carro parcelado é:", {valor})
        else:
            print("Opção de parcelamento inválida")
