def xCuadrado(x,y):
    z = x**y
    print(f"Este es el resultado de la funcion",z)
    return z
xCuadrado (2,4)

def AreaDelCirculo(R):
    a= 3.141592*(R)**2
    print(f"Este es el resultado de la funcion",a)
    return a
AreaDelCirculo (10)

def AreaRectangulo(b,c):
    d = b*c
    return d

b = float(input("Largo del rectangulo: "))
c = float(input("Ancho del rectangulo: "))
print("El area del rectangulo es: ", end= " ")
print(AreaRectangulo (b,c))





