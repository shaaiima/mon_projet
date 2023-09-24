# Importation des modules nécessaires
from flask import Flask, jsonify, request
from flask_cors import CORS


# Création de l'application Flask
app = Flask(__name__)

# Activation du support CORS pour autoriser les requêtes 
CORS(app)

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


# Route de l'API qui traite les requêtes POST pour vérifier si un mot est présent dans un fichier texte
@app.route('/api/check_mot', methods=['POST'])
def check_mot():
    mot_a_chercher = request.json['mot']
    fichier_texte = "test_BTF.txt"
    if mot_present(mot_a_chercher, fichier_texte): #appel de la fct mot_present 
        response = {
            'message': "Le mot '{}' est présent dans le fichier '{}'.".format(mot_a_chercher, fichier_texte),
            'found': True
        }
    else:
        response = {
            'message': "Le mot '{}' n'est pas présent dans le fichier '{}'.".format(mot_a_chercher, fichier_texte),
            'found': False
        }

    return jsonify(response)


# Point d'entrée de l'application Flask, exécutée uniquement si ce script est exécuté en tant que programme principal.
if __name__ == '__main__':
 #app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
    
 # Lance le serveur de développement Flask pour gérer les requêtes entrantes et les transmettre aux routes correspondantes  app.run(debug=False)
 app.run (debug=False )
 
