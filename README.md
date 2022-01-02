# nox-demo

C'est un simple package d'exemple écrit en [Markdown](https://guides.github.com/features/mastering-markdown/)

## Création de l'environnement virtuel dans le répertoire .nox

`nox --install-only`

## Formatage et analyse statique du code

`nox -rs format`

## Execution des tests unitires

`nox -rs test`

## Création du package dans le répertoire dist

`nox -rs package`

## Génération de la documentation du projet dans le répertoire docs

`nox -rs docs`

## Execution des tâches de formatage et de tests sans redeployer les librairies

`nox --reuse-existing-virtualenvs --no-install`

## Suppression des fichiers et répertoires générés

`./clear_env.sh`

## Les fichiers

 Nom du fichier  | Description  
|- | - 
| `LICENSE` | `licence du programme` 
| `README.md` | `ce fichier` 
| `.gitignore` | `chemins à ignorer pour git` 
| `clear_env.sh` | `Scripte de nettoyage` 
| `mypy.ini` | `configuration pour mypy` 
| `.flake8` | `configuration pour flake8` 
| `noxfile.py` | `les tâches NOX` 
| `requirements.txt` | `les librairies Python` 
| `setup.py` | `fichier de construction du package` 



## Les répertoires

 Nom du fichier  | Description  
|- | - 
| `.vscode` | `la configuration pour vscode` 
| `mylib` | `les sources Python` 
| `tests` | `les fichiers de tests unitaires` 
| `docs` | `la documentation du programme` 

## Licence
MIT