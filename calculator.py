 
#** 
# ! Function
# ? f1
# *

def taux_évolution_global():
    nmbr1 = int(input("Combien voulez vous d'évolution(s) ? \nDe 2 a 5 : "))
    test = 0
    while test == 0:
        if nmbr1 == 2:
            evo1 = float(input("Quel est la première évolution ? "))
            evo2 = float(input("Quel est la seconde évolution ? "))
            tevo1 = 1 + (evo1 / 100)
            tevo2 = 1 + (evo2 / 100)
            cm2 = tevo1 * tevo2
            t2 = cm2 - 1
            sevo1 = sens(evo1)
            sevo2 = sens(evo2)
            print("La première évolution est " + sevo1 + " et la seconde évolution est " + sevo2 + ".")
            return(round(t2,3))
            test = test +1
        elif nmbr1 == 3:
            evo1 = float(input("Quel est la première évolution ? "))
            evo2 = float(input("Quel est la seconde évolution ? "))
            evo3 = float(input("Quel est la troisième évolution ? "))
            tevo1 = 1 + (evo1 / 100)
            tevo2 = 1 + (evo2 / 100)
            tevo3 = 1 + (evo3 / 100)
            cm3 = tevo1 * tevo2 * tevo3
            t3 = cm3 - 1
            sevo1 = sens(evo1)
            sevo2 = sens(evo2)
            sevo3 = sens(evo3)
            print("La première évolution est " + sevo1 + ", la seconde évolution est " + sevo2 + " et la troisème évolution est " + sevo3 + ".")
            return(round(t3,3))
            test = test +1
        elif nmbr1 == 4:
            evo1 = float(input("Quel est la première évolution ? "))
            evo2 = float(input("Quel est la seconde évolution ? "))
            evo3 = float(input("Quel est la troisième évolution ? "))
            evo4 = float(input("Quel est la quatrième évolution ? "))
            tevo1 = 1 + (evo1 / 100)
            tevo2 = 1 + (evo2 / 100)
            tevo3 = 1 + (evo3 / 100)
            tevo4 = 1 + (evo4 / 100)
            cm4 = tevo1 * tevo2 * tevo3 * tevo4
            t4 = cm4 - 1
            sevo1 = sens(evo1)
            sevo2 = sens(evo2)
            sevo3 = sens(evo3)
            sevo4 = sens(evo4)
            print("La première évolution est " + sevo1 + ", la seconde évolution est " + sevo2 + " , la troisème évolution est " + sevo3 + " et la quatrième évolution est de " + sevo4 + ".")
            return(round(t4,3))
            test = test +1
        elif nmbr1 == 5:
            evo1 = float(input("Quel est la première évolution ? "))
            evo2 = float(input("Quel est la seconde évolution ? "))
            evo3 = float(input("Quel est la troisième évolution ? "))
            evo4 = float(input("Quel est la quatrième évolution ? "))
            evo5 = float(input("Quel est la cinquième evolution ? "))
            tevo1 = 1 + (evo1 / 100)
            tevo2 = 1 + (evo2 / 100)
            tevo3 = 1 + (evo3 / 100)
            tevo4 = 1 + (evo4 / 100)
            tevo5 = 1 + (evo5 / 100)
            cm5 = tevo1 * tevo2 * tevo3 * tevo4 * tevo5
            t5 = cm5 - 1
            sevo1 = sens(evo1)
            sevo2 = sens(evo2)
            sevo3 = sens(evo3)
            sevo4 = sens(evo4)
            sevo5 = sens(evo5)
            print("La première évolution est " + sevo1 + ", la seconde évolution est " + sevo2 + " , la troisème évolution est " + sevo3 + " , la quatrième évolution est de " + sevo4 + " et la cinquième évolution est de " + sevo5 + ".")
            return(round(t5,3))
            test = test +1
        else:
            print("Vérifier que le nombre saisit est bien contenus entre 2 et 5 et que c'est un nombre entier.")
    
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
    t = taux_évolution_global()
    print("\nLe taux d'évolution est aproximativement égale à " + str(t) + ", et en pourcentage " + str(t*100) + "%.\n")

#** 
# ? f4
# *

def taux_recipr(taux):
    try:
        cmr = 1/(1+(taux/100))
        tr = cmr - 1
        return (round(tr,3))
    except:
        print("En l’absence de précisions supplémentaires sur l’axiomatique utilisée, selon le second théorème de Gödel, la proposition est indécidables")

#** 
# ? Choix
# *

wdyw = input("\nQue souhaitez vous calculez ? Faites votre choix parmis les posibilité ci-dessous :\n\n1) taux d'évolution\n2) taux reciproque\n3) taux d'évolution puis taux reciproque\n4) taux d'évolution et taux reciproque\n\n")
if wdyw == "1":
    ter = taux() 
elif wdyw == "2":
    t1 = float(input("Faites le choix du premier coeficien multiplicateur (en pourcentage) : "))
    tr = taux_recipr(t1)
    print("\nLe taux reciproque est aproximativement à " + str(tr) + ", en pourcentage " + str(tr*100) + "%")
elif wdyw == "3":
    ter = taux()
    tr = taux_recipr(ter)
    print("\nLe taux reciproque est aproximativement à " + str(tr) + ", en pourcentage " + str(tr*100) + "%")
elif wdyw == "4":
    ter = taux()
    t1 = float(input("Faites le choix du premier coeficien multplicateur (en pourcentage) : "))
    tr = taux_recipr(t1)
    print("\nLe taux reciproque est aproximativement à " + str(tr) + ", en pourcentage " + str(tr*100) + "%")
else:
    print("Veuillez verifiez la saisie du bon numéro attribuer au(x) calcul(s) choisi(s).")