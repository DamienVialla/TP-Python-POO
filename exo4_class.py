import json
from datetime import datetime
import sys

chemin_acces = "./data/donnees.json"

class Movie:
    
    def __init__(self, titre : str,dateSortie : str, description : str):
        self.titre = titre
        self.description = description
        self.dateSortie = dateSortie
        # on teste si la date rentrée est au format demandé
        try :
            datetime.strptime(dateSortie, "%d/%m/%Y")
            self.dateSortie = dateSortie
        except ValueError:
            print(f"{dateSortie} n'est pas au format indiqué, nous n'avons pas pu enregistrer votre film")
            sys.exit()
    
    @staticmethod # ouverture en lecture du fichier
    def ouverture_json():
        with open(chemin_acces, "r") as file:
            data = json.load(file)
        return data
    
    @staticmethod # ouverture en ecriture du fichier
    def enregistrement_json(data):
        with open(chemin_acces, "w") as file:
            json.dump(data, file, indent=4)
    
    @staticmethod
    def enregistrement_film(titre, dateSortie, description):
        # on intancie un film        
        data = Movie.ouverture_json()
        
        movie = Movie(titre, dateSortie, description)
        film_trouve = False
        
        # test si le film est déjà dans BdD. Pris en compte de "capitalize" pour éviter les problèmes de casse
        for i in range(len(data["movies"])):
            if data["movies"][i]["titre"] == titre.capitalize() and data["movies"][i]["date_de_sortie"] == dateSortie:
                print(f"\nle film {titre.capitalize()} sorti le {dateSortie} existe déjà et ne peux pas être mis en double")
                film_trouve = True
        
        # si film non présent dans BdD, on l'ajoute  
        if not film_trouve :  
            data["movies"].append({# on ajoute les attributs du film
                                    "titre": movie.titre.capitalize(),
                                    "date_de_sortie": movie.dateSortie,
                                    "description": movie.description})
            print(f"\n{titre.capitalize()} a été rajouté à notre base de données")
            Movie.enregistrement_json(data)  
    
    @staticmethod
    def list_titres():     
        data = Movie.ouverture_json()
        liste_film = [] # création d'une liste pour ensuite trier par ordre aphabétique pour faciliter la recherche)
        for i in range(len(data["movies"])):
            liste_film.append(data["movies"][i]["titre"])
        print(" - ".join(sorted(liste_film)))
        
            
    
    def details_film(titre):    
        data = Movie.ouverture_json()
        for i in range(len(data["movies"])):
            if data["movies"][i]["titre"] == titre.capitalize() :
                print(f"Titre : {data['movies'][i]['titre']}\nDate de Sortie : {data['movies'][i]['date_de_sortie']}\nCommentaire : {data['movies'][i]['description']}")
                
    @staticmethod
    def suppression_film(titre):  
        data = Movie.ouverture_json()
        
        # on va chercher où se trouve le titre dans la base de données et on le supprime
        for i in range(len(data["movies"])):
            if data["movies"][i]["titre"] == titre.capitalize():
                del data["movies"][i]
                
        Movie.enregistrement_json(data)
    
    @staticmethod
    def modification_film(titre : str, new_titre : str,new_date : str ,new_description : str):
        data = Movie.ouverture_json()
        
        # on va chercher où se trouve le titre dans la base de données et on le supprime
        for i in range(len(data["movies"])):
            if data["movies"][i]["titre"] == titre.capitalize():
            # on ajoute les attributs du film
                if new_titre != "Pas de modification":
                    data["movies"][i]["titre"] = new_titre.capitalize()
                if new_date != "Pas de modification":
                    data["movies"][i]["date_de_sortie"] = new_date
                if new_description != "Pas de modification":
                    data["movies"][i]["description"] = new_description
        # on ouvre écriture le json au format json et on met à jour
        
        Movie.enregistrement_json(data)
        
        print(f"\n{titre} a été modifié, ci-joint sa nouvelle fiche : ")
        #affiche la fiche du film modifié
        if new_titre != "Pas de modification":
            Movie.details_film(new_titre)
        else :
            Movie.details_film(titre)

    @staticmethod
    def tri():
        data = Movie.ouverture_json()
        film_tri = sorted(data["movies"], key=lambda movie : datetime.strptime(movie["date_de_sortie"], "%d/%m/%Y"))

        # impression des films et leur date triés
        for movie in film_tri:
            print(f"{movie['titre']} - {movie['date_de_sortie']}")
            

