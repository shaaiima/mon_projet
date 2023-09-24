import re
test_number=2 
def create_html_table(table_content, test_number):
    return f"""
        <h3>Tableau {test_number} (Test#{test_number})</h3>
        <table border="1" cellspacing="0" cellpadding="5">
            <tr>{table_content}</tr>
        </table>
        <br>
    """

def extract_tables_from_icp_file(icp_file_path):
    with open(icp_file_path, 'r') as icp_file:
        icp_content = icp_file.read()

        # Utiliser des expressions régulières pour rechercher les tables avec leur nom
        tables = re.findall(r'Test#(\d+)\s*[\):]\s*([\s\S]*?)(?=Test#|$)', icp_content)

        # Enregistrer toutes les tables dans un fichier HTML
        with open("All_Tables.html", 'w', encoding='utf-8') as html_file:
            html_file.write("<html><body>")

            for i, (test_number, table_content) in enumerate(tables, 1):
                # Séparer les lignes du tableau
                rows = table_content.strip().split('\n')
                rows_html = "\n".join([f"<tr><td>{row}</td></tr>" for row in rows])
                html_table = create_html_table(rows_html, test_number)
                html_file.write(html_table)

            html_file.write("</body></html>")

if __name__ == "__main__":
    icp_file_path = "All_Tables.html"
    extract_tables_from_icp_file(icp_file_path)

