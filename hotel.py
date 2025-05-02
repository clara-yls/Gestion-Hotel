from client import Client
from chambre import Chambre
from reservation import Reservation
from datetime import datetime

class Hotel:
    def __init__(self):
        self.clients = []
        self.chambres = []
        self.reservations = []

    # Clients
    def ajouter_client(self, client):
        self.clients.append(client)

    def lister_clients(self):
        for client in self.clients:
            print(client)

    def get_client_par_id(self, id):
        for client in self.clients:
            if client.id == id:
                return client
        return None
    
    def supprimer_client(self,id):
        if any(res.client_id == id for res in self.reservations):
            print("Erreur: Client avec reservation active")
            return
        self.clients=[c for c in self.clients if c.id != id]
        print(f"Client {id} supprimé.")

    # Chambres
    def ajouter_chambre(self, chambre):
        self.chambres.append(chambre)

    def lister_chambres(self):
        for chambre in self.chambres:
            print(chambre)
    
    def get_chambre_par_id(self, id):
        for chambre in self.chambres:
            if chambre.id == id:
                return chambre
        return None
    
    def supprimer_chambre(self,id):
        if any ( res.chambre_id == id for res in self.reservations):
            print("Erreur: Chambre avec resrevation active.")
            return
        self.chambres=[c for c in self.chambres if c.id != id]
        print(f"Chambre {id} suppriméé.")

    # Réservations
    def ajouter_reservation(self, reservation: Reservation):
        nouvelle_arrivee = datetime.strptime(reservation.date_arrivee, "%Y-%m-%d")
        nouvelle_depart = datetime.strptime(reservation.date_depart, "%Y-%m-%d")
        for res in self.reservations:
            if res.chambre_id == reservation.chambre_id:
                arrivee_existante = datetime.strptime(res.date_arrivee,"%Y-%m-%d")
                depart_existante = datetime.strptime(res.date_depart,"%Y-%m-%d")

                if (nouvelle_arrivee < depart_existante) and (nouvelle_depart > arrivee_existante):
                    print("Erreur: Chambre déjà réservée à ces dates.")
                    return
        self.reservations.append(reservation)
        print("Réservation effectuée avec succès.")

    def lister_reservations(self):
        for reservation in self.reservations:
            print(reservation)

    def get_reservation(self, id):
        for reservation in self.reservations:
            if reservation.id == id:
                return reservation
        return None
    
    def supprimer_reservation(self, id):
        self.reservations=[r for r in self.reservations if r.id != id]
        print(f"Réservation{id} supprimmée.")