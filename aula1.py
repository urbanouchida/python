print("hello world!")

#criando uma variavel no python
fruta = "melancia"
#imprimir a variavel
print(fruta)

#expressoes matematicas
print(2*3+3**2)

#funcao para dicionar uma pessoa a lista
def adicionar_pessoa(lista, nome, idade, profissao):
    pessoa = {"nome":nome, "idade":idade, "profissao":profissao}
    lista.append(pessoa)

#funcao para mostrar as pessoas da lista
def exibir_pessoa(lista):
    print("lista de pessoas cadastradas")
    for pessoa in lista:
        print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Profissao: {pessoa['profissao']}")

#lista para armazenar pessoas
pessoas = []

#adicionando pessoas em uma lista
adicionar_pessoa(pessoas, "Ana", 25, "Engenheira")
adicionar_pessoa(pessoas, "Bruno", 30, "Professor")
adicionar_pessoa(pessoas, "Carla", 22, "Medica")

#Exibir a lista de pessoas
exibir_pessoa(pessoas)