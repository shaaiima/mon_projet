def mot_present(mot, nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            contenu = fichier.read()
            if mot in contenu:
                return True
            else:
                return False
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")
        return False


def mots_dans_fichier(fichier_test, fichier_source):
    mots_trouves = []
    with open(fichier_test, 'r') as fichier_test:
        mots = fichier_test.read().split()
    
    for mot in mots:
        if mot_present(mot, fichier_source):
            mots_trouves.append(mot)

    return mots_trouves

fichier_test = "test_BTF.txt"
fichier_source = "Log_BTF.txt"

mots_trouves = mots_dans_fichier(fichier_test, fichier_source)
print("Mots trouvés dans {} et présents dans {} :".format(fichier_test, fichier_source))
print(mots_trouves)
