sexo = input ("Qual seu sexo? \n 1 - Para Homem \n 2 - Para Mulher \n")
altura = input ("Qual sua altura? \n")

if sexo == '1':
    calc = (72.7*float(altura))-58
    print (f"Seu peso ideal seria {round(calc, 1)}")
elif sexo == '2':
    calc = (62.1*float(altura))-44.7
    print (f"Seu peso ideal seria {round(calc, 1)}")
else:
    print("Ops... Algo deu errado, tente novamente!")

