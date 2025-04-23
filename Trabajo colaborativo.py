KAPPA: float=9E+9 
def ley_coulomb (Q1,Q2,r): 
    modulo = KAPPA*Q1*Q2/r**2 
    return modulo 
carga1 = float(input("Carga1: ")) 
carga2 = float(input("Carga2: ")) 
distancia=float(input("Distancia entre cargas: ")) 
print("El modulo de la fuerza es: ",end="") 
print(ley_coulomb(carga1, carga2, distancia))