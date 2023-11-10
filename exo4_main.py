from os import sys
from exo4_class import Movie
import os
import json
import pygame
import time


####################################################
# Les fonctions
####################################################

# fonction sur la partie variable des modifs à faire en cas de choix  3
def test_modification(texte1, texte2):
        test_modif = input (f"\nSouhaitez-vous changer {texte1} (O/N) ? ")
        if test_modif == "O":
            modification = input(f"{texte2} : ")
        elif test_modif =="N":
            print("Aucune modification prise en compte.")
            modification = "Pas de modification"
        else :
            print("Seuls 'O' et 'N' sont tolérés comme réponse.")
            test_modification(texte1, texte2)
        return modification

# partie commune => transformé en fonction, affiche liste des films dans BdD, on retourne une info pour savoir si la BdD est vide ou non pour adapter le message dans les choix du main
def impression_liste_titres():
    data = Movie.ouverture_json()
    
    if len(data["movies"]) == 0:# test si la base de données est vide pour adapter le print
        print("\nAucun film rentré dans la base de données")
        return False
    else :
        print("\nVoici la liste des films enregistrés dans notre base de données par ordre alphabétique :\n")
        Movie.list_titres()
        return True

# partie commune => transformé en fonction, affiche la conclusion du choix
def impression_conclusion_choix(titre, texte):
        print(f"\n{titre} a été {texte} à notre base de données")

# partie commune => transformé en fonction, affiche caractéristique du film
def impression_details_film():
    print("\nVoici ses caractéristiques :")
    Movie.details_film(titre)

####################################################
# Partie préalable au fonctionnement du main
####################################################

chemin_acces = "./data/donnees.json"
# test si le dossier data exist ou non, en fonciton on le créee et on créee un fichier donnees.json vierge
if not os.path.exists("./data"):
    os.makedirs("./data")

# si dossier existe, on teste s'il y a le jason à l'intérieur
if not os.path.exists(chemin_acces):
    with open(chemin_acces, "w") as fichier: 
	    json.dump({'movies': []}, fichier)  

####################################################
# Partie principale du Main
####################################################

titre_presentation = "Gestion Bibliothèque de films"    
print("="*len(titre_presentation))
print(titre_presentation)
print("="*len(titre_presentation))
pygame.mixer.init()
pygame.mixer.music.load("damien-librairie.mp3")
pygame.mixer.music.play()
    
while True :
    # menu principal
    print("\n1- Ajouter un film")
    print("2- Supprimer un film")
    print("3- Modifier un film")
    print("4- Editer information film")
    print("5- Quitter")
    choix = input("\nQuel est votre choix ? ")

    match choix:
        case "1":
            titre = input ("\nQuel est le titre du film ? ")
            dateSortie = input("Quel est la date de sortie (jj/mm/aaaa) ? ")
            description = input("Quel description souhaitez-vous faire ? ")
            Movie.enregistrement_film(titre,dateSortie,description)
            impression_liste_titres()

        case "2":
            if impression_liste_titres(): # test si BdD vide ou non pour proposer cas échéant le reste. Idem pour les autres case
                titre = input("\nQuel film souhaitez-vous supprimer ? ")
                Movie.suppression_film(titre)
                impression_conclusion_choix("supprimé")
                impression_liste_titres()
            
        case "3":
            if impression_liste_titres():
                titre = input("\nQuel film souhaitez-vous modifier ? ")
                impression_details_film() 
               
                Movie.modification_film(titre,
                                    test_modification("le titre","Nouveau titre"),
                                    test_modification("la date de sortie","Nouvelle date de Sortie (jj/mm/aaaa)"),
                                    test_modification("la description","Nouvelle description"))
            
        case "4":
            if impression_liste_titres():
                choix_edition = input("\nSouhaitez-vous ?\n1- Consulter un livre en particulier\n2- Editer la liste des films par ordre croissant de date de sortie ?\n")
                if choix_edition == "1":
                    titre = input("\nQuel film souhaitez-vous consulter ? ")
                    impression_details_film()
                elif choix_edition == "2":
                    Movie.tri()
                else :
                    print(f"{choix_edition} n'est pas un choix possible, merci de tapper 1 ou 2.")
            
        case "5":
            def play_video():
                # Ouvrir la vidéo avec le lecteur vidéo par défaut
                video_file = "aurevoir.mp4"
                os.system(f'start {video_file}')
            
            play_video()
            time.sleep(5)
            sys.exit()
            
        case _:
            print(f"\n{choix} ne fait pas parti des choix autorisés")
                                                                                
                                                                                                                                      

