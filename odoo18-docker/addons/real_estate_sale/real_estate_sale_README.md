Readme écrit à l'aide de l'ia

# Module : Real Estate Sale

**Version :** 18.0.1.0.0
**Dépendances :** `sale_management`, `analytic`, `account`, `website_sale`

---

## Description

Ce module permet d'associer un **projet immobilier** à un bon de commande de vente.
Il couvre 3 exercices techniques : backend, frontend shop et rapport PDF.

---

## Fonctionnalités

### Exercice 1 — Backend

**Modèle `real.estate.project`**

| Champ | Type | Description |
|-------|------|-------------|
| name | Char | Nom du projet |
| analytic_account_id | Many2one | Compte analytique lié (optionnel) |
| description | Text | Description libre |
| status | Selection | `planned` / `in_progress` / `done` |

**Héritage `sale.order`**

- Nouveau champ `real_estate_project_id` sur le bon de commande
- Lors de la sélection d'un projet, le compte analytique est automatiquement appliqué sur toutes les lignes de commande (`onchange` + `write`)
- Les distributions analytiques existantes sont préservées si complexes (plusieurs comptes)
- **Bandeau d'alerte orange** affiché si le projet sélectionné est en statut "Terminé"
- Le changement de projet après enregistrement recalcule la distribution (cohérence garantie)

**Menu**

`Immobilier → Projets`

---

### Exercice 2 — Frontend Shop

**Route :** `GET/POST /shop/project`

Page publique accessible depuis le tunnel de commande eCommerce permettant de :
- Visualiser tous les projets immobiliers avec leur statut (badge coloré)
- Sélectionner un projet à associer à la commande en cours
- Afficher un **message d'avertissement** si le projet sélectionné est en statut "Terminé" (non bloquant)

> ⚠️ Cette page nécessite une commande active (produit dans le panier).

---

### Exercice 3 — Rapport PDF

Le projet immobilier associé est affiché dans le **rapport PDF du bon de commande** :
- Nom du projet
- Statut du projet (Planifié / En cours / Terminé)

Accessible via : Bon de commande → Imprimer → Bon de commande

---

## Structure des fichiers

```
real_estate_sale/
├── __manifest__.py
├── __init__.py
├── models/
│   ├── __init__.py
│   ├── real_estate_project.py   ← modèle central
│   └── sale_order.py            ← héritage sale.order
├── views/
│   ├── real_estate_project_views.xml
│   └── sale_order_views.xml
├── report/
│   └── sale_order_report.xml    ← héritage rapport PDF
├── controllers/
│   ├── __init__.py
│   └── main.py                  ← route /shop/project
├── templates/
│   └── website_project.xml      ← template QWeb frontend
├── static/src/js/
│   └── project_select.js        ← warning temps réel
└── security/
    └── ir.model.access.csv
```

---

## Points techniques notables

- Utilisation de `@api.depends` pour le champ computed `is_project_done`
- Gestion de la distribution analytique via le champ `Json` `analytic_distribution` (clés en `str`)
- Double déclenchement `onchange` (UI) + `write` (API/scripts) pour garantir la cohérence
- Attribut `invisible=` Odoo 18 (remplace `attrs` déprécié)
- Balise `<list>` à la place de `<tree>` (Odoo 17+)
- XPath ancré sur des éléments stables (`field[@name='partner_id']`, `div[@name='informations_reference']`)
