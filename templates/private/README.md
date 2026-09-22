# Modèle du dépôt privé

Ce dossier est un **squelette générique**, pas la copie de l'instance de l'auteur.
Les seize fichiers de `files/` sont copiés à la racine du dépôt privé choisi ;
`templates/private/` n'est pas reproduit dans la destination.
Le [manifeste](manifest.json) donne la liste exacte, les chemins et empreintes SHA-256.
Ne copier ni l'historique public, ni un dépôt privé existant, ni des données d'exemple réelles.

## Utilisation normale : une conversation

Le paragraphe du [README principal](../../README.md) charge
[instructions/INSTALLATION.md](../../instructions/INSTALLATION.md).
Chat lit les fichiers à un SHA unique, vérifie les empreintes, substitue les cinq
variables techniques, écrit le dépôt privé et relit le résultat. Puis il complète
les réglages et le mandat par dialogue, teste réellement et raccorde le scheduler.
Les paramètres métier ne sont pas des remplacements textuels : Chat modifie le
JSON analysé, après validation du propriétaire, sans interpolation de texte arbitraire.

## Variables de génération

| Variable | Valeur à obtenir, jamais une donnée de l'auteur |
| --- | --- |
| PRIVATE_REPO | `proprietaire/nom` choisi, propriétaire vérifié. |
| PRIVATE_BRANCH | Branche convenue et réellement disponible. |
| KIT_SHA | SHA de 40 caractères résolu sur main du kit pour cette installation. |
| INSTALLATION_ID | Identifiant unique généré, conservé lors des reprises. |
| RENDERED_AT_UTC | Heure réelle de préparation, ISO 8601 UTC, pas une preuve de publication. |

Les tableaux d'affaires, décisions, abonnements et préférences sont vides.
Le contrôle et la tâche de départ sont inactifs. Ce n'est pas l'état final :
INSTALLATION.md explique leur activation après accord, avant le premier cycle réel.
Aucun compte Gmail, destinataire, fuseau, heure, identifiant de tâche ou mandat
personnel n'est prérempli. Les preuves et checkpoints sont inconnus, pas inventés.

## Validation déterministe facultative

`tools/scaffold_private.py` sait préparer ces mêmes fichiers hors ligne, dans un
répertoire local nouveau. Il ne crée ni dépôt GitHub, ni tâche, ni accès à un compte.
Le parcours Chat n'impose ni terminal ni Python ; il peut utiliser les appels GitHub
pour appliquer exactement le manifeste. Les tests sont sous `tests/test_scaffold_private.py`.
Une génération locale réussie ne vaut pas test de création d'un dépôt distant.
