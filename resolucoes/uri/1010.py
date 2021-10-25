entrada1 = input().split()
entrada2 = input().split()

produto1 = int(entrada1[1]) * float(entrada1[2])
produto2 = int(entrada2[1]) * float(entrada2[2])

soma = produto1 + produto2
print("VALOR A PAGAR: R$ %.2f" %soma)
