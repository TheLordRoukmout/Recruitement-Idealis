Readme écrit à l'aide de l'ia

# Module : Parking Management

**Version :** 18.0.1.0.0
**Dépendances :** `base`, `website`

---

## Description

Module de gestion d'un parking avec suivi des clients abonnés et affichage
en temps réel de la disponibilité des places via une page web publique.

---

## Fonctionnalités

### Backend

**Modèle `parking.client`**

| Champ | Type | Description |
|-------|------|-------------|
| first_name | Char | Prénom du client |
| last_name | Char | Nom du client |
| license_plate | Char | Immatriculation du véhicule |
| subscription_paid | Boolean | Abonnement payé ou non |
| full_name | Char (computed) | Prénom + Nom (utilisé comme `_rec_name`) |

**Modèle `parking.place`**

| Champ | Type | Description |
|-------|------|-------------|
| name | Char | Numéro de la place (ex: P1, P2...) |
| is_available | Boolean | Disponible (`True`) ou occupée (`False`) |

**Menu**

```
Parking
├── Clients
└── Places
```

---

### Frontend — Page publique

**Route :** `GET /parking`

Page accessible sans authentification affichant :

- **Compteurs** : total des places, disponibles, occupées
- **Grille visuelle** des places avec code couleur :
  - 🟢 Vert — place libre
  - 🔴 Rouge — place occupée
- **Auto-refresh** toutes les 10 secondes (rechargement de page)
- Header et footer Odoo masqués (page épurée)

---

## Utilisation

### 1. Créer des places de parking

`Parking → Places → Nouveau`

Créer autant de places que nécessaire (P1, P2, A1, B3, etc.) et définir leur disponibilité initiale.

### 2. Créer des clients

`Parking → Clients → Nouveau`

Renseigner les informations du client et son statut d'abonnement.

### 3. Consulter la disponibilité

Ouvrir `http://localhost:8069/parking`

La page se rafraîchit automatiquement toutes les 10 secondes.
Pour modifier la disponibilité d'une place en temps réel, modifier le champ `Disponible` depuis le backend.

---

## Structure des fichiers

```
parking_management/
├── __manifest__.py
├── __init__.py
├── models/
│   ├── __init__.py
│   ├── parking_client.py
│   └── parking_place.py
├── views/
│   ├── parking_client_views.xml
│   └── parking_place_views.xml
├── controllers/
│   ├── __init__.py
│   └── main.py
├── templates/
│   └── parking_website.xml
└── security/
    └── ir.model.access.csv
```

---

## Points techniques notables

- Champ `full_name` computed avec `@api.depends` utilisé comme `_rec_name`
- Accès public via `sudo()` sur les modèles (lecture seule pour les visiteurs)
- Auto-refresh côté client via `setTimeout` + `window.location.reload()`
- Page épurée sans header/footer via `t-set="no_header"` et `t-set="no_footer"`
- Droits d'accès séparés : lecture publique, CRUD pour les utilisateurs internes
