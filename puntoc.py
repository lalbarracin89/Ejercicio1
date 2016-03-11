#Los factores primos en 13195 son 5, 7, 13 y 29 Cual es el factor primo mas grande en el numero 600851475143 
num=100

limite=num/2
lista=range(1,limite+1)
i=0
listaimpar=[]

#obtener lista de numero impares
while i<limite:
    if lista[i]%2 and num%lista[i]==0:
	    listaimpar.append(lista[i])
    i=i+1
    
print(listaimpar)
	
#recorrer vector desde atras

print(listaimpar)
flag=1
i=-1

while flag:
	contador=0
	for j in range(3, (listaimpar(i)/2)+1)
		if listaimpar%i=0:
			break
		flag=0
	i-=
