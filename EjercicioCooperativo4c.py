#Interes Compuesto

def InteresPrestamo(P,R,T):
    modulo = P*(1+R)**T
    return modulo
P=float(input("Capital inicial: "))
R=float(0.03) #Tasa de interes mensual en decimal
T=float(input("Tiempo en meses: ")) 
print("El monto final es: ",end="") 
print(InteresPrestamo(P,R,T))
