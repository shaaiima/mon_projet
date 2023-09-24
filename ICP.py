import PyPDF2
import re
import os
import subprocess

# Fonction pour extraire les tests spécifiés à partir du fichier PDF
def extract_tests_from_pdf(pdf_file_path, text_file_path, tests_to_extract):
    with open(pdf_file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.getNumPages()

        with open(text_file_path, 'w') as text_file:
            for page_num in range(num_pages):
                page = pdf_reader.getPage(page_num)
                text = page.extractText()

                # Utiliser des expressions régulières pour rechercher les tests spécifiés dans le texte
                for test in tests_to_extract:
                    pattern = re.compile(re.escape(test), re.IGNORECASE)
                    if pattern.search(text):
                        # Chercher le tag correspondant dans le fichier Log_BTF.txt
                        tag = find_tag_for_test(test, "Log_BTF.txt")
                        if tag:
                            text_file.write(f"{test} [{tag}]\n")
                        else:
                            text_file.write(f"{test}\n")
                        break

# Fonction pour chercher le tag correspondant pour un test donné dans le fichier Log_BTF.txt
def find_tag_for_test(test, log_btf_file):
    with open(log_btf_file, 'r') as file:
        for line in file:
            if test in line:
                # Extrayez le tag entre les crochets
                tag = re.search(r'\[(.*?)\]', line)
                if tag:
                    return tag.group(1)
    return None

# Liste des tests que vous souhaitez extraire du PDF
tests_a_extraire = [
    "HDMI",
    "ETHERNET",   
    "USB",
    "FRONT PANEL",
    "SWITCH",
    "CHIPSET SECURITY",
    "BLUETOOTH",
    "WIFI",
]

# Exemple de chemin brut (raw string) pour le fichier PDF
pdf_file_path = r"C:\Users\LENOVO\Desktop\shoushou\ICP_PRODUCT_ORANGE_DTIW377_v0.1.pdf"

# Chemin vers le fichier texte où vous souhaitez enregistrer les tests extraits
text_file_path = r"C:\Users\LENOVO\Desktop\shoushou\ICP.txt"

# Appel de la fonction pour extraire les tests spécifiés et les enregistrer dans le fichier texte
extract_tests_from_pdf(pdf_file_path, text_file_path, tests_a_extraire)

# Enregistrement du fichier Excel
# Ajoutez ici le code pour enregistrer le fichier Excel comme vous l'avez fait auparavant

# Lire et afficher le contenu du fichier ICP.txt
with open(text_file_path, 'r') as icp_file:
    icp_content = icp_file.read()
    print("Contenu du fichier ICP.txt:")
    print(icp_content)

# Ouvrir le fichier ICP.txt avec le programme par défaut associé au fichier texte
# Cela ouvrira le fichier ICP.txt avec le bloc-notes de Windows
subprocess.Popen(['start', text_file_path], shell=True)

