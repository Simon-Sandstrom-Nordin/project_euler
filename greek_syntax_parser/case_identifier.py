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

def second_dec_os(stem):
    print(stem + " : second declination noun on -os")
    print("Singular:")
    print("N: " + stem + "os")
    print("G: " + stem + "ou")
    print("D: " + stem + "ω")
    print("A: " + stem + "on")
    print("V: " + stem + "e")
    #
    print("Plural:")
    print("N: " + stem + "oi")
    print("G: " + stem + "ωv")
    print("D: " + stem + "ois")
    print("A: " + stem + "ous")
    print("V=N: " + stem + "oi")
    print("\n")
second_dec_os("log")

def second_dec_ov(stem):
    print(stem + " : second declination noun on -ov")
    print("Singular:")
    print("N: " + stem + "ov")
    print("G: " + stem + "ou")
    print("D: " + stem + "ω")
    print("A: " + stem + "ov")
    print("V=N: " + stem + "ov")
    #
    print("Plural:")
    print("N: " + stem + "a")
    print("G: " + stem + "ωv")
    print("D: " + stem + "ois")
    print("A: " + stem + "a")
    print("V=N: " + stem + "a")
    print("\n")
second_dec_ov("erg")    # Ergon was work, which is like this fuckery hell
second_dec_ov("snmei")  # Snmeion was sign, just for fun

# Contracta nouns on -os and -ov contracted like -ous are above my paygrade, which is none anyway
# but useful to know of their existance, like third declination nouns

# Hetroklitiska former har annat böjningsmönster än ordets normala
# Metaplasm är övergång till annan deklination än ursprungliga
# Attiska andra deklinationen - aos blev -nos under hellenistisk tid till klassisk attiska och skit

def third_dec_nouns_klausil_v_k_g_ch(stem):
    print(stem + " : third declination noun on -v,-k,-g,-ch")
    print("Singular:")
    print("N: " + stem[0:len(stem)-1] + "ψ")
    print("G: " + stem + "os")
    print("D: " + stem + "i")
    print("A: " + stem + "a")
    print("V=N: " + stem[0:len(stem)-1] + "ψ")
    #
    print("Plural:")
    print("N: " + stem[0:len(stem)-1] + "s")
    print("G: " + stem + "ωv")
    print("D: " + stem[0:len(stem)-1] + "ψi (n)")
    print("A: " + stem + "as")
    print("V=N: " + stem[0:len(stem)-1] + "s")
    print("\n")
third_dec_nouns_klausil_v_k_g_ch("phleb")   # åder
# sark (kött) uses xsi instead of psi
# salpigg (trumpet) uses xsi
# thrich (hår) uses xsi instead of chi

def third_dec_nouns_klausil_vt(stem):
    print(stem + " : third declination noun on -vt")
    print("Singular:")
    print("N: " + stem[0:len(stem)-2] + "s")
    print("G: " + stem + "os")
    print("D: " + stem + "i")
    print("A: " + stem + "a")
    print("V: " + stem[0:len(stem)-2] + "v")
    #
    print("Plural:")
    print("N: " + stem + "es")
    print("G: " + stem + "wn")
    print("D: " + stem[0:len(stem)-2] + "si(n)")
    print("A: " + stem + "as")
    print("V=N: " + stem + "es")
    print("\n")
third_dec_nouns_klausil_vt("gigavt")

# Verloren jag ich, was vergangen ist,
# Hinterfrag das Elend nicht
# Sonst würd ich den Verstand verlier'n
# Ich kann nicht erreichen, was nicht ist, doch wie tief der Schmerz auch sitzt
# Ich muss nur vergessen, was passiert
# - Rememberance, Selphius

# https://www.youtube.com/watch?v=AgHJo1N3M8g&t=706s&ab_channel=gigi
# Third declension adjectives have the same declensions for masculine/feminine forms,
# And the definite article will tell which inherent gender a noun has. Adjectives morph
# to have congruent genders as the nouns they are an attribute to.
