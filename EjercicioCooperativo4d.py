#Numero de contagiados de Covid-19

def NumeroContagiados(C,D):
    modulo = C*(2**D)
    return modulo
C=int(input("Numero de contagiados actuales: "))
D=int(input("Numero de dias a partir de hoy: ")) 
print(f"el numero de contagiados en NuncaLandia para el dia {D} es: ",end="") 
print(NumeroContagiados(C,D)) 