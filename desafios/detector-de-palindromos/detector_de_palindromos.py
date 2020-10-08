# Faz a leitura da frase e armazena na variavel word
word = input("Digite a palavra/frase: ")

# Substitui os espaços em brancos para string vazia(remove os espaços)
word = word.replace(' ', '')
# Coloca todo o texto para caixa baixa.
word = word.lower()
# Inverte a string word.
word_inverted = word[::-1]

# Compara a string invertida com a palavra original(em caixa baixa e sem espaços)
if (word_inverted == word):
    print("eh palindromo")
else:
    print("nao eh palindromo")
