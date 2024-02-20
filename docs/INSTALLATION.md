### English Version

# Installation Instructions

Follow these steps to install the `phishing_campaign_tool`:

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Tom-Souillard/phishing_campaign_tool.git
    cd phishing_campaign_tool
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install the package in editable mode**:
    ```bash
    pip install -e .
    ```

5. **Install Scapy dependencies**:
    - On Debian/Ubuntu:
      ```bash
      sudo apt-get install python3-scapy
      ```

6. **(Optional) Install Npcap for Windows users**:
    - Download and install Npcap from [Npcap Download](https://nmap.org/npcap/)
    - Ensure that "Install Npcap in WinPcap API-compatible Mode" is checked during installation.

## Verifying the Installation

To verify that the installation was successful, you can run one of the included scripts:

```bash
generate_email_list emails.txt 10
```

If this command executes without errors and generates a file `emails.txt` with 10 email addresses, the installation was successful.

## Running Unit Tests

To ensure everything is working correctly, you can run the unit tests:

```bash
pytest
```

---

<p>&nbsp;</p>
<p>&nbsp;</p>

### French Version

# Instructions d'Installation

Suivez ces étapes pour installer le `phishing_campaign_tool` :

## Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de packages Python)

## Étapes

1. **Cloner le dépôt** :
    ```bash
    git clone https://github.com/Tom-Souillard/phishing_campaign_tool.git
    cd phishing_campaign_tool
    ```

2. **Créer et activer un environnement virtuel** (optionnel mais recommandé) :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows : venv\Scripts\activate
    ```

3. **Installer les packages Python requis** :
    ```bash
    pip install -r requirements.txt
    ```

4. **Installer le package en mode édition** :
    ```bash
    pip install -e .
    ```

5. **Installer les dépendances de Scapy** :
    - Sur Debian/Ubuntu :
      ```bash
      sudo apt-get install python3-scapy
      ```

6. **(Optionnel) Installer Npcap pour les utilisateurs de Windows** :
    - Téléchargez et installez Npcap depuis [Npcap Download](https://nmap.org/npcap/)
    - Assurez-vous que l'option "Install Npcap in WinPcap API-compatible Mode" est cochée pendant l'installation.

## Vérification de l'Installation

Pour vérifier que l'installation s'est déroulée avec succès, vous pouvez exécuter l'un des scripts inclus :

```bash
generate_email_list emails.txt 10
```

Si cette commande s'exécute sans erreur et génère un fichier `emails.txt` contenant 10 adresses email, l'installation a été réussie.

## Exécution des Tests Unitaires

Pour s'assurer que tout fonctionne correctement, vous pouvez exécuter les tests unitaires :

```bash
pytest
```
