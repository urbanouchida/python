temp = float(input("digite a temperatura: "))
origem = input("digite a unidade de origem (C, F ou K):").upper()
destino = input("digite a unidade de destino(C, F ou K):").upper()

if origem == destino:
    resultado = temp
elif origem == "C":
    if destino == "F":
        resultado = (temp *9/5) + 32
    else: #Kelvin
        resultado = temp + 273.15

elif origem == "F":
    if destino == "C":
        resultado = (temp -32) * 5/9
    else: #Kelvin
        resultado = (temp -32) * 5/9 + 273.15  
else: #Kelvin
    if destino == "C":
        resultado = temp -273.15
    else: #Fahrenheit
        resultado = (temp - 273.15) * 9/5 + 32

print(f"{temp} {origem} é igual a {resultado:.2f} {destino}")                                            