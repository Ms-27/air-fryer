# Convertisseur Four → Airfryer

Application web pour convertir les températures et temps de cuisson d'un four traditionnel vers un airfryer.

## � Structure du projet

```
air-fryer/
├── index.html          # Structure HTML
├── styles.css          # Styles et design
├── app.js              # Logique métier et interactions
├── .htaccess           # Configuration Apache
├── .github/
│   └── workflows/
│       └── ftp-deploy.yml  # CI/CD automatique
└── README.md
```

## �🚀 Déploiement

Cette application utilise **HTML/CSS/JavaScript pur** et fonctionne sur n'importe quel hébergement web.

### Fichiers déployés

Fichiers nécessaires sur votre serveur :
- `index.html` - Structure de l'application
- `styles.css` - Feuille de styles
- `app.js` - Logique JavaScript
- `.htaccess` - Configuration Apache (optionnel)

### Déploiement automatique

Le workflow GitHub Actions déploie automatiquement sur votre serveur FTP/SFTP à chaque push sur `master`.

**Secrets GitHub requis :**
- `OVH_FTP_SERVER` - Adresse du serveur
- `OVH_FTP_USERNAME` - Nom d'utilisateur
- `OVH_FTP_PASSWORD` - Mot de passe

### Accès

Une fois déployé, accédez à : `votre-site.com/airfry/`

## 🛠️ Développement local

Ouvrez simplement `index.html` dans votre navigateur. Aucune installation nécessaire.

## 📋 Fonctionnalités

- Conversion température : -15°C
- Conversion temps : -20%
- Mémorisation des valeurs fréquentes (localStorage)
- Suggestions rapides basées sur l'historique
- Interface responsive et moderne

## 🏗️ Architecture

Le projet suit les bonnes pratiques du développement web :
- **Séparation des préoccupations** : HTML, CSS et JavaScript dans des fichiers distincts
- **Code modulaire** : Fonctions réutilisables et bien nommées
- **Clean code** : Code lisible et maintenable
- **Progressive enhancement** : Fonctionne sans JavaScript (formulaire de base)

