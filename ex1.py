totali3 = 0
opiniao = 0
op1 = 0
op2 = 0
op3 = 0
idade = 0
for contador in range (1,15):
    print(f"\nEspectador-",{contador})
    idade = int(input("Qual é a sua idade?:"))
    opiniao = int(input("O que achou do filme? (ótimo - 3; bom - 2; regular - 1):"))
    if(opiniao == 3):
        totali3 += idade
        op3 += 1

    if(opiniao == 1):
        op1+=1

    if(opiniao == 2):
        op2+=1


print(f"A média das idades das pessoas que responderam ótimo:",{totali3/op3})
print(f"A quantidade de pessoas que responderam regular: ", {op1})
print(f"A percentagem de pessoas que responderam bom, entre todos os espectadores analisados: ", {(op2/15) *100})
