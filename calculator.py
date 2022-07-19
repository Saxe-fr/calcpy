 
#*
# ! Fonction :
# ? F1 = Calcul a partir des données fournie par l'utilisateur le coéf mutliplicateur, puis le taux d'évolution qu'il return
# ? Il affiche quel évolution est une hausse, une baisse ou est nulle parmis celle fournis par l'utilisateur
#*
 
def taux_et_coefmutlipli(x1, x2, x3):
    if x1 > 0 and x2 > 0 and x3 > 0:
        print("Toutes les évolution données sont des hausse.")
    elif x1 < 0 and x2 < 0 and x3 < 0:
        print("Toutes les évolution données sont des baisse.")
    elif x1 == 0 and x2 == 0 and x3 == 0:
        print("Cette demande n'a aucun interêt... J'ai beau avoir été programmer, sachez que c'est blessant de me voir donnée une tache si innutile, alors si vous pouviez la prochaine fois choisir des évolution non nulle se serait respectueux a mon égard, merci.") #text d'aucune utilité
    else:
        print()
    tx1 = 1 + (x1 / 100)
    tx2 = 1 + (x2 / 100)
    tx3 = 1 + (x3 / 100)
    cm = tx1 * tx2 * tx3
    t = cm - 1
    return (round(t,3))

#*
# ? F2 = Calcul le taux réciproque a partir d'un taux donné par l'utilisateur 
#*

def taux_recipr(t, t2):
    if t > 0:
        cmr = 1/(1+(t/100))
        tr = cmr - 1
    else :
        t = t * -1
        cmr = 1/(1-(t/100))
        tr = cmr - 1
    try:
        if t2 > 0:
            cmr2 = 1/(1+(t2/100))
            tr2 = cmr2 - 1
        else :
            t2 = t2 * -1
            cmr2 = 1/(1-(t2/100))
            tr2 = cmr2 - 1
    except:
        tr2 = 0
    if tr2 == 0:
        return (tr)
    else:
        tr3 = tr + tr2
        tr = tr3
        return (round(tr,3))

#*
# ? F3 = Demande des évolutions et utilisation de la F1
#*

def t():
    x1 = float(input("\nEntrez la première évolution (en pourcentage) : "))
    x2 = float(input("\nEntrez la seconde évolution (en pourcentage) : "))
    x3 = float(input("\nEntrez la troisème évolution (en pourcentage) : "))
    t = taux_et_coefmutlipli(x1, x2, x3)
    print("\nLe coeficien multiplicateur est aproximativement égale à " + str(t) + ", et en pourcentage " + str(t*100) + "%")
    return (round(t,3))

#*
# ! Don des réponses 
#* 

wdhw = input("\nQue souhaitez vous calculez ? Faites votre choix parmis les posibilité ci-dessous :\n\n1) taux multiplicateur\n2) taux reciproque\n3) taux multiplicateur puis taux reciproque\n4) taux multiplicateur et taux reciproque\n")
if wdhw == "1":
    ter = t() 
elif wdhw == "2":
    t1 = float(input("Faites le choix du premier coeficien multiplicateur (en pourcentage) : "))
    t2 = float(input("Faites le choix du second coeficien multiplicateur (en pourcentage) : "))
    tr = taux_recipr(t1, t2)
    print("\nLe taux reciproque est aproximativement à " + str(tr) + ", en pourcentage " + str(tr*100) + "%")
elif wdhw == "3":
    ter = t()
    t2 = float(input("Faites le choix du second coeficien multplicateur (en pourcentage) : "))
    tr = taux_recipr(ter, t2)
    print("\nLe taux reciproque est aproximativement à " + str(tr) + ", en pourcentage " + str(tr*100) + "%")
elif wdhw == "4":
    t()
    t1 = float(input("Faites le choix du premier coeficien multplicateur (en pourcentage) : "))
    t2 = float(input("Faites le choix du second coeficien multplicateur (en pourcentage) : "))
    tr = taux_recipr(t1, t2)
    print("\nLe taux reciproque est aproximativement à " + str(tr) + ", en pourcentage " + str(tr*100) + "%")
else:
    print("Veuillez verifiez la saisie du bon numéro attribuer au(x) calcul(s) choisi(s).")