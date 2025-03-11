def registrar_notas():
    notas = []
    while True:
        try:
            entrada = input("digite a nota do aluno (ou 'fim' para encerrar): ")
            if entrada.lower() == 'fim':
                break

            nota = float(entrada)
            if 0 <= nota <=10:
                notas.append(nota)

            else:
                print("nota inválida. Digite um valor de 0 a 10.")

        except ValueError:
            print("Entrada inválida. Por favor digite um número ou 'fim.'")

            if notas:
                media = sum(notas) / len(notas)
                print(f"\nMédia da turma: {media:2f}")
                print(f"total de notas válidas registradas: {len(notas)}")

            else:
                print('nenhuma nota válida registrada')

registrar_notas()                             