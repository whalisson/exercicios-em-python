total = 0
idade = 0
r_olho_n_a = 0
olhoa = 0
idadeal = 0
pkgal = 0
altura = 0
for contador in range(1, 6):
    print(f"Pessoa", {contador})
    idade = int(input('Digite a sua idade:'))

    peso = float(input("Digte seu peso(em kg ultilizando ponto):"))
    altura = float(input("Digite sua altura(em m ultilizando ponto):"))
    cabelo = str(input("Informe a cor do seu cabelo (P - preto; C - castanho; L -louro; e R - ruivo):"))
    olho = str(input("Informe a cor do seu olho(A - azul; P -preto; V - verde; e C - castanho):"))

    if idade > 50 and peso < 60:
        pkgal += 1

    if altura < 1.5:
        idadeal += 1
        total += idade

    if olho == 'A':
        olhoa += 1

    if cabelo == 'R' and olho != 'A':
        r_olho_n_a += 1

print(f"A quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 kg:", {pkgal})
print(f"A média das idades das pessoas com altura inferior a 1,50 m: ", {total / idadeal})
print(f"A porcentagem de pessoas com olhos azuis entre todas as pessoas analisadas: ", {olhoa / 6 * 100})
print(f"A quantidade de pessoas ruivas e que não possuem olhos azuis:", {r_olho_n_a})
