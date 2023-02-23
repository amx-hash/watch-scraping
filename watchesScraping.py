import requests
from bs4 import BeautifulSoup
import pandas as pd

from Watch import Watch

base_url = "https://www.crownandcaliber.com"
uri = "/collections/shop-for-watches?page="
final_url = base_url + uri
page_number = 33


# Cette fonction prend une URL en entrée, envoie une requête HTTP à cette URL
# et renvoie une instance de BeautifulSoup contenant le HTML de la page. Si la réponse HTTP n'est pas réussie,
# elle affiche un message d'erreur et renvoie None.
def swoup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser') if response.ok else print("Error response") or None


# Cette fonction prend un tableau de montres en entrée et renvoie une liste de dictionnaires contenant des informations sur chaque montre.
def format_watches(watches_array):
    watches_data = []
    for watch in watches_array:
        if watch:
            watch_dict = {
                'Marque': watch.get_brand(),
                'Nom': watch.get_name(),
                'Référence': watch.get_ref(),
                'Condition': watch.get_condition(),
                'Boîte': watch.get_box(),
                'Papiers': watch.get_papers(),
                'Prix': watch.get_price()

            }
            watches_data.append(watch_dict)

    return watches_data


watches = []


# C'est la fonction principale du programme. Elle boucle à travers une plage de pages, envoie des requêtes HTTP à chaque
# page, extrait des informations sur chaque montre de la page, crée un objet Watch pour chaque montre,
# ajoute chaque objet Watch à une liste de montres, formate la liste de montres à l'aide de la fonction "format_watches",
# et enregistre les données résultantes dans un fichier CSV.
def main():
    for page in range(0, page_number + 1):
        soup = swoup(final_url + str(page))
        watch_cards = soup.findAll("div", class_="popular-watches--card")

        for watch_card in watch_cards:
            card = watch_card.find("a", class_="grid-view-item__link")
            brand = card.find("div", class_="card-title").text
            name = card.find("div", class_="card-subTitle").text
            ref = card.find("div", class_="card-barcode").text
            condition = card.find('span', class_="list-value").text.replace("\n", "").strip()
            box = card.find_all('span', class_="list-value")[1].text.replace("\n", "").strip()
            papers = card.find_all('span', class_="list-value")[2].text.replace("\n", "").strip()
            price = card.find('span', class_="product-price__price").text.replace("\n", "") if card.find('span',
                                                                                                         class_="product-price__price") else None

            watches.append(Watch(brand, name, ref, condition, box, papers, price))

    watches_array = format_watches(watches)
    df = pd.DataFrame(watches_array)
    df.to_csv("watch.csv", index=False)


main()
