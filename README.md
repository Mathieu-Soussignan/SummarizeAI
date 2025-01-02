# SynthèseAI

## Description

SynthèseAI est une application web de résumé automatique de texte utilisant des algorithmes d'intelligence artificielle. Elle permet aux utilisateurs de générer rapidement des résumés concis à partir de textes longs, offrant un gain de temps précieux pour la lecture et l'analyse de documents.

---

## Fonctionnalités

- Résumé automatique de texte
- Choix de la langue (Français, Anglais, Espagnol, Allemand)
- Sélection de l'algorithme de résumé (LSA, TextRank, LexRank)
- Personnalisation du nombre de phrases du résumé
- Interface responsive avec mode sombre/clair

&#x20;

---

## Exemple d'utilisation

### Texte d'entrée :

> "La technologie de l'intelligence artificielle connaît une croissance rapide, révolutionnant les industries à travers le monde."

### Résumé généré (2 phrases, algorithme : LSA, langue cible : anglais) :

> "Artificial intelligence is growing rapidly. It is revolutionizing industries worldwide."

---

## Installation

### Étape 1 : Clonez le dépôt

```bash
git clone https://github.com/Mathieu-Soussignan/SummarizeAI.git
cd SummarizeAI
```

### Étape 2 : Créez un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

### Étape 3 : Installez les dépendances

```bash
pip install -r requirements.txt
```

### Étape 4 : Téléchargez les données NLTK

```bash
python -c "import nltk; nltk.download('punkt')"
```

---

## Utilisation

1. Lancez l'application :

```bash
python app.py
```

2. Ouvrez votre navigateur et accédez à `http://localhost:5000`

3. Entrez ou collez votre texte dans la zone prévue à cet effet

4. Choisissez la langue, l'algorithme et le nombre de phrases souhaité

5. Cliquez sur "Résumer" pour obtenir votre résumé

---

## Déploiement

Cette application est conçue pour être facilement déployable sur des plateformes comme Vercel.

### Étapes de déploiement sur Vercel

1. Assurez-vous d'avoir un compte Vercel.
2. Clonez le dépôt GitHub et poussez-le sur votre propre repository.
3. Liez votre repository à Vercel.
4. Assurez-vous que le fichier `vercel.json` est bien configuré :
   ```json
   {
       "builds": [
           { "src": "app.py", "use": "@vercel/python" }
       ],
       "routes": [
           { "src": "/(.*)", "dest": "app.py" }
       ]
   }
   ```
5. Déployez votre application depuis le tableau de bord Vercel.

---

## Contribution

Les contributions à ce projet sont les bienvenues. N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

---

## FAQ

### 1. Quelle est la longueur maximale du texte ?

Actuellement, le texte est limité à environ 5000 caractères pour garantir des performances optimales.

### 2. Puis-je utiliser l'application sur mobile ?

Oui, l'interface est responsive et s'adapte aux appareils mobiles.

### 3. Quels algorithmes sont pris en charge ?

SynthèseAI prend en charge les algorithmes LSA, TextRank et LexRank.

---

## Licence

[MIT License](https://opensource.org/licenses/MIT)

---

## Contact

Mon mail - [contact.mathieu.soussignan@gmail.com](mailto\:contact.mathieu.soussignan@gmail.com)

Lien du projet : [https://github.com/Mathieu-Soussignan/SummarizeAI](https://github.com/Mathieu-Soussignan/SummarizeAI)