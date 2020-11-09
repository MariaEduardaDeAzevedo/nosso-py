# lê novos valores enquanto não houver EOF
while True:
    try:
        # n sempre ímpar
        n = int(input())
        for i in range(n):
            # imprime metade das n-iterações
            if (not(int((n+1)/2) == i)):
                # imprime n-1 espaços antes e os asteriscos depois
                print(' ' * (n - i),'*' * (2*i+1))
                # quantos asteriscos foram imprimidos
                # print(' ' * (n - i),'*' * (2*i+1), (2*i+1))
            else:
                break
        # imprime a base da árvore (sempre 1 -> 3)
        for k in range(2):
                print(' ' * (n - k),'*' * (2*k+1))
    except EOFError:
        exit()