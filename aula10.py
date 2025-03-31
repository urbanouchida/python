#Função para obter um usuario aleatorio consultando a API
import requests
 
def obter_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    try: 
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()['results'][0]
        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']
        return f"Nome: {nome}\nEmail: {email}\País: {pais}"
     
    except requests.RequestException as e:
        return f"Erro ao obter usuário aleatório: {e}"
     
def main():
    print("Gerando um usuário aleatório...")
    usuario = obter_usuario_aleatorio()
    print(usuario)
 
if __name__ == "__main__":
    main()