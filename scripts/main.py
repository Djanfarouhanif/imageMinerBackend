import requests
from bs4 import BeautifulSoup
import html5lib


url = "https://miniamaker.ai/" # Url a scrapper les image

def imageUrl():
        
    response = requests.get(url) # Récupérer le contenu HTML de la page

    if response.status_code == 200:

        # Créer un objet BeautifulSoup avec html5lib camme parser
        soup = BeautifulSoup(response.content, 'html5lib') 

        # Trouver toutes les balise <img> 
        images = soup.find_all('img')
        
        # Extraire les liens des images
        image_urls = []

        for img in images:
            # Récupérer l'atribu src de chaque image
            src = img.get('src')

            # Si le lien de l'image est relatif, le comptéter avec l'url de base
            if src.startswith('http'):
                image_urls.append(src)
                
            else:
                image_urls.append(url + src)

        # Afficher les liens des image
        for img_url in image_urls:
            print(img_url)
        return image_urls

    else:
        print(f"Echec de la requête {response.status_code}")
