### English Version

# Usage Instructions

Follow these steps to use the `phishing_campaign_tool`:

## Generate a Sample Email List

Generate a sample email list with a specified number of email addresses:

```bash
generate_email_list emails.txt 10
```

- **Output**: A file named `emails.txt` containing 10 sample email addresses.

## Run a Phishing Campaign

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

## Send Phishing Packets with Scapy

Send a phishing packet to a target IP and port using Scapy:

```bash
python phishing_campaign_tool/scapy_phishing.py 192.168.1.100 80 "This is a test payload"
```

- **Input**:
  - `192.168.1.100`: Target IP address.
  - `80`: Target port number.
  - `"This is a test payload"`: Payload to send.

## Run Unit Tests

To ensure everything is working correctly, run the unit tests provided with the project:

```bash
pytest
```

- **Output**: Results of the tests, indicating pass or fail status for each test case.

---

<p>&nbsp;</p>
<p>&nbsp;</p>

#### French Version

# Instructions d'Utilisation

Suivez ces étapes pour utiliser le `phishing_campaign_tool` :

## Générer une Liste d'Emails de Test

Générer une liste d'emails de test avec un nombre spécifié d'adresses email :

```bash
generate_email_list emails.txt 10
```

- **Sortie** : Un fichier nommé `emails.txt` contenant 10 adresses email de test.

## Lancer une Campagne de Phishing

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

## Envoyer des Paquets de Phishing avec Scapy

Envoyer un paquet de phishing à une IP cible et un port en utilisant Scapy :

```bash
python phishing_campaign_tool/scapy_phishing.py 192.168.1.100 80 "Ceci est une charge utile de test"
```

- **Entrée** :
  - `192.168.1.100` : Adresse IP cible.
  - `80` : Numéro de port cible.
  - `"Ceci est une charge utile de test"` : Charge utile à envoyer.

## Exécuter les Tests Unitaires

Pour s'assurer que tout fonctionne correctement, exécutez les tests unitaires fournis avec le projet :

```bash
pytest
```

- **Sortie** : Résultats des tests, indiquant le statut de réussite ou d'échec de chaque cas de test.