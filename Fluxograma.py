idade = int(input("Idade:"))
alfabetizado = input("Alfabetizado (s ou n):")

if idade < 16:
    print("Não pode votar")
elif idade >70:
    print("Voto Facultativo")
elif (idade<18):
    print("Voto Facultativo")
elif alfabetizado == "s" or alfabetizado == "s" or alfabetizado == "sim":
    print("Voto Obrigatório")
else:
    print("Voto Facultativo")
