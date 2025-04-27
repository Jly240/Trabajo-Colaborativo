from math import pi

def VolumenEsfera(k,pi,r):
    modulo = k*pi*r**3
    return modulo
r=float(input("Radio de la esfera: ")) 
k= float(4/3)
pi= float(pi)
print("El volumen de la esfera es: ",end="") 
print(VolumenEsfera(k,pi,r))

def VolumenCono(k2,pi,r2,h):
    modulo2 = k2*pi*(r2**2)*h
    return modulo2
r2=float(input("Radio del cono: "))
h=float(input("Altura del cono: ")) 
k2= float(1/3)
pi= float(pi)
print("El volumen del cono es: ",end="") 
print(VolumenCono(k2,pi,r2,h))

print("El volumen total de las figuras es: ", VolumenEsfera(k,pi,r)+VolumenCono(k2,pi,r2,h))