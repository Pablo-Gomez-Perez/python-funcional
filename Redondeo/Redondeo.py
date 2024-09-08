

# Actividad 4: Redondee al peso mas cercano


# Una persona ha comprado en una tienda los siguientes artídulos

# - 7 chicles a 80 centavos c/u
# - 3 cajas de cerillos a $1.26 c/u
# - 5 kilos de jabón a $18.45 c/u

# De esta transacción calcule:

# - Sub Total (Calculo de la operación)
# - Iva del 16%
# - total a pagar(Redondee al peso mas cercano).


"""
Calcular el sub total de los chicles
"""
def subTotalPorChicles(cantidad):
    return (cantidad,round(float(cantidad * 0.8),0))
  

#Calcular el subtotal por cajas de cerillos compradas
def subTotalPorCerillos(cantidad):
    return (cantidad,round(float(cantidad * 1.26),0))

def subTotalPorJabon(cantidad):
    return (cantidad, round(float(cantidad * 18.45),0))

def suma(Chicles,Cerillos,Jabon):
    return round(float(subTotalPorChicles(Chicles)[1] + subTotalPorCerillos(Cerillos)[1] + subTotalPorJabon(Jabon)[1]))

def calcularIva(valor):
    return (round(float(valor + (valor * 0.16))), round(float(valor * 0.16)))

def imprimirDetallesDeVenta(Chicles,Cerillos,Jabon):
    print("################## Detalles de compra #######################################\n")
    print("Chicles: " + str(subTotalPorChicles(Chicles)[0]) + " importe: " + str(subTotalPorChicles(Chicles)[1]))
    print("Cerillos: " + str(subTotalPorCerillos(Cerillos)[0]) + " Importe: " + str(subTotalPorCerillos(Cerillos)[1]))
    print("Jabon: " + str(subTotalPorJabon(Jabon)[0]) + " Importe: " + str(subTotalPorJabon(Jabon)[1]) + "\n")
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
    print("Sub Total: " + str(suma(Chicles,Cerillos,Jabon)) + "\n")
    print("Iva: " + str(calcularIva(suma(Chicles,Cerillos,Jabon))[1]))
    print("Gran total: " + str(calcularIva(suma(Chicles,Cerillos,Jabon))[0]))
    
    

#def suma():
    

def main():
    if __name__ == '__main__':
        
        print("\n\t===================================================================================\n")
        print("\t=====================        Nueva Compra            ==============================\n")
        print("\t===================================================================================\n")
        
        imprimirDetallesDeVenta(float(input("Cantidad de Chicles: ")),float(input("Cantidad de cerillos: ")),float(input("Cantidad de jabon: ")))
        
        if(int(input("\n Nueva compra ? 1)Si 0)No -> ")) == 1):
            main()
        else:
            exit(0);
                                
        
main()
