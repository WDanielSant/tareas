x = int(input("ingrese un numero mayor a 3 ... "))
y = 1
z = 1
a = 1
b = z+a
list=[1,1,2]
fibo=[1,1]
while b<x:
 z=a
 a=b
 b=z+a
 if (b %2) == 1:
     fibo.append(b)
 list.append(b)
print(sum(fibo))
