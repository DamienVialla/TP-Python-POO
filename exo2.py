from dataclasses import dataclass

@dataclass
class DatabaseConnection:
    type : str
    user : str
    password : str
    hote : str = "localhost"
 
    # propriété statique, pour se faire on ne la type pas (2h pour m'en rendre compte) pas d'utilisation de ClassVar non maitrisé
    nb_instance = 0
    
    # permet d'incrémenter à chaque instanciation
    def __post_init__(self):
        DatabaseConnection.nb_instance +=1
    
    @staticmethod  
    def impression():
        print(f"La classe {__class__.__name__} possède actuellement {DatabaseConnection.nb_instance} instance{'s' if DatabaseConnection.nb_instance>1 else ''}.")
 
    # méthode de classe qui crée une DatabaseConnection particulière    
    @classmethod
    def instance_particuliere(cls):
        connexion_particuliere = cls('mariadb','76.287.872.12','root','123')
        return connexion_particuliere
    
# instanciation de plusieurs DatabaseConnection
connexion1 = DatabaseConnection("MySQL","root","12589""76.287.872.12",)
connexion2 = DatabaseConnection("PostgreSQL","root","12365","76.287.842.12")
connexion3 = DatabaseConnection("MySQL","root","2568","76.127.878.14")
connexion4 = DatabaseConnection("PostgreSQL","root","365","76.377.873.15")
connexion5 = DatabaseConnection("mariadb","root","1215847","76.787.972.16")

# impression du nombre de classe(s) créee(s) => pas bon
DatabaseConnection.impression()

# instanciation et impression d'un objet sans spécifier l'hôte
connexion6 = DatabaseConnection("MySQL","76.365.972.12","root")
print(connexion6)

# impression de la méthode de classe
print(DatabaseConnection.instance_particuliere())