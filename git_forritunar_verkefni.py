def daemi1():
    tala1 = int(input("Sláðu inn tölu [1]: "))
    tala2 = int(input("Sláðu inn tölu [2]: "))
    print("Tölurnar lagðar saman: ", tala1 + tala2)
    print("Tölurnar margfaldaðar: ", tala1 * tala2)

def daemi2():
    fornafn = str(input("Fornafn?: "))
    eftirnafn = str(input("Eftirnafn?: "))
    print("Halló", fornafn, eftirnafn)

def daemi3():
    texti = str(input("Sláðu inn texta: "))
    lagstafir = 0
    hastafir = 0
    teljari = 0
    ha_undan_la = 0
    for stafur in texti:
        if stafur.lower() == stafur:
            lagstafir += 1
            if teljari == 1:
                ha_undan_la += 1
                teljari = 0
        elif stafur.upper() == stafur:
            hastafir += 1
            teljari += 1
    print("Í þessum texta eru", hastafir, "hástafir,", lagstafir, "lágstafir og", ha_undan_la, "lágstafir koma strax eftir hástaf")

valmynd = 1
while(valmynd == 1):
    print("\n-------------------")
    print("  [1] fyrir dæmi1  ")
    print("  [2] fyrir dæmi2  ")
    print("  [3] fyrir dæmi3  ")
    print("-------------------")
    val = int(input("Hvað velurðu?[1-3]: "))
    if val == 1:
        print("Þú hefur valið að keyra dæmi 1.")
        daemi1()

    elif val == 2:
        print("Þú hefur valið að keyra dæmi 2.")
        daemi2()

    elif val == 3:
        print("Þú hefur valið að keyra dæmi 3.")
        daemi3()

    else:
        print("Ekki á milli 1-3..")