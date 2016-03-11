fib1=0
fib2=1
suma=0
while fib2<1000000:
    if fib1%2:
        suma=suma+fib1
    aux=fib1+fib2
    fib1=fib2
    fib2=aux
if fib1%2:
    suma=fib1+suma
print suma

