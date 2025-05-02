class Client:
    def __init__(self,id, nom, prenom):
        self.id = id
        self.nom =nom
        self.prenom =prenom
#Affichage
    def __str__(self):
        return f"Client(Client n°{self.id}, prenom={self.prenom} nom={self.nom})"
    


