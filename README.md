# SynthèseAI

## Description
SynthèseAI est une application web de résumé automatique de texte utilisant des algorithmes d'intelligence artificielle. Elle permet aux utilisateurs de générer rapidement des résumés concis à partir de textes longs, offrant un gain de temps précieux pour la lecture et l'analyse de documents.

## Fonctionnalités
- Résumé automatique de texte
- Choix de la langue (Français, Anglais, Espagnol, Allemand)
- Sélection de l'algorithme de résumé (LSA, TextRank, LexRank)
- Personnalisation du nombre de phrases du résumé
- Interface responsive avec mode sombre/clair

## Technologies utilisées
- Python 3.9+
- Flask
- Sumy (pour les algorithmes de résumé)
- NLTK
- HTML/CSS/JavaScript

## Installation

1. Clonez le dépôt :

git clone https://github.com/votre-username/syntheseai.git
cd syntheseai

2. Créez un environnement virtuel et activez-le :
python -m venv venv
source venv/bin/activate  # Sur Windows, utilisez : venv\Scripts\activate

3. Installez les dépendances :
pip install -r requirements.txt

4. Téléchargez les données nécessaires pour NLTK :
python -c "import nltk; nltk.download('punkt')"

## Utilisation

1. Lancez l'application :
python app.py

2. Ouvrez votre navigateur et accédez à `http://localhost:5000`

3. Entrez ou collez votre texte dans la zone prévue à cet effet

4. Choisissez la langue, l'algorithme et le nombre de phrases souhaité

5. Cliquez sur "Résumer" pour obtenir votre résumé

## Déploiement
Cette application est conçue pour être facilement déployable sur des plateformes comme Vercel. Consultez la documentation de Vercel pour plus de détails sur le déploiement.

## Contribution
Les contributions à ce projet sont les bienvenues. N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence
[MIT License](https://opensource.org/licenses/MIT)

## Contact
Votre Nom - [mathieu.soussignan@hotmail.fr](mailto:mathieu.soussignan@hotmail.fr)

Lien du projet : [https://github.com/votre-username/syntheseai](https://github.com/votre-username/syntheseai)
