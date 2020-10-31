t = int(input()) # t recebe o número de casos de teste

for e in range(n):
	a, b = input().split() # Lê uma string a e uma string b
	num_operacoes = 0 # Contador que vai guardar a quantidade de operações realizadas
	
	for i in range(len(a)): # For para iterar cada letra da string a 
		
		
		x = ord(a[i]) # A função ord retorna o unicode da letra
		y = ord(b[i]) 
		
		while x != y: # Enquanto o unicode da letra i da string a não for igual ao da letra i da string b na mesma posição 
					  # esse unicode é incrementado em 1 até que seja igual ao unicode da letra i da string b
					  
			x += 1 # Incremento do unicode
			num_operacoes += 1 # Incremento do numero de operações
			
			if x > ord("z"): # Se o unicode for maior que o unicode de "z" então é porque ele passou da letra "z"
							 # e deve voltar para a letra "a"
				x = ord("a")
				
	print(num_operacoes) # Imprime o número de operações
	

