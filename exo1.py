from os import sys

# grosse redondance entre le getter / setter et le test de l'attirbut dans le init. Sans doute moyen de regrouper tout cela.
class Entreprise:
    def __init__(self, nom: str, adresse: str, siret: int):
        self.nom = nom
        self.adresse = adresse
        
        # test à la création l'attribut siret
        if isinstance(siret, int) and len(str(siret))==14 : # test si valeur a bien 14 caractère et si c'est un entier
            self._siret = siret
        elif len(str(siret))!=14  : # gestion erreur longueur
            print(f"Votre siret ({siret}) n'est pas un numéro valide car il possède {len(str(siret))} caractères et non 14")
        elif not isinstance(siret, int) : # gestion erreur integer
            print(f"Votre siret ({siret}) n'est pas un numéro valide car pas une valeur numérique")
   
        
    @property
    def siret(self):
        return self._siret
    
    @siret.setter 
    def siret(self, valeur):
        if isinstance(valeur, int) and len(str(valeur))==14 : # test si valeur a bien 14 caractère et si c'est un entier
            self._siret = valeur
        elif len(str(valeur))!=14  : # gestion erreur longueur
            print(f"Votre siret ({valeur}) n'est pas un numéro valide car il possède {len(str(valeur))} caractères et non 14")
        elif not isinstance(valeur, int) : # gestion erreur integer
            print(f"Votre siret ({valeur}) n'est pas un numéro valide car pas une valeur numérique")
            

    def __str__(self): # méthode magique pour écrire la principale phrase
        return f"L'entreprise {self.nom}, ayant son siège social au {self.adresse}, possède le numéro de siret {self._siret}"      

# création d'une instance et impression des caractéristiques
Credit_Agricol = Entreprise("Crédit Agricol", "12 chemin de l'horloge 30000 Nimes", 12512512512512)
print("Donneés de votre instanciation :\n",Credit_Agricol)

# impression nom entreprise
print("Nom de votre instanciation :\n",Credit_Agricol.nom)

#changement numéro de siret et impression
Credit_Agricol.siret = "123456789t101e"
Credit_Agricol.siret = 123456789101

