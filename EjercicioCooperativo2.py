from math import pi

def AreaRectangulo(b,a):
    modulo = b*a
    return modulo
b=float(input("Base del rectangulo: "))
a=float(input("Lado del rectangulo: ")) 
print("El area del rectangulo es: ",end="") 
print(AreaRectangulo(b,a))

def AreaCirculo(pi,r):
    modulo2 = pi*r**2
    return modulo2
r=float(input("Radio del circulo: "))
pi= float(pi)
print("El area del circulo es: ",end="") 
print(AreaCirculo(pi,r))

print("El area total de las figuras es: ", AreaRectangulo(b,a)+ 2*AreaCirculo(pi,r))