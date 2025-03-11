#Desafio

#Criar uma calculadora para realizar operações básicas de matemática

#Requisitos:

#1 - As operações matemática deve ser realizada entre dois números
#2 - As operações básicas são: adição, multiplicação, divisão e subtração 
#3 - O programa deve tratar entradas inválidas

def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número"))
            num2 = float(input("Digite o segundo número"))
            operacao = input("Digite a operação(+,-,*,/):")

            if operacao =='+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao =='*':
                resultado = num1 * num2
            elif operacao =='/':
                resultado = num1 / num2
            else:
                raise ValueError

            print(f"Resultado:{resultado}")
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente")
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitido. Tente novamente")

calculadora()            

