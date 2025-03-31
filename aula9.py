#Função para obter a cotação da moeda atual
import requests 
from datetime import datetime
 
 #Função principal para integrar c a api e mostrar o valor da moeda na cotação atual
 #Função main para interagir c o script (input)
 
def obter_cotacao(moeda):
   url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
   try: 
     response = requests.get(url)
     response.raise_for_status()
     dados = response.json()
     cotacao = dados[f"{moeda}BRL"]
     return f"""
     Moeda: {moeda} para BRL
     Valor: R$ {float(cotacao['bid']):.2f}
     Máxima: R$ {float(cotacao['high']):.2f}
     Mínima: R$ {float(cotacao['low']):.2f}
     Data/Hora: {datetime.fromtimestamp(int(cotacao['timestamp']))} 
     """
   except requests.RequestException as e: 
     return f"Erro ao obter cotação: {e}"
   except KeyError:
     return "Moeda não encontrada ou suportada"
   
def main():
   moeda = input("Digite o valor da moeda para cotação (ex: USD, EUR, GBP): ").upper()
   print("\nObtendo cotação...")
   resultado = obter_cotacao(moeda)
   print(resultado)
 
if __name__ == "__main__":
     main()