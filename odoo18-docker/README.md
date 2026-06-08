README Ecrit à l'aide de l'ia

# Odoo 18 — Use Case Technique

Modules développés dans le cadre d'un exercice de recrutement pour idealis.

---

## Prérequis

- [Docker](https://docs.docker.com/get-docker/) installé
- [Docker Compose](https://docs.docker.com/compose/install/) installé
- Ports `8069` libre sur la machine

---

## Installation & Lancement

### 1. Cloner / décompresser le projet

```
projet/
├── docker-compose.yml
├── addons/
│   ├── real_estate_sale/
│   └── parking_management/
└── README.md
```

### 2. Permissions du dossier addons (Linux/Bazzite)

```bash
chmod -R 777 addons/
sudo chcon -Rt svirt_sandbox_file_t addons/   # si SELinux actif
```

### 3. Lancer les containers

```bash
docker compose up -d
```

### 4. Créer la base de données

Ouvrir http://localhost:8069/web/database/manager

| Champ | Valeur suggérée |
|-------|----------------|
| Master Password | `admin` |
| Database Name | `odoo18` |
| Email | `admin@example.com` |
| Password | `admin` |
| Language | Français |
| Country | Belgique |

Cocher **Demo data** pour avoir des données de test.

### 5. Installer les modules prérequis

Depuis **Apps**, installer dans cet ordre :
1. **Sales** (ventes)
2. **eCommerce** (website_sale)

### 6. Installer les modules custom

- Apps → **Update Apps List** (nécessite le mode développeur)
- Activer le mode développeur : Settings → Developer Tools → Activate
- Apps → Update Apps List
- Rechercher et installer **Real Estate Sale**
- Rechercher et installer **Parking Management**

---

## Commandes utiles

```bash
# Voir les logs en temps réel
docker compose logs -f odoo

# Redémarrer Odoo (changements Python)
docker compose restart odoo

# Mettre à jour un module (changements de modèles/vues)
docker compose exec odoo odoo -u real_estate_sale -d odoo18 --stop-after-init
docker compose exec odoo odoo -u parking_management -d odoo18 --stop-after-init

# Arrêter les containers
docker compose down

# Repartir de zéro (supprime la base de données)
docker compose down -v
```

---

## Modules

### Module 1 — Real Estate Sale

> Voir [addons/real_estate_sale/README.md](addons/real_estate_sale/README.md)

### Module 2 — Parking Management

> Voir [addons/parking_management/README.md](addons/parking_management/README.md)
