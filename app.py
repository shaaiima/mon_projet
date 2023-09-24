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
            contenu = fichier.read().lower()  # Convertir en minuscules
            if mot.lower() in contenu:  # Comparaison insensible à la casse
                return True
            else:
                return False
    except FileNotFoundError:
        print("Le fichier {} n'a pas été trouvé.".format(nom_fichier))
        return False

# Route de l'API qui traite les requêtes POST pour vérifier si un mot est présent dans le fichier BFE.txt
@app.route('/api/check_mot_BFE', methods=['POST'])
def check_mot_BFE():
    mot_a_chercher = request.json['mot']
    fichier_texte = "BFE.txt"
    if mot_present(mot_a_chercher, fichier_texte): 
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

# Route de l'API pour afficher le contenu du fichier ICP.txt
@app.route('/api/display_icp_content', methods=['GET'])
def display_icp_content():
    fichier_texte_icp = "ICP_bfe.txt"
    try:
        with open(fichier_texte_icp, 'r') as fichier_icp:
            contenu_icp = fichier_icp.read()
            return jsonify({'content': contenu_icp})  # Ajout de jsonify pour renvoyer le contenu en JSON
    except FileNotFoundError:
        print("Le fichier ICP_bfe.txt n'a pas été trouvé.")
        return "Une erreur s'est produite lors du chargement du fichier ICP_bfe.txt."

# Point d'entrée de l'application Flask
if __name__ == '__main__':
 app.run(debug=True)  # Nous activons le mode de débogage pour afficher les erreurs détaillées.
