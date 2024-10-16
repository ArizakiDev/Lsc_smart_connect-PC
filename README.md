# 🎥 Lsc Smart Connect pc - Application Python avec Tkinter

> Un outil simple pour se connecter aux appareils **LSC Smart Connect** et visualiser les caméras en utilisant l'API **Tuya** avec une interface utilisateur **Tkinter**.

## 🚀 Fonctionnalités

- 🔑 Connexion à l'API **Tuya** pour accéder aux appareils **LSC Smart Connect**.
- 📋 Liste des appareils connectés (caméras, capteurs, etc.).
- 🔍 Affichage des informations détaillées sur chaque appareil.
- 💡 Interface utilisateur simple avec **Tkinter**.

## 🛠️ Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants :

- 🐍 **Python 3.7** ou supérieur installé.
- 🖥️ Un compte développeur **Tuya IoT** ([Créer un compte ici](https://iot.tuya.com)).
- 🔑 Les **ACCESS_ID** et **ACCESS_KEY** de votre projet **Tuya**.
- 📱 Votre **nom d'utilisateur (email)** et **mot de passe** de l'application **LSC Smart Connect**.

## 🛠️ Installation

1. Clonez ce dépôt GitHub dans votre environnement local :

```bash
git clone https://github.com/ArizakiDev/Lsc_smart_connect-PC.git
cd lsc_smart_connect-PC
```

2. Installez les dépendances nécessaires :

```bash
pip install -r requirements.txt
```

3. Modifiez le fichier **`main.py`** pour inclure vos informations d'authentification **Tuya** (🛠️ Remplacez les valeurs par vos propres informations) :

```python
ACCESS_ID = "ton_access_id"  # Remplacez avec votre ACCESS_ID Tuya
ACCESS_KEY = "ton_access_key"  # Remplacez avec votre ACCESS_KEY Tuya
API_REGION = "eu"  # Modifiez la région si nécessaire (eu, us, cn, in)
USERNAME = "ton_email"  # L'email de votre compte LSC Smart Connect
PASSWORD = "ton_mot_de_passe"  # Le mot de passe associé à ce compte
```

## ⚙️ Configuration du compte développeur Tuya

1. **Créer un compte développeur sur Tuya IoT Platform :**
   - Rendez-vous sur [iot.tuya.com](https://iot.tuya.com) et inscrivez-vous ou connectez-vous.
   
2. **Créer un projet :**
   - Après vous être connecté, créez un nouveau projet. Assurez-vous de choisir les bonnes **régions** et **industries** pour votre projet.
   
3. **Lier votre application LSC Smart Connect au projet :**
   - Allez dans **"Cloud Development"** > **"Devices"** > **"Link Tuya App Account"** et suivez les instructions pour associer votre compte **LSC Smart Connect** au projet IoT Tuya.

4. **Obtenir les `ACCESS_ID` et `ACCESS_KEY` :**
   - Une fois que votre projet est configuré, rendez-vous dans **"Project Overview"** pour obtenir votre **`ACCESS_ID`** et **`ACCESS_KEY`**.

## ▶️ Utilisation

1. **Lancer l'application** :

   Après avoir configuré vos identifiants dans le fichier **`main.py`**, lancez l'application en utilisant la commande suivante :

   ```bash
   python main.py
   ```

2. **Connexion réussie :**
   - Si la connexion à l'API est réussie, un message de succès s'affichera 🎉.
   
3. **Liste des appareils :**
   - La liste des appareils connectés à votre compte s'affichera dans l'interface Tkinter. Sélectionnez un appareil pour afficher ses détails.

## 🌐 Support des régions

Assurez-vous que le paramètre **`API_REGION`** dans le fichier **`main.py`** correspond à la région de votre compte Tuya. Voici les options disponibles :

- 🌍 `eu` (Europe)
- 🇺🇸 `us` (Amérique du Nord)
- 🇨🇳 `cn` (Chine)
- 🇮🇳 `in` (Inde)

## 🔄 Commandes supplémentaires

Vous pouvez ajouter des fonctionnalités supplémentaires comme l'accès au flux vidéo des caméras ou la commande des appareils en utilisant l'API Tuya. Consultez la documentation officielle de l'API Tuya pour plus d'informations.

## 📄 License

Ce projet est sous licence MIT.
