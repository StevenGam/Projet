class Salarié(object):  ## qui hérite de object
    """Classe des salariés"""           # Documentation de la classe

### Constructeur de la classe : construite et initialiser un  objet
    def __init__(self, nom, pnom):
        print ("Création d'un objet salarié...")
        self.Nom = nom
        self.Prenom=pnom
 
    def get_nom(self):  # Méthode 'get' pour retourner le nom
        return self.Nom
    def get_pnom(self):
        return self.Prenom
  ### pour toutes les caratéristiques ou attributs de la classe
    def set_nom(self, nouveau_nom):   # Méthode 'set' pour modifier le nom
        if nouveau_nom == "":
            print ("Le nom de l'employé ne peut pas être vide!!!!")
        else:
            self.Nom = nouveau_nom
            print ("Le Nom à été modifié.") 
     
    def afficher(self):
        print (self.Nom, " a été ajouté(e)")
### User est une classe qui hérite de la classe Salarié
class User(Salarié):
    ### constructeur de la nouvelle classe User
    def __init__(self, nom, pnom, login, pwd):
        print ("Création d'un objet User...")
        Salarié.__init__(self,nom, pnom)
        ##self.Nom = nom
        ##self.Prenom=pnom
        self.Login=login
        self.Password=pwd
        
    def Afficher_User(self):
        print("User : ", self.get_nom(),"", self.get_pnom())
    
 
# main, programme principal
## Classe mère : Salarié
salarié1 = Salarié("OULMI","Céline")  # Initialiser un objet de la classe vide
salarié1.afficher()               # Accéder à une méthode de la classe
 
print ("Nom de l'employé est:", salarié1.get_nom()) # Accéder à une propriété de la classe
print ("Modification du nom de la classe :")
salarié1.set_nom("") # Génération d'une erreur, si Nom est vide
 
salarié1.set_nom("ESGI")
salarié1.afficher()
## classe qui dérive : User
User1=User("OULMI", "Céline", "coulmi", "Mypass")
User1.Afficher_User()


