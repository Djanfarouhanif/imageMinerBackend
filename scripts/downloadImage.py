import os 
import aiohttp
import asyncio
from .main import imageUrl


# Dossier où stocker les images
folder = "images"

# Vérifier si le dossier existe, sinno le créer
if not os.path.exists(folder):
    os.makedirs(folder)

async def download_image(session, url, index):
    # Télécharge une image depuis une URL et l'enregistre dans le dossier.abs

    try:
        async with session.get(url,timeout=10) as response:
            if response.status == 200:
                # Déterminer l'extension du fichier 
                ext = url.split('.')[-1].split('?')[0]
                if len(ext) > 5 or '/' in ext: #  Cas où l'URL ne contient pas d'extension valide
                    ext = "jpg" # Extension par défaut
                
                filename = f"image_{index + 1}.{ext}"
                filepath = os.path.join(folder,filename)

                # Ecriture asynchrone du fichier 
                with open(filepath, "wb") as file:
                    file.write(await response.read())

                print(f" Téléchargé : {filename}")
            else:
                print(f"Erreur {response.status} pour {url}")

    except Exception as e:
        print(f"Erreur lors du téléchargement de {url} : {e}")

async def main(url):
    # Gérz le téléchargement de toutes les images en parallèle.abs
    img_urls = imageUrl(url)

    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url, index) for index, url in enumerate(img_urls)]
        await asyncio.gather(*tasks) # Exécute toutes les tâches en parallèle

# Lancer le programme asynchrome

if __name__ == "__main__":
    asyncio.run(main(url))
