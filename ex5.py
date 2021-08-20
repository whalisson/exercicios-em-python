total = 0.0
cha4: int = 0
cha5 = 0
cha7 = 0
cha10 = 0
cha12 = 0
pessoas = 0

ncasas = int(input("Informe o numero de casas visitadas:"))

for contador in range(0, ncasas):
    print("Casa-",  ncasas)
    televisao = str(input("\nA televisão está ligada no momento?(S ou N):"))

    if televisao == 'S':
        canal = int(input("\nInforme o número da canal que a família assiste no momento(4, 5, 7, 10, 12):"))

        if canal == 4:
            pessoas = int(input("\nInforme a quantidade de pessoas vendo esse canal na casa: "))
            cha4 += pessoas
        if canal == 5:
            pessoas = int(input("\nInforme a quantidade de pessoas vendo esse canal na casa: "))
            cha5 += pessoas
        if canal == 7:
            pessoas = int(input("\nInforme a quantidade de pessoas vendo esse canal na casa: "))
            cha7 += pessoas
        if canal == 10:
            pessoas = int(input("\nInforme a quantidade de pessoas vendo esse canal na casa: "))
            cha10 += pessoas
        if canal == 12:
            pessoas = int(input("\nInforme a quantidade de pessoas vendo esse canal na casa: "))
            cha12 += pessoas

        total += pessoas
        print(f"A porcentagem de pessoas assistindo o canal 4 era de.:", cha4 / total * 100, "%")
        print(f"A porcentagem de pessoas assistindo o canal 5 era de.:", cha5 / total * 100, "%")
        print(f"A porcentagem de pessoas assistindo o canal 7 era de.:", cha7 / total * 100, "%")
        print(f"A porcentagem de pessoas assistindo o canal 10 era de:", cha10 / total * 100, "%")
        print(f"A porcentagem de pessoas assistindo o canal 12 era de:", cha12 / total * 100, "%")

    if televisao == 'N':
        print("\nObrigado pela atenção!")
