#### English Version

# Phishing Campaign Tool

Welcome to the `phishing_campaign_tool` project. This professional-grade Python package is designed to create and manage phishing campaigns using email and Scapy. It includes comprehensive scripts and utilities to facilitate the setup and execution of phishing attacks for security testing purposes.

## Features

- Send phishing emails using customizable templates
- Manage phishing campaigns with multiple recipients
- Send phishing packets using Scapy
- Utility functions for loading email lists and templates
- Generate sample email lists for testing
- Comprehensive unit tests for all functionalities

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Tom-Souillard/phishing_campaign_tool.git
    cd phishing_campaign_tool
    ```

2. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install the package in editable mode**:
    ```bash
    pip install -e .
    ```

4. **Install Scapy dependencies**:
    - On Debian/Ubuntu:
      ```bash
      sudo apt-get install python3-scapy
      ```

## Usage

### Generate a Sample Email List

Generate a sample email list with a specified number of email addresses:

```bash
generate_email_list emails.txt 10
```

- **Output**: A file named `emails.txt` containing 10 sample email addresses.

### Run a Phishing Campaign

Run a phishing campaign by sending phishing emails to a list of recipients:

```bash
run_campaign "Phishing Subject" email_template.txt sender@example.com emails.txt smtp.example.com 587 smtp_login smtp_password
```

- **Input**: 
  - `Phishing Subject`: Subject of the phishing email.
  - `email_template.txt`: Path to the email template file.
  - `sender@example.com`: Sender's email address.
  - `emails.txt`: Path to the file containing the list of recipient email addresses.
  - `smtp.example.com`: SMTP server address.
  - `587`: SMTP server port.
  - `smtp_login`: SMTP server login.
  - `smtp_password`: SMTP server password.
- **Output**: Emails sent to the recipients listed in `emails.txt`.

### Send Phishing Packets with Scapy

Send a phishing packet to a target IP and port using Scapy:

```bash
python phishing_campaign_tool/scapy_phishing.py 192.168.1.100 80 "This is a test payload"
```

- **Input**:
  - `192.168.1.100`: Target IP address.
  - `80`: Target port number.
  - `"This is a test payload"`: Payload to send.

### Run Unit Tests

Run the unit tests to ensure the tool works correctly:

```bash
pytest
```

- **Output**: Results of the tests, indicating pass or fail status for each test case.

## Documentation

For detailed usage and customization instructions, please refer to the [documentation](docs/USAGE.md).

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING](CONTRIBUTING.md) guidelines before submitting a pull request.

---

#### French Version

# Outil de Campagne de Phishing

Bienvenue dans le projet `phishing_campaign_tool`. Ce package Python de qualité professionnelle est conçu pour créer et gérer des campagnes de phishing en utilisant l'email et Scapy. Il comprend des scripts et des utilitaires complets pour faciliter la configuration et l'exécution des attaques de phishing à des fins de tests de sécurité.

## Fonctionnalités

- Envoyer des emails de phishing en utilisant des modèles personnalisables
- Gérer des campagnes de phishing avec plusieurs destinataires
- Envoyer des paquets de phishing en utilisant Scapy
- Fonctions utilitaires pour charger des listes d'emails et des modèles
- Générer des listes d'emails de test
- Tests unitaires complets pour toutes les fonctionnalités

## Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de packages Python)

### Étapes

1. **Cloner le dépôt** :
    ```bash
    git clone https://github.com/Tom-Souillard/phishing_campaign_tool.git
    cd phishing_campaign_tool
    ```

2. **Installer les packages Python requis** :
    ```bash
    pip install -r requirements.txt
    ```

3. **Installer le package en mode édition** :
    ```bash
    pip install -e .
    ```

4. **Installer les dépendances de Scapy** :
    - Sur Debian/Ubuntu :
      ```bash
      sudo apt-get install python3-scapy
      ```

## Utilisation

### Générer une Liste d'Emails de Test

Générer une liste d'emails de test avec un nombre spécifié d'adresses email :

```bash
generate_email_list emails.txt 10
```

- **Sortie** : Un fichier nommé `emails.txt` contenant 10 adresses email de test.

### Lancer une Campagne de Phishing

Lancer une campagne de phishing en envoyant des emails de phishing à une liste de destinataires :

```bash
run_campaign "Sujet de Phishing" email_template.txt sender@example.com emails.txt smtp.example.com 587 smtp_login smtp_password
```

- **Entrée** :
  - `Sujet de Phishing` : Sujet de l'email de phishing.
  - `email_template.txt` : Chemin vers le fichier modèle de l'email.
  - `sender@example.com` : Adresse email de l'expéditeur.
  - `emails.txt` : Chemin vers le fichier contenant la liste des adresses email des destinataires.
  - `smtp.example.com` : Adresse du serveur SMTP.
  - `587` : Port du serveur SMTP.
  - `smtp_login` : Identifiant de connexion au serveur SMTP.
  - `smtp_password` : Mot de passe de connexion au serveur SMTP.
- **Sortie** : Emails envoyés aux destinataires listés dans `emails.txt`.

### Envoyer des Paquets de Phishing avec Scapy

Envoyer un paquet de phishing à une IP cible et un port en utilisant Scapy :

```bash
python phishing_campaign_tool/scapy_phishing.py 192.168.1.100 80 "Ceci est une charge utile de test"
```

- **Entrée** :
  - `192.168.1.100` : Adresse IP cible.
  - `80` : Numéro de port cible.
  - `"Ceci est une charge utile de test"` : Charge utile à envoyer.

### Exécuter les Tests Unitaires

Exécuter les tests unitaires pour s'assurer que l'outil fonctionne correctement :

```bash
pytest
```

- **Sortie** : Résultats des tests, indiquant le statut de réussite ou d'échec de chaque cas de test.

## Documentation

Pour des instructions détaillées sur l'utilisation et la personnalisation, veuillez consulter la [documentation](docs/USAGE.md).

## Licence

Ce projet est sous licence Apache License 2.0. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Contribuer

Les contributions sont les bienvenues ! Veuillez lire les lignes directrices de [CONTRIBUTING](CONTRIBUTING.md) avant de soumettre une demande de tirage.