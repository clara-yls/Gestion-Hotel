# Gestion de Chambre d'Hotel 
**Par Clara YOUTA**

---

## 📕 Description
Ce projet est une application console en Python qui permet de gérer la réservation
de chambre d'hotel (dans ceux cas c'est celui de l'hotel YLS). Il permet d'ajouter, de supprimer, de visualiser et consulter les clients, chamnres et réservations tout en respectent certaines contraintes de gestion comme ne pas réserver une chambre déjà réservé.

---

## 💡 Fonctionnalités principales

- Ajouter, consulter, supprimer un **client**
- Ajouter, consulter, supprimer un **chambre** (simple, double ou suite)
- Faire une **réservation**
  - Vérifie automatiquement les disponibilité de la chambre aux dates demandées
- Supprimer un client seulement s'il n'a pas de réservation actives
- Supprimer une chambre seulement si elle n'est pas réservée
- Supprimer une réservation
- Lister ou rechercher (via 'get_...') un client, une chambre ou une réservation

---

## 🗂️ Organisation du code
- 'menu.py' : menu interactif principal et éxecution du programme
- 'hotel.py' :  gestion des opérations sur les clients, chambres et réservations
- 'client.py', 'chambre.py', 'reservation.py' : définition des classes

---
**Fait le 01-05-2025**