# Guide de déploiement - Convertisseur Airfryer

## Prérequis sur l'hébergement web

Votre hébergeur doit supporter :
- **Python 3.8+**
- **WSGI** (mod_wsgi pour Apache ou équivalent)
- Accès SSH ou panneau de contrôle pour installer les dépendances

## Fichiers nécessaires pour le déploiement

Les fichiers suivants doivent être uploadés sur votre serveur :

```
/votre-dossier/
├── app.py                    # Application Flask principale
├── page_template.py          # Template HTML
├── wsgi.py                   # Point d'entrée WSGI
├── .htaccess                 # Configuration Apache
└── requirements.txt          # Dépendances Python
```

## Instructions de déploiement

### 1. Upload des fichiers

Uploadez tous les fichiers listés ci-dessus dans le dossier de votre choix sur votre serveur (par exemple `/public_html/airfryer/` ou `/www/airfryer/`).

### 2. Installation des dépendances

Connectez-vous en SSH à votre serveur et naviguez vers le dossier :

```bash
cd /chemin/vers/votre-dossier
```

Installez les dépendances Python :

```bash
pip3 install -r requirements.txt --user
```

Ou si vous avez accès à un environnement virtuel :

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configuration du serveur

#### Option A : Hébergement avec cPanel ou Plesk

1. Accédez à la section "Python" ou "Applications Python"
2. Créez une nouvelle application Python
3. Définissez le chemin vers votre dossier
4. Définissez `wsgi.py` comme point d'entrée
5. Sélectionnez Python 3.8 ou supérieur

#### Option B : Configuration Apache manuelle

Le fichier `.htaccess` est déjà configuré pour rediriger les requêtes vers `wsgi.py`.

Assurez-vous que mod_wsgi est activé sur votre serveur Apache.

### 4. Vérification

Accédez à votre application via :
```
https://votre-domaine.com/airfryer/
```

L'application devrait afficher le convertisseur Four → Airfryer.

## Déploiement automatique avec GitHub Actions

Le workflow GitHub Actions (`.github/workflows/ftp-deploy.yml`) déploie automatiquement l'application sur votre serveur FTP.

### Configuration des secrets GitHub

1. Allez dans **Settings → Secrets and variables → Actions**
2. Ajoutez les secrets suivants :
   - `FTP_SERVER` : adresse de votre serveur FTP (ex: `ftp.example.com`)
   - `FTP_USERNAME` : votre nom d'utilisateur FTP
   - `FTP_PASSWORD` : votre mot de passe FTP

### Personnalisation du répertoire de destination

Modifiez la ligne `server-dir` dans `.github/workflows/ftp-deploy.yml` :

```yaml
server-dir: /public_html/airfryer/  # Changez selon votre structure
```

## Dépannage

### L'application ne se charge pas

- Vérifiez que Python 3.8+ est installé : `python3 --version`
- Vérifiez que Flask est installé : `pip3 list | grep Flask`
- Consultez les logs d'erreur de votre serveur

### Erreur 500

- Vérifiez les permissions des fichiers (644 pour les fichiers, 755 pour les dossiers)
- Vérifiez que le chemin dans `wsgi.py` est correct
- Consultez les logs Apache/WSGI

### Les dépendances ne s'installent pas

- Utilisez `pip3` au lieu de `pip`
- Ajoutez `--user` si vous n'avez pas les droits root
- Contactez votre hébergeur pour vérifier le support Python

## Support

Pour toute question, consultez la documentation de votre hébergeur concernant les applications Python/WSGI.
