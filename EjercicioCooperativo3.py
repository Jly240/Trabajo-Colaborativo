from math import pi

def AreaRectangulo(b,a):
    modulo = b*a
    return modulo
b=float(input("Base del rectangulo: "))
a=float(input("Lado del rectangulo: ")) 
print("El area del rectangulo es: ",end="") 
print(AreaRectangulo(b,a))

def AreaRectangulo2(b2,a2):
    modulo2 = b2*a2
    return modulo2
b2=float(input("Base del rectangulo 2: "))
a2=float(input("Lado del rectangulo 2: ")) 
print("El area del rectangulo 2 es: ",end="") 
print(AreaRectangulo2(b2,a2))

def AreaCirculo(pi,r):
    modulo3 = pi*r**2
    return modulo3
r=float(input("Radio del circulo: "))
pi= float(pi)
print("El area del circulo es: ",end="") 
print(AreaCirculo(pi,r))

def AreaCirculo2(pi,r2):
    modulo4 = pi*r2**2
    return modulo4
r2=float(input("Radio del circulo 2: "))
pi= float(pi)
print("El area del circulo es: ",end="") 
print(AreaCirculo2(pi,r2))

print("El area total de las figuras es: ", AreaRectangulo(b,a)+ AreaRectangulo2(b2,a2)+ AreaCirculo(pi,r)+ AreaCirculo2(pi,r2))