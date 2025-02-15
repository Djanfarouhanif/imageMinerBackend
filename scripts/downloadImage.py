import os
import requests
from main import imageUrl


img_url = imageUrl()
# Dossier où stocker les images
folder = "images"

# Vérifier si le dossier existe, sinon le crée

if not os.path.exists(folder):
    os.makedirs(folder)

# Télécharger et sauvergader chaque images
for index, url in enumerate(img_url):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status() # Vérifier que la requete a reussi

        # Déterminer l'extension de l'immage (jpg, png , etc)
        ext = url.split('.')[-1]
        filename = f"image_{index + 1}.{ext}"
        filepath = os.path.join(folder, filename)

        # Sauvergardr l'image_urls

        with open(filepath, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"Téléchargeé: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors du téléchargement de {url} : {e}")