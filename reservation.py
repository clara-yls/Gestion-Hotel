class Reservation:
    def __init__(self, id, date_arrivee, date_depart, client_id, chambre_id):
        self.id = id
        self.date_arrivee = date_arrivee
        self.date_depart= date_depart
        self.client_id = client_id
        self.chambre_id =chambre_id
    def __str__(self):
        return f"[{self.id}] Réservation du {self.date_arrivee} au {self.date_depart} - Client ID: {self.client_id}, Chambre ID: {self.chambre_id}"
        
        
