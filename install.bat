@echo off

echo Installation des dépendances...
pip install flask
pip install flask_cors

:: Exécution du script chance2.py
python chance2.py

echo L'installation et l'exécution sont terminées.
