
sexo = 'M'
experiencia = 'S'
menorf = 9999
f21 = 0
hm45 = 0
idadefexp = 0
expf = 0
idademexp = 0
expm = 0
sexom = 0
sexof = 0
idadem = 0
idadef = 0
candidatos = int(input("Número de candidatos:"))

for contador in range(1,candidatos):
    print(f"Pessoa-", {candidatos})
    sexo = str(input("\nInforme seu sexo(M ou F): "))

    if(sexo == 'M'):
        sexom += 1
        idadem = int(input("Informe sua idade:"))
        idademexp += idadem
        experiencia = str(input("Possui experiencia (S ou N):"))

        if(idadem >= 45):
            hm45 += 1

        if(experiencia == 'S'):
            expm += 1

        else:
            idademexp -= idadem


    if(sexo == 'F'):
        sexof += 1
        idadef = int(input("Informe sua idade:"))
        idadefexp += idadef
        experiencia = str(input("Possui experiencia (S ou N):"))

        if(experiencia == 'S'):
            expf += 1

        if(idadef < 21):
            f21 += 1

        if(idadefexp < menorf):
            menorf = idadefexp

        else:
            idadefexp -= idadef


print(f"O número de candidatos do sexo masculino é: ", {sexom})
print("O fnúmero de candidatos do sexo feminino é.: ", {sexof})
if(sexom > 0):
    print(f"Idade média de homens com experiencia..........: ", {idademexp / expm})
print(f"A porcentagem de homens com mais de 45 anos é: ", {(hm45 / sexom) * 100}, "%")
print(f"O número de mulheres com idade inferior a 21 e com experiencia é: ", {f21})
if(menorf > 100):
    menorf = 0
print(f"A menor idade entre as mulheres que já têm experiência no serviço: ", {menorf})



