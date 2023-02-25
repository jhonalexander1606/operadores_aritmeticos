# programa para imlementar operadores aritmeticos 

print("---------------------------------")
print("----operadores aritmeticos-------")
print("---------------------------------")

#input

x = int(input("digite el valor de x: "))
y = int(input("digite el valor de y: "))


# procesing

s = x + y
r = x - y 
m = x * y
d = x / y
mod = x % y
de = x // y
p = x ** y

# output
 
print("------------------------------")
print("---------RESULTADOS-----------")
print("------------------------------")
print("suma: " + str(s))
print("Resta: " + str(r))
print("Multiplicacion: " + str(m))
print("Divison: " + str(d))
print("modulo: " + str(mod))
print("division entera: " + str(de))
print("potencia: " + str(p))