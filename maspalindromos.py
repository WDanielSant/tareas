p = int(input("escriba un numero ... "))

#la funcion rot(e,j) para calcular r
def rot(e,j):
    lista2=[]
    #convertimos el input en cadena y separamos en una lista
    num=str(e)
    num1=len(num)
    for n in num:
        n=int(n)
        lista2.append(n)
    #permutamos hacia adelante (para hacerlo hacia atras
    # quitamos num1 de la resta) 
    k = num1-(j%num1)
    permuta=lista2[k:]+lista2[:k]
    #concatenamos la lista premutada y la volvemos valor int
    numper="".join(map(str,permuta))
    z=int(numper)
    
    return z
#la funcion pal(x) clasifica a x como palindromo o no, (usamosa rot)
def pal(x):
    v1=str(x)
    y=len(v1)
    lista1=[x]
    for i in range(0,y):
     z1=int(str(x)[i:(i+1)])
     a=rot(x,z1)*((-1)**i)    
     lista1.append(a)
     r = sum(lista1)
    
    #verificamos si r es palindromo
    #valor absoluto de r
    r=abs(r)
    cdn = str(r)
    temp = cdn.replace(" ","")

    if temp == temp[::-1]:
      return 1     
    else: 
      return 0

#generamos la lista de turbopalindromos
list3=[]
for i in range(1,p):
    if pal(i)!=0:
     list3.append(i)

print(list3)
print(len(list3))

