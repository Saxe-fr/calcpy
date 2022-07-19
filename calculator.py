 
#*
# ! Fonction :
# ? F1 = Calcul à partir des données fournies par l'utilisateur le coéf mutliplicateur, puis le taux d'évolution qu'il return
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
# ? F2 = Calcul le taux réciproque à partir d'un taux donné par l'utilisateur 
#*

def taux_recipr(t, t2):
    if t > 0:
        cmr = 1/(1+(t/100))
        tr = cmr - 1
    else :
        t = t * -1
        cmr = 1/(1-(t/100))
        tr = cmr - 1
        return (round(tr,3))

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
        return "nul"


#*
# ! Don des réponses 
#* wdyw = what do you whant
#*

wdyw = input("\nQue souhaitez vous calculer ? Faites votre choix parmis les posibilités ci-dessous :\n\n1) taux d'évolution\n2) taux réciproque\n3) taux d'évolution puis taux réciproque\n4) taux d'évolution et taux réciproque\n\n")
if wdyw == "1":
    ter = t() 
elif wdyw == "2":
    t1 = float(input("Faites le choix du coeficient multiplicateur (en pourcentage) : "))
    tr = taux_recipr(t1)
    print("\nLe taux réciproque est aproximativement à " + str(tr) + ", en pourcentage " + str(tr*100) + "%")
elif wdyw == "3":
    ter = t()
    tr = taux_recipr(ter)
    print("\nLe taux réciproque est aproximativement à " + str(tr) + ", en pourcentage " + str(tr*100) + "%")
elif wdyw == "4":
    t()
    t1 = float(input("Faites le choix du coeficient multplicateur (en pourcentage) : "))
    tr = taux_recipr(t1)
    print("\nLe taux réciproque est aproximativement à " + str(tr) + ", en pourcentage " + str(tr*100) + "%")
else:
    print("Veuillez vérifier la saisie du bon numéro attribué au(x) calcul(s) choisi(s).")