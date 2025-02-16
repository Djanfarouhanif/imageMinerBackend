import os
import requests
from main import imageUrl
import shutil

# Récuperer tout les urls

# Dossier où stocker les images
folder = "images"


# Fonction pour télécharger les image
def download(folder):
    # Dossier où es stocker les image
    img_url = imageUrl()

    # a chaque iteration on l'ajouter un index a l'element
    for index, url in enumerate(img_url):
        try:
            # Télécharge l'imageUrl
            response = requests.get(url,stream=True)
            response.raise_for_status() # Vérifier que la requete a reussi

            # Déterminer l'extention de l'image (jpg, png, etc)
            if '?' in url :
                clean = url.split('?')[0] # suprimer tous ce qui se trouver apres ?
                #ext = clean.split('.')[-1] # extrainre le 
                filename = clean.split('/')[-1] # Extraire le nom de l'image
                print(filename, "*********************")
            else:
                ext = url.split('.')[-1] # split perment de couper le string a se android

            #filename = f"image_{index + 1}.{ext}" # Crée un nom pour l'image
                filename = url.split('/')[-1] # extraire le nom sur l'url
            filepath = os.path.join(folder,filename) # Ajouter l'image dans le dossier

            # Sauvergarder l'imageUrl
            with open(filepath, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)

            print(f"Téléchargement du fichier: {filename}")
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors du téléchargement de {url} : {e}")

# Vérifier si le dossier existe, sinon le crée

if not os.path.exists(folder):
    os.makedirs(folder)

    # Télécharger l'image
    download(folder)

else:
    shutil.rmtree(folder)
    print('suprimer')
    if not os.path.exists(folder):
        os.makedirs(folder)
        # Télécharger l'image
        download(folder)
    