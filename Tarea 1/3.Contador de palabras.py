def contar_palabra(texto, palabra):
    return texto.lower().split().count(palabra.lower())

texto = "Este es un ejemplo de texto. Este texto tiene palabras repetidas."
palabra_buscada = "texto"

print(f"La palabra '{palabra_buscada} aparece {contar_palabra(texto, palabra_buscada)} veces.")