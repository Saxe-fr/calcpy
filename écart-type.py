from math import *

def écart_type():
    N = int(input("Nombre de variable : "))
    #x = float(input("Multiplicatif des variable : "))
    n = N
    Σ = 0
    σ = 0
    vrc = 0
    vrct = 0
    l = []

    for n in range (n):
        x = float(input("Variable N°" + str(n + 1) + " = "))
        Σ = x + Σ
        l.append(x)

    µ = Σ / N

    for n in range (n):
        x = l[n]
        vrc = ((x - µ)**2)
        vrct = vrc + vrct
    
    σ2 = vrct / N
    σ = sqrt(σ2)

    print("La moyenne des de " + str(µ))
    print("La varriance est de " + str(vrct))
    print("L'écart type σ est égale a " + str(σ))


écart_type()