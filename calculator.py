 
#*
# ! Fonction :
# ? F1 = Calcul a partir des données fournie par l'utilisateur le coéf mutliplicateur, puis le taux d'évolution qu'il return
#*

def taux_et_coefmutlipli(x1, x2, x3):
    sx1 = sens(x1)
    sx2 = sens(x2)
    sx3 = sens(x3)
    print("La première évolution est " + sx1 + ", la seconde évolution est " + sx2 + " et enfin la troisème évolution est " + sx3 + ".")
    tx1 = 1 + (x1 / 100)
    tx2 = 1 + (x2 / 100)
    tx3 = 1 + (x3 / 100)
    cm = tx1 * tx2 * tx3
    t = cm - 1
    return (round(t,3))

#*
# ? F2 = Calcul le taux réciproque a partir d'un taux donné par l'utilisateur 
#*

def taux_recipr(t):
    try:
        tr = 1/tr
        return (round(tr,3))
    except:
        print("En l’absence de précisions supplémentaires sur l’axiomatique utilisée, selon le second théorème de Gödel, la proposition est indécidables")

#*
# ? F3 = Demande des évolutions et utilisation de la F1
#*

def t():
    x1 = float(input("\nEntrez la première évolution (en pourcentage) : "))
    x2 = float(input("\nEntrez la seconde évolution (en pourcentage) : "))
    x3 = float(input("\nEntrez la troisème évolution (en pourcentage) : "))
    t = taux_et_coefmutlipli(x1, x2, x3)
    print("\nLe taux d'évolution est aproximativement égale à " + str(t) + ", et en pourcentage " + str(t*100) + "%.\n")
    return (round(t,3))

#*
# ? F4 = Verifie si x(n) est une baisse, une hausse ou est nul
#*

def sens(x):
    if x > 0:
        return "une hausse"
    elif x < 0:
        return "une baisse"
    else:
        return "nulle"

#*
# ! Don des réponses 
#* wdyw = what do you whant
#*

wdyw = input("\nQue souhaitez vous calculez ? Faites votre choix parmis les posibilité ci-dessous :\n\n1) taux d'évolution\n2) taux reciproque\n3) taux d'évolution puis taux reciproque\n4) taux d'évolution et taux reciproque\n\n")
if wdyw == "1":
    ter = t() 
elif wdyw == "2":
    t1 = float(input("Faites le choix du premier coeficien multiplicateur (en pourcentage) : "))
    tr = taux_recipr(t1)
    print("\nLe taux reciproque est aproximativement à " + str(tr) + ", en pourcentage " + str(tr*100) + "%")
elif wdyw == "3":
    ter = t()
    tr = taux_recipr(ter)
    print("\nLe taux reciproque est aproximativement à " + str(tr) + ", en pourcentage " + str(tr*100) + "%")
elif wdyw == "4":
    t()
    t1 = float(input("Faites le choix du premier coeficien multplicateur (en pourcentage) : "))
    tr = taux_recipr(t1)
    print("\nLe taux reciproque est aproximativement à " + str(tr) + ", en pourcentage " + str(tr*100) + "%")
else:
    print("Veuillez verifiez la saisie du bon numéro attribuer au(x) calcul(s) choisi(s).")