from math import *
#FR Code
#**
# ! Function
# ? f1
# *

def taux_évolution_global():
    nmbr1 = int(input("Combien voulez vous d'évolutions ? "))
    try:
        cm = 1
        for i in range(2, nmbr1+2):
            taux = float(input("\nTaux n°" + str(i-1) + " ? "))
            cm = cm*(1+(taux/100))
        taux = cm-1
        a = sens(taux)
        print("\nVotre taux d'évolution est " + a + ".")
        return(round(taux,3))
    except:
        print("Vérifier que le nombre saisit est bien contenu entre 2 et 5 et que c'est un nombre entier.")
    
#** 
# ? f2
# *

def sens(x):
    if x > 0:
        return "une hausse"
    elif x < 0:
        return "une baisse"
    else:
        return "nulle"

#** 
# ? f3
# *

def taux():
    try: 
        t = taux_évolution_global()
        print("\nLe taux d'évolution est aproximativement égale à " + str(t) + ", et en pourcentage " + str(round(t*100,3)) + "%.\n")
    except:
        print()

#** 
# ? f4
# *

def taux_recipr(taux):
    try:
        cmr = 1/(1+(taux/100))
        tr = cmr - 1
        return(round(tr,3))
    except:
        print("En l’absence de précisions supplémentaires sur l’axiomatique utilisée, selon le second théorème de Gödel, la proposition est indécidable.") #Blague de mathématicien

#**
# ? F5
# *

def écart_type():
    N = int(input("Quel est le nombre de variable que vous avez a traitez ? \nChoissisez un nombre superieur a deux. "))
    #Initialisation :
    n = N    
    somme = 0
    ecrtyp = 0
    vrc = 0 
    vrct = 0
    l = []
    for n in range (n): 
        x = float(input("Entrer la valeur de la variable N°" + str(n+1) + " = "))
        somme = x + somme
        l.append(x)
    moyenne = somme / N
    for n in range (n):
        x = l[n]
        vrc = (x-moyenne)**2
        vrct = vrc + vrct
    ecrtyp2 = vrct / N
    ecrtyp = sqrt(ecrtyp2)

    print("La moyenne des valeur µ es de " + str(moyenne))
    print("La varriance σ² est de " + str(vrct))
    print("L'écart type σ est égale a " + str(ecrtyp))

#** 
# ? Choix
# *

wdyw = input("\nQue souhaitez vous calculer ? Faites votre choix parmis les posibilités ci-dessous :\n\n1) taux d'évolution\n2) taux reciproque\n3) taux d'évolution puis taux reciproque\n4) taux d'évolution et taux reciproque\n5) l'écart type\n\n")
try:
    if wdyw == "1":
        ter = taux() 
    elif wdyw == "2":
        t1 = float(input("\nFaites le choix du taux d'évolution (en pourcentage) : "))
        tr = taux_recipr(t1)
        print("\nLe taux reciproque est approximativement à " + str(tr) + ", en pourcentage " + str(tr*100) + "%")
    elif wdyw == "3":
        ter = taux()
        tr = taux_recipr(ter)
        print("\nLe taux reciproque est approximativement à " + str(tr) + ", en pourcentage " + str(tr*100) + "%")
    elif wdyw == "4":
        ter = taux()
        t1 = float(input("Faites le choix du taux d'évolution (en pourcentage) : "))
        tr = taux_recipr(t1)
        print("\nLe taux reciproque est approximativement égale à " + str(tr) + ", en pourcentage " + str(tr*100) + "%")
    elif wdyw == "5":
        écart_type()
    else:
        print("Veuillez verifier la saisie du bon numéro attribué au(x) calcul(s) choisi(s).")
except:
    print("Source//, ERROR systeme; code-source try=false") #Juste erreur si vous voulez