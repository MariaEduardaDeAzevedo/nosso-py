w=input().split(" ")
count=0
media=0
while(int(w[0])!=0 and int(w[1])!=0 and int(w[2])!=0):

    count=count+1
    rm1=int(w[0])*(1+int(w[2])/30)
    rm2=int(w[1])*(1+int(w[2])/30)

    rm=(rm1+rm2)/2
    media=media+rm

    if (1 <= rm < 13):
        print("Nao vai da nao")
    if (13 <= rm < 14):
        print("E 13")
    if (14 <= rm < 40):
        print("Bora, hora do show! BIIR!")
    if (40 <= rm <= 60):
        print("Ta saindo da jaula o monstro!")
    if (60 < rm):
        print("AQUI E BODYBUILDER!!")

    w=input().split(" ")
if(media/count>=40):
    print("\nAqui nois constroi fibra rapaz! Nao e agua com musculo!")