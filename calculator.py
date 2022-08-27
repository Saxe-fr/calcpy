from math import *
#EN Code
#** 
# ! Function
# ? f1
# *

def overall_evolution_rate():
    nmbr1 = int(input("How many evolution do you want ? "))
    try:
        cm = 1
        for i in range(2, nmbr1+2):
            taux = float(input("\nTaux n°" + str(i-1) + " ? "))
            cm = cm*(1+(taux/100))
        taux = cm-1
        a = sense(taux)
        print("\nYour evolution rate is " + a + ".")
        return(round(taux,3))
    except:
        print("Check that the number entered is well contained between 2 and 5 and that it is an integer.")
    
#** 
# ? f2
# *

def sense(x):
    if x > 0:
        return "a rise"
    elif x < 0:
        return "a drop"
    else:
        return "nul"

#** 
# ? f3
# *

def rate():
    try: 
        t = overall_evolution_rate()
        print("\nThe rate of evolution is approximately equal to " + str(t) + ", and in percentage " + str(round(t*100,3)) + "%.\n")
    except:
        print()

#** 
# ? f4
# *

def reciprocal_rate(taux):
    try:
        cmr = 1/(1+(taux/100))
        tr = cmr - 1
        return(round(tr,3))
    except:
        print("In the absence of additional details on the axiomatic used, according to Gödel's second theorem, the proposition is undecidable.") #Math joke

#**
#? f5
#*

def standard_deviation():
    N = int(input("How many variables do you have to process? \nChoose a number greater than two."))
    #Initialization :
    n = N    
    sum = 0
    ecrtyp = 0
    vrc = 0 
    vrct = 0
    l = []
    for n in range (n): 
        x = float(input("Enter the value of variable N°" + str(n+1) + " = "))
        sum = x + sum
        l.append(x)
    mean = sum / N
    for n in range (n):
        x = l[n]
        vrc = (x-mean)**2
        vrct = vrc + vrct
    ecrtyp2 = vrct / N
    ecrtyp = sqrt(ecrtyp2)

    print("The average of the values ​​µ es of " + str(mean))
    print("Varriance σ² is " + str(vrct))
    print("The standard deviation σ is equal to " + str(ecrtyp))

#** 
# ? Choix
# *

wdyw = input("\nWhat do you want to calculate? Choose from the options below: \n\n1) evolution rate\n2) reciprocal rate\n3) evolution rate then reciprocal rate\n4) evolution rate and reciprocal rate\n5) Standard deviation\n\n")
try:
    if wdyw == "1":
        ter = rate() 
    elif wdyw == "2":
        t1 = float(input("\nChoose the evolution rate (in percentage): "))
        tr = reciprocal_rate(t1)
        print("\nThe reciprocal rate is approximately" + str(tr) + ", in percentage " + str(tr*100) + "%")
    elif wdyw == "3":
        ter = rate()
        tr = reciprocal_rate(ter)
        print("\nThe reciprocal rate is approximately" + str(tr) + ", in percentage " + str(tr*100) + "%")
    elif wdyw == "4":
        ter = rate()
        t1 = float(input("Choose the evolution rate (in percentage): "))
        tr = reciprocal_rate(t1)
        print("\nThe reciprocal rate is approximately" + str(tr) + ", in percentage " + str(tr*100) + "%")
    elif wdyw == "5":
        standard_deviation()
    else:
        print("Please check that you have entered the correct number assigned to the chosen calculation(s).")
except:
    print("Source//, ERROR systeme; code-source try=false") #Juste error if you want