 
#*
# ! Fonction :
# ? F1 = Calcul a partir des données fournie par l'utilisateur le coéf mutliplicateur, puis le taux d'évolution qu'il return
#*
 
def taux_et_coefmutlipli(x1, x2, x3):
    if x1 == 0 and x2 == 0 and x3 == 0:
        print("Toutes les évolutions sont nulle.")
    elif x1 < 0 and x2 < 0 and x3 < 0:
        print("Toutes les évolutions sont des baisse.")
    elif x1 > 0 and x2 > 0 and x3 > 0:
        print("Toutes les évolutions sont des hausse.")
    elif x1 < 0 and x2 < 0 and x3 == 0:
        print("Toutes les évolutions sont des baisse.")
    elif x1 > 0 and x2 > 0 and x3 == 0:
        print("Toutes les évolutions sont des hausse.")
    elif x1 < 0 and x2 > 0 and x3 == 0:
        print("La première évolutions est une baisse et la seconde est une hausse.")
    elif x1 > 0 and x2 < 0  and x3 == 0:
        print("La première évolutions est une hausse et la seconde est une baisse")
    elif x1 < 0 and x2 < 0 and x3 > 0:
        print("Seul les deux première évolutions sont des baisse, la troisème est une hausse.")
    elif x1 > 0 and x2 > 0 and x3 < 0:
        print("Seul les deux première évolutions sont des hausse, la troisème est une baisse.")
    elif x1 < 0 and x2 > 0 and x3 > 0:
        print("Seul les deux dèrnière évolutions sont des hausse, la première est une baisse.")
    elif x1 > 0 and x2 < 0 and x3 < 0:
        print("Seul les deux dèrnière évolutions sont des baisse, la première est une hausse.") 
    elif x1 > 0 and x2 < 0 and x3 > 0:
        print("La première évolution est une hausse, la seconde est une baisse et la troisième est une hausse") 
    elif x1 < 0 and x2 > 0 and x3 < 0:
        print("La première évolution est une baisse, la seconde est une hausse et la troisème est une baisse.")
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
        return (round(tr,3))

#*
# ? F3 = Demande des évolutions et utilisation de la F1
#*

def t():
    x1 = float(input("\nEntrez la première évolution (en pourcentage) : "))
    x2 = float(input("\nEntrez la seconde évolution (en pourcentage) : "))
    x3 = float(input("\nEntrez la troisème évolution (en pourcentage) : "))
    t = taux_et_coefmutlipli(x1, x2, x3)
    print("\nLe taux d'évolution est aproximativement égale à " + str(t) + ", et en pourcentage " + str(t*100) + "%")
    return (round(t,3))

#*
# ! Don des réponses 
#* wdyw = what do you whant
#*

wdyw = input("\nQue souhaitez vous calculez ? Faites votre choix parmis les posibilité ci-dessous :\n\n1) taux d'évolution\n2) taux reciproque\n3) taux d'évolution puis taux reciproque\n4) taux d'évolution et taux reciproque\n")
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