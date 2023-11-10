# Robin : ne pas tenir compte de l'entièreté des points susceptibles d'être donnés sur les getter / setter


from os import sys
import random
from datetime import datetime

class Client:
    
    def __init__(self, nom : str, prenom : str, adresse : str, NIR : int):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        
        if isinstance(NIR, int) and len(str(NIR))==15 :
            self._NIR = NIR
        else :
            print(f"{NIR} n'est pas un numéro de NIR, nous ne pouvons pas instancier")
            sys.exit()
    
    @property
    def NIR(self):
        return self._NIR
    
    @NIR.setter
    def NIR(self, valeur):
        if isinstance(valeur, int) and len(str(valeur))==15 :
            self._NIR = valeur
        else :
            print(f"{valeur} n'est pas un numéro de NIR, nous ne pouvons pas instancier")
            sys.exit()
    def __str__(self):
        return f"{self.nom}, {self.prenom},{self.adresse},{self.NIR}"

class CompteBancaire:
    """
    date : str format YYYY-MM-DD
    """
    sommeSolde = 0
    
    def __init__(self, dateCreation : str, client, solde : float):
        
        self.solde : str= solde
        # try except pour voir si le client rentré est au format class Client => marche pas !!!
        try :
            isinstance(client, Client)
            self.client = client
        except ValueError:
            print(f"{client} n'est pas au bon format, nous ne pouvons pas instancier")
            sys.exit()
        
        # try except pour voir si la date existe bien après l'avoir convertie
        try :
            datetime.strptime(dateCreation, '%Y-%m-%d')
            self.dateCreation = dateCreation
        except ValueError:
            print(f"{dateCreation} n'est pas un numéro de NIR, nous ne pouvons pas instancier")
            sys.exit()
        
        # création identifiant selon 4*Maj + date américaine inversée sans tiret
        liste_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.Identifiant = 4*random.choice(liste_alphabet) + datetime.strptime(dateCreation,'%Y-%m-%d').strftime('%d%m%Y')
        
        # propriété statique qui vient additionner la somme des soldes des comptes
        # += ne marche pas car trop de décimale donc obligé d'additionner et faire un round après
        CompteBancaire.sommeSolde = round(CompteBancaire.sommeSolde + self.solde,2)
        
    def __str__(self):
        return f"{self.dateCreation}, {self.solde},{self.client}"

    def __eq__(self, other): # methode magique pour tester l'égalité
        return self.solde == other.solde
    

            

      
# instanciation des clients et de comptes
Damien = Client("Vialla de Soleyrol", "Damien", "11 Rue des multipliants, Baillargues", 125125125125125)
Aurelie = Client("Chastan", "Aurélie", "11 Rue des multipliants, Baillargues", 132132132132132)
Clemence = Client("Chastan", "Clemence", "11 Rue des multipliants, Baillargues", 287287287287287)
Bats = Client("Vialla de Soleyrol", "Damien", "8 grand rue, Générac", 963963963963963)
compteDamien = CompteBancaire("2022-12-12", Damien, 18.35)
compteAurelie = CompteBancaire("2021-03-17", Aurelie, 125.55)
compteClemence = CompteBancaire("2020-06-15", Clemence, 125.55)
compteBats = CompteBancaire("2020-07-03", Bats, 235.36)



#création d'une fonction pour vérifier l'égalité de compte et renvoyer l'identifiant avec méthode Damien
    
def isegal(valeur_identifiant1,valeur_solde1,valeur_identifiant2,valeur_solde2):
        if valeur_solde1 == valeur_solde2:
            print(f"{valeur_identifiant1} et {valeur_identifiant2} sont égaux avec une solde de {valeur_solde1}")
        else :
            print(f"{valeur_identifiant1} et {valeur_identifiant2} ne sont pas 'égaux'")
            
# impression des identifiants et impression de leur égalité
print("\nMéthode Damien création d'une fonction : ")
# test deux comptes inégaux => OK
isegal(compteDamien.Identifiant,compteDamien.solde,compteAurelie.Identifiant,compteAurelie.solde)
# test deux comptes inégaux => OK
isegal(compteClemence.Identifiant,round(compteClemence.solde,2),compteAurelie.Identifiant,round(compteAurelie.solde,2))


# test égalité de deux comptes par méthode magique
print("\nMéthode magique: ")
# impression des identifiants et impression de leur égalité 2 comptes égaux
if compteClemence == compteAurelie:
    print(f"{compteClemence.Identifiant} et {compteAurelie.Identifiant} sont des comptes 'égaux' à {compteClemence.solde}")
else :
    print(f"{compteClemence.Identifiant} et {compteAurelie.Identifiant} ne sont pas des comptes 'égaux'")
 
# impression des identifiants et impression de leur égalité 2 comptes inégaux
if compteDamien == compteAurelie:
    print(f"{compteDamien.Identifiant} et {compteAurelie.Identifiant} sont des comptes 'égaux' à {compteDamien.solde}")
else :
    print(f"{compteDamien.Identifiant} et {compteAurelie.Identifiant} ne sont pas des comptes 'égaux'")

# impression de tous les comptes bancaires crées
print(f"\nLa somme de l'ensemble des comptes est de : {CompteBancaire.sommeSolde}\n")