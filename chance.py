
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

# Exemple d'utilisation
mot_a_chercher = "USB"
fichier_texte = "Log_BTF.txt"

if mot_present(mot_a_chercher, fichier_texte):
    print("Le mot '{}' est present dans le fichier '{}'.".format(mot_a_chercher, fichier_texte))
else:
    print("Le mot '{}' n'est pas present dans le fichier '{}'.".format(mot_a_chercher, fichier_texte))

