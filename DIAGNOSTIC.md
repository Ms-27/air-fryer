# Diagnostic du problème 404

## Étape 1 : Identifier votre type d'hébergement

Accédez à `mon-site.com/airfry/info.php` dans votre navigateur.

### Résultat possible :

#### ✅ Vous voyez une page avec plein d'informations PHP
→ **Votre hébergement supporte PHP mais probablement pas Python**
→ **Solution : Utilisez la version HTML statique (voir ci-dessous)**

#### ❌ Erreur 404 ou page blanche
→ **Votre hébergement ne supporte peut-être que HTML/CSS/JS**
→ **Solution : Utilisez la version HTML statique (voir ci-dessous)**

#### ✅ Vous voyez des informations avec "Python" ou "WSGI"
→ **Votre hébergement supporte Python**
→ **Solution : Configuration WSGI nécessaire (voir DEPLOIEMENT.md)**

---

## Solution immédiate : Version HTML statique

J'ai créé `index.html` - une version 100% JavaScript qui fonctionne sur n'importe quel hébergement.

### ✅ Avantages
- Fonctionne partout (même hébergement statique)
- Aucune configuration serveur nécessaire
- Même fonctionnalité que la version Flask
- Stockage local des valeurs fréquentes

### 📋 Pour l'utiliser

Le fichier `index.html` est déjà dans votre repo et sera déployé automatiquement.

**Accédez simplement à :** `mon-site.com/airfry/` ou `mon-site.com/airfry/index.html`

---

## Si vous voulez absolument utiliser la version Python

### Vérifications nécessaires

1. **Votre hébergeur supporte-t-il Python ?**
   - Connectez-vous en SSH : `python3 --version`
   - Si erreur → Python non supporté, utilisez `index.html`

2. **WSGI est-il configuré ?**
   - Vérifiez si mod_wsgi est installé (Apache)
   - Ou si votre hébergeur a une interface "Applications Python"

3. **Structure des fichiers**
   ```
   /home/juliver/www/airfry/
   ├── app.py
   ├── page_template.py
   ├── wsgi.py
   ├── .htaccess
   ├── requirements.txt
   └── index.html (fallback)
   ```

4. **Permissions**
   ```bash
   chmod 644 *.py
   chmod 644 .htaccess
   chmod 755 /home/juliver/www/airfry/
   ```

5. **Installation des dépendances**
   ```bash
   cd /home/juliver/www/airfry/
   pip3 install -r requirements.txt --user
   ```

### Configuration cPanel (si disponible)

1. Allez dans **Setup Python App**
2. Créez une nouvelle application :
   - Python version : 3.8+
   - Application root : `/home/juliver/www/airfry`
   - Application URL : `/airfry`
   - Application startup file : `wsgi.py`
   - Application Entry point : `application`

---

## Recommandation

**Pour la plupart des hébergements mutualisés (OVH, etc.) :**

👉 **Utilisez `index.html`** - c'est la solution la plus simple et fiable.

La version Python est utile si vous avez besoin de :
- Traitement côté serveur complexe
- Base de données
- API externes avec clés secrètes

Pour un simple convertisseur comme celui-ci, la version HTML/JavaScript est parfaite et plus rapide !

---

## Test rapide

1. Allez sur `mon-site.com/airfry/`
2. Si vous voyez le convertisseur → ✅ Ça marche !
3. Entrez 200°C et 20 minutes
4. Cliquez sur "Convertir"
5. Vous devriez voir : 185°C et 16 minutes

---

## Besoin d'aide ?

Si `index.html` ne fonctionne toujours pas :
1. Vérifiez que le fichier est bien uploadé
2. Vérifiez les permissions (644)
3. Essayez d'accéder directement à `mon-site.com/airfry/index.html`
4. Vérifiez les logs d'erreur de votre hébergeur
