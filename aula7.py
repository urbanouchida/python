def is_palindramo(texto):
    texto_limpo = ''.join(char.lower()
                          for char in texto
                          if char.isalnum())
    return texto_limpo == texto_limpo[:: -1]

frase = "A cara rajada da jararaca"
resultado = is_palindramo(frase)

if resultado == True:
    resposta = "sim"

else:
    resposta = "não"

    print(f"' {frase}' é um palindramo? {resposta}")