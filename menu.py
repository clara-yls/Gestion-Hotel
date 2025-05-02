from hotel import Hotel
from client import Client
from chambre import ChambreDouble, ChambreSimple, ChambreSuite
from reservation import Reservation
#Creation du menu interface utilisateur
def clear_console():
    print("\n" * 20)

def afficher_menu():
    print("Bonjour, application de gestion des chambres de l'Hotel YLS")
    print("1. Ajouter un client")
    print("2. Ajouter une chambre")
    print("3. Faire une reservation")
    print("4. Afficher tout les clients") 
    print("5. Afficher toutes les chambres")
    print("6. Afficher toutes les reservations")
    print("7. Supprimer un client")
    print("8. Supprimer une chambre")
    print("9. Supprimer une réservation")
    print("10. Rechercher un client / chambre / réservation par ID")
    print("q. Quitter")

def main():
    hotel = Hotel()
    client_id = chambre_id = reservation_id = 1

    while True:
        clear_console()
        afficher_menu()
        choix = input("Faites votre choix: ").strip().lower()
        if choix == "1":
            clear_console()
            nom = input("Nom du client: ")
            prenom= input("Prenom du client: ")
            nouveau_client= Client(client_id,nom,prenom)
            hotel.ajouter_client(nouveau_client)
            client_id += 1
            print("Client ajouter avec sucess")
            input("Appuyez sur Entrée pour revenir au menu...")

        elif choix=="2":
            clear_console()
            numero = int(input("Numero de chambre: "))
            type_chambre = input("Type(simple,double,suite): ").lower()
            prix= float(input("Prix par nuit: "))
            if type_chambre == "simple" :
                nouvelle_chambre= ChambreSimple(chambre_id,numero,prix)
            elif type_chambre == "double":
                nouvelle_chambre= ChambreDouble(chambre_id,numero,prix)
            elif type_chambre == "suite":
                nouvelle_chambre= ChambreSuite(chambre_id,numero,prix)
            else:
                print("Type de chambre invalide")
                continue
            hotel.ajouter_chambre(nouvelle_chambre)
            chambre_id += 1
            print("Chambre ajouter avec sucess")
            input("Appuyez sur Entrée pour revenir au menu...")

        elif choix == "3":
            clear_console()
            date_arrivee = input("Date d'arrivée (YYYY-MM-DD) : ")
            date_depart = input("Date de départ (YYYY-MM-DD) : ")
            hotel.lister_clients()
            client_id_choisi = int(input("ID du client : "))
            hotel.lister_chambres()
            chambre_id_choisi = int(input("ID de la chambre : "))
            reservation = Reservation(reservation_id, date_arrivee, date_depart, client_id_choisi, chambre_id_choisi)
            hotel.ajouter_reservation(reservation)
            reservation_id += 1
            input("Appuyez sur Entrée pour revenir au menu...")
        
        elif choix == "4":
            clear_console()
            hotel.lister_clients()
            input("Appuyez sur Entrée pour revenir au menu...")

        elif choix == "5":
            clear_console()
            hotel.lister_chambres()
            input("Appuyez sur Entrée pour revenir au menu...")

        elif choix == "6":
            clear_console()
            hotel.lister_reservations()
            input("Appuyez sur Entrée pour revenir au menu...")

        elif choix == "7":
            clear_console()
            id = int(input("ID client à supprimer: "))
            hotel.supprimer_client(id)
            input("Appuyez sur Entrée pour revenir au menu...")

        elif choix == "8":
            clear_console()
            id = int(input("ID chambre à supprimer: "))
            hotel.supprimer_chambre(id)
            input("Appuyez sur Entrée pour revenir au menu...")

        elif choix == "9":
            clear_console()
            id = int(input("ID réservation à supprimer: "))
            hotel.supprimer_reservation(id)
            input("Appuyez sur Entrée pour revenir au menu...")

        elif choix == "10":
            clear_console()
            print("\n --- Recherche par ID ---")
            print("1. Rechercher un client")
            print("2. Rechercher une chambre")
            print("3. Rechercher une réservation")
            sous_choix = input("Choisissez une option: ")

            if sous_choix == "1":
                id_recherche = int(input("ID du client: "))
                client = hotel.get_client_par_id(id_recherche)
                if client:
                    print(client)
                else:
                    print("Client non trouvé.")
            elif sous_choix == "2":
                id_recherche = int(input("ID de la chambre: "))
                chambre= hotel.get_chambre_par_id(id_recherche)
                if chambre:
                    print(chambre)
                else:
                    print("Chambre pas trouvé.")
            elif sous_choix == "3":
                id_recherche = int(input("ID de la reservation"))
                reservation = hotel.get_reservation(id_recherche)
                if reservation:
                    print(reservation)
                else:
                    print("Reservation non trouvé.")
            else:
                print("Choix invalide.")

            input("Appuyez sur Entrée pour revenir au menu...")


        elif choix == "0":
            clear_console()
            print("Fermeture de l'application. À bientôt !")
            break

        else:
            clear_console()
            print("Choix invalide. Réessaie.")
            input("Appuyez sur Entrée pour revenir au menu...")

if __name__ == "__main__":
    main()

            