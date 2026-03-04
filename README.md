# Convertisseur Four → Airfryer

Application web pour convertir les températures et temps de cuisson d'un four traditionnel vers un airfryer.

## 🚀 Déploiement

Cette application utilise **HTML/JavaScript pur** et fonctionne sur n'importe quel hébergement web.

### Fichiers déployés

Seuls ces fichiers sont nécessaires sur votre serveur :
- `index.html` - Application complète
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

## 🔧 Version Python (archive)

Les fichiers Python (`app.py`, `page_template.py`, `wsgi.py`) sont conservés dans le repo mais ne sont plus déployés. La version HTML offre les mêmes fonctionnalités sans nécessiter de configuration serveur complexe.
