class  Chambre:
    def __init__(self,id , numero,prix,type_chambre):
        self.id = id
        self.numero = numero
        self.prix= prix
        self.type= type_chambre
    def __str__(self):
        return f"Chambre(id={self.id}, numero={self.numero}, prix={self.prix}€/nuit , type={self.type})"

class ChambreSimple(Chambre):
    def __init__(self, id, numero, prix):
        super().__init__(id, numero, prix, "simple")


class ChambreDouble(Chambre):
    def __init__(self, id, numero, prix):
        super().__init__(id, numero, prix, "double")


class ChambreSuite(Chambre):
    def __init__(self, id, numero, prix):
        super().__init__(id, numero, prix, "suite")

