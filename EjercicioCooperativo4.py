#Cantidad de dinero faltante o sobrante

def CantidadCarne(B,P,M,H):
    modulo = B-(P*300 + M*3300+ H*350)
    return modulo
B=int(input("Cantidad de pesos del billete: "))
P=int(input("Numero de panes: "))
M=int(input("Numero de bolsas de leche: "))
H=int(input("Numero de huevos: "))

if(CantidadCarne(B,P,M,H)<0):
    print("La cantidad de dinero faltante es: " ,CantidadCarne(B,P,M,H))
if(CantidadCarne(B,P,M,H)>0):
    print("La cantidad de dinero sobrante es: " ,CantidadCarne(B,P,M,H))
