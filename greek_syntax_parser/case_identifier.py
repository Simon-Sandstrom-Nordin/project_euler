# First declination nouns

# Feminine first declination nouns end in -ᾱ, -ᾰ, -η in
#   nominative singular, and in
# nevermind, as a rule of thumb feminine declinations and in
#   -a, -a, -n while masculine end in -as, ns.

print("#Feminine\n")

def first_dec_fem_group_1(stem):    # ends in -a in all forms which is preceded by eps, iota, or rho
    print(stem + " : first declination group 1 feminine")
    print("Singular:")
    print("NV: " + stem + "a")
    print("G: " + stem + "as")
    print("D: " + stem + "a")
    print("A: " + stem + "av")
    #
    print("Plural:")
    print("NV: " + stem + "ai")
    print("G: " + stem + "wn")
    print("D: " + stem + "ais")
    print("A: " + stem + "as")
    print("\n")
first_dec_fem_group_1("oik")

def first_dec_fem_group_2(stem):    # ends in -n in all forms which is NOT(!!!!) preceded by eps, iota, or rho
    print(stem + " : first declination group 2 feminine")
    print("Singular:")
    print("NV: " + stem + "n")
    print("G: " + stem + "ns")
    print("D: " + stem + "n")
    print("A: " + stem + "nv")
    #
    print("Plural:")
    print("NV: " + stem + "ai")
    print("G: " + stem + "wn")
    print("D: " + stem + "ais")
    print("A: " + stem + "as")
    print("\n")
first_dec_fem_group_2("vik")

def first_dec_fem_group_3(stem):    # ends in -a but with d.c. u in NAV(s) and - in GD in which case it's before an ipsilon or a rho exept for -ra which ends in -rns -rn i GD(s) and shit n
    print(stem + " : first declination group 3 feminine")
    print("Singular:")
    print("NV: " + stem + "a")
    print("G: " + stem + "as")
    print("D: " + stem + "a")
    print("A: " + stem + "av")
    #
    print("Plural:")
    print("NV: " + stem + "ai")
    print("G: " + stem + "wn")
    print("D: " + stem + "ais")
    print("A: " + stem + "as")
    print("\n")
first_dec_fem_group_3("asthevei")

def first_dec_fem_group_4(stem):    # -a u in NAV(s) -n in GD. Before there's not eps, iota, or rho
    print(stem + " : first declination group 4 feminine")
    print("Singular:")
    print("NV: " + stem + "a")
    print("G: " + stem + "ns")
    print("D: " + stem + "n")
    print("A: " + stem + "av")
    #
    print("Plural:")
    print("NV: " + stem + "ai")
    print("G: " + stem + "wn")
    print("D: " + stem + "ais")
    print("A: " + stem + "as")
    print("\n")
first_dec_fem_group_4("tpaπez")

print("#Masculine\n")

def first_dec_mas_group_1(stem):    # ends in -a in all forms which is preceded by eps, iota, or rho
    print(stem + " : first declination group 1 masculine")
    print("Singular:")
    print("N: " + stem + "s")
    print("G: " + stem[1:len(stem)-1] + "ou")
    print("D: " + stem)
    print("A: " + stem + "v")
    print("V: " + stem)
    #
    print("Plural:")
    print("NV: " + stem + "i")
    print("G: " + stem[1:len(stem)-1] + "wn")
    print("D: " + stem + "is")
    print("A: " + stem + "s")
    print("\n")
first_dec_fem_group_1("veavia")

def first_dec_mas_group_2(stem):    # ends in -n in all forms which is NOT(!!!!) preceded by eps, iota, or rho
    print(stem + " : first declination group 2 masculine")
    print("Singular:")
    print("N: " + stem + "s")
    print("G: " + stem[1:len(stem)-1] + "ou")
    print("D: " + stem)
    print("A: " + stem + "v")
    print("V: " + stem[1:len(stem)-1] + "a")
    #
    print("Plural:")
    print("NV: " + stem[1:len(stem)-1] + "ai")
    print("G: " + stem[1:len(stem)-1] + "wn")
    print("D: " + stem[1:len(stem)-1] + "ais")
    print("A: " + stem[1:len(stem)-1] + "as")
    print("\n")
first_dec_fem_group_2("vautn")

def first_dec_mas_group_etc(stem):    # other examples were in this form.
    print(stem + " : first declination group etcetera masculine")
    print("Singular:")
    print("N: " + stem + "s")
    print("G: " + stem)
    print("D: " + stem)
    print("A: " + stem + "n")
    print("V: " + stem)
    #
    print("Plural:")
    print("-")
    print("-")
    print("-")
    print("-")
    print("\n")
first_dec_mas_group_etc("Aewvida")

