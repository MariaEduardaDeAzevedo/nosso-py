numero_candidato = int(input("Entre com o numero do candidato a vaga: "))

classificados = [2,8,9,10]
desclassificados = [1,3,4,5,6,7,11]

if numero_candidato in classificados:
    print("Aprovado!")

if numero_candidato in desclassificados:
    posicao = desclassificados.index(numero_candidato) + 1
    print(f"Número {posicao} na lista de espera.")
