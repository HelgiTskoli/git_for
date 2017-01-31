def daemi1():
    tala1 = int(input("Sláðu inn tölu [1]: "))
    tala2 = int(input("Sláðu inn tölu [2]: "))
    print("Tölurnar lagðar saman: ", tala1 + tala2)
    print("Tölurnar margfaldaðar: ", tala1 * tala2)

def daemi2():
    fornafn = str(input("Fornafn?: "))
    eftirnafn = str(input("Eftirnafn?: "))
    print("Halló", fornafn, eftirnafn)

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
        print("Þetta dæmi er ekki tilbúið.")

    else:
        print("Ekki á milli 1-3..")