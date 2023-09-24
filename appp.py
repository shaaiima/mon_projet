import PyPDF2

# Fonction pour extraire le contenu du tableau sous le sous-titre "Test#1"
def extract_table_from_pdf(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.getNumPages()

        # Recherche du sous-titre "Test#1"
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()

            if "Test#1" in text:
                # Rechercher le début du tableau après le sous-titre
                start_index = text.find("Test#1")
                table_text = text[start_index:]

                # Afficher le contenu du tableau trouvé
                print("Table content:")
                print(table_text)

                break

# Exemple de chemin brut (raw string) pour le fichier PDF
pdf_file_path = r"C:\Users\LENOVO\Desktop\shoushou\ICP_PRODUCT_ORANGE_DTIW377_v0.1.pdf"

# Appel de la fonction pour extraire le contenu du tableau sous le sous-titre "Test#1"
extract_table_from_pdf(pdf_file_path)
