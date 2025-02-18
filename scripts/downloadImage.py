import os 
import aiohttp
import asyncio
from .main import imageUrl
from django.conf import settings
import shutil

# Dossier où stocker les images
folder = os.path.join(settings.MEDIA_ROOT, "images")


# le fichier zip 
zip_file = os.path.join(settings.MEDIA_ROOT, "images.zip")

# Vérifier si le dossier existe, sinno le créer
def control():
    # ==================== Fonction pour controler le dossier image======================
    if not os.path.exists(folder):
        os.makedirs(folder)
        sub_folder = os.path.join(folder, 'images')
        os.makedirs(sub_folder)
    else:
        shutil.rmtree(folder)
        os.makedirs(folder)
        sub_folder = os.path.join(folder, 'images')
        os.makedirs(sub_folder)
    # ================================= Fonction pour controler le fichier zip =========================================================

    if os.path.exists(zip_file):
       
        os.remove(zip_file)
        
    return sub_folder

# le sous dossier 

async def download_image(session, url, index):
    # Télécharge une image depuis une URL et l'enregistre dans le dossier.abs

    # Le sous dossier de folder
    sub_folder = control()
    try:
        async with session.get(url,timeout=10) as response:
            if response.status == 200:
                # Déterminer l'extension du fichier 
                ext = url.split('.')[-1].split('?')[0]
                if len(ext) > 5 or '/' in ext: #  Cas où l'URL ne contient pas d'extension valide
                    ext = "jpg" # Extension par défaut
                
                filename = f"image_{index + 1}.{ext}"
                filepath = os.path.join(sub_folder,filename)

                # Ecriture asynchrone du fichier 
                with open(filepath, "wb") as file:
                    file.write(await response.read())
                    # print(filename, "*************")
            else:
                # print(f"Erreur {response.status} pour {url}")
                pass

    except Exception as e:
        print(f"Erreur lors du téléchargement de {url} : {e}")

async def main(url):
    # Gérz le téléchargement de toutes les images en parallèle.abs
   
    try:
        img_urls = imageUrl(url)

        async with aiohttp.ClientSession() as session:
            tasks = [download_image(session, url, index) for index, url in enumerate(img_urls)]
            await asyncio.gather(*tasks) # Exécute toutes les tâches en parallèle
    except Exception as error:
        message = "zéro élement trouver"
        return message
    

# Lancer le programme asynchrome

if __name__ == "__main__":
    asyncio.run(main(url))
