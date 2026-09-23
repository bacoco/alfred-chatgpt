# Diagnostic guidé du dépôt privé

Complément obligatoire des étapes 1 à 4 d'INSTALLATION.md, avant toute écriture.
Référence : [issue #4](https://github.com/bacoco/alfred-chatgpt/issues/4).
Ne pas changer de connecteur, de compte ou de permissions pour réussir l'installation.

## Ce que l'utilisateur doit comprendre

Présenter le parcours avant les opérations : vérifier les capacités, créer ou
reprendre son dépôt privé, choisir une ou deux missions, tester un cycle, puis
raccorder uniquement la planification convenue. Réutiliser les réponses déjà données.

Texte court à afficher dans le parcours d'installation :

> Selon le connecteur, vous devrez peut-être créer vous-même un dépôt privé et
> vérifier son accès dans l'installation GitHub App. ALFRED reprendra ensuite
> sans écraser vos fichiers. Aucune donnée personnelle ne sera écrite en public.

La création d'un dépôt, l'écriture de fichiers et l'initialisation d'un dépôt vide
sont trois capacités distinctes. Ni leur nom ni une lecture réussie ne les prouvent.

## Matrice de diagnostic

| Observation réellement vérifiée | État | Action suivante et responsable |
| --- | --- | --- |
| Refus de conversation | conversation_refused | Proposer au propriétaire une branche Chat, même connecteur et compte, puis une lecture minimale ; aucune garantie. |
| Refus de sécurité/permission | blocked | Arrêter ; ne pas chercher un autre canal. Signaler l'erreur et l'action autorisée nécessaire. |
| Mauvais propriétaire | wrong_owner | Clarifier la destination avant toute donnée. |
| Dépôt public | public_repository | Aucune écriture ALFRED. Demander au propriétaire de passer ce dépôt en Private, puis revérifier. |
| Absence démontrée | repository_absent | Créer le dépôt privé convenu seulement si l'action est disponible et autorisée ; sinon demander sa création manuelle avec README. |
| Dépôt privé existant, exclusion de l'App confirmée | private_not_selected | Le propriétaire vérifie Repository access dans l'installation de la même GitHub App. ALFRED ne change pas les droits. |
| 404, refus ou résultat inconnu sans cause établie | access_unknown | Rapporter exactement ce qui manque ; ne pas conclure « dépôt absent » ou « permission à élargir ». |
| Privé accessible, écriture indisponible | write_unavailable | Expliquer la capacité manquante ; pas de faux succès. |
| Privé accessible et vide | empty_private_repository | Initialiser ce même dépôt si l'outil sait réellement le faire ; sinon demander un README initial. |
| Fichiers partiellement présents | partial_scaffold | Appliquer WRITE_RECOVERY.md, conserver les fichiers, reprendre uniquement les manques. |
| Tous présents mais non relus | readback_required | Relire et comparer chaque fichier requis. |
| Stockage entièrement vérifié | storage_verified | Reprendre l'instance et ses choix ; demander seulement le périmètre encore manquant. |

Un 404 ne distingue pas à lui seul inexistence et ressource inaccessible.
Ne jamais utiliser le nom d'une autre installation pour contourner cette ambiguïté.

## GitHub App et OAuth : explication ciblée

Lorsque l'exclusion est effectivement constatée, orienter le propriétaire vers
[Installed GitHub Apps](https://github.com/settings/installations), puis la
configuration de l'installation correspondant au connecteur déjà choisi.
Le réglage pertinent pour une GitHub App est Repository access, notamment
« Only select repositories ». La page OAuth Apps n'est pas ce réglage.

Ne pas demander « All repositories », remplacer l'App ou élargir les droits par
défaut. Le propriétaire ou administrateur choisit l'accès nécessaire conformément
à ses règles ; l'agent n'effectue aucun changement de permissions. Après correction
par la personne autorisée, vérifier une lecture du même dépôt via le même connecteur.
Une restriction explicite d'administrateur n'est pas un incident à contourner.

## Reprise sans répétition

Relire state/setup.json et le journal d'installation existants. Préserver nom,
installation_id, paramètres de rendu, choix, affaires et décisions. Ne recréer ni
dépôt ni scheduler. Private est une condition bloquante ; README est une commodité
récupérable lorsque le connecteur sait initialiser un dépôt vide. L'existence du
README ne prouve pas la vérification des seize fichiers.

Enregistrer les observations et leur date seulement dans le privé autorisé.
Si la destination n'est pas privée, garder le diagnostic dans Chat ; même un
journal d'installation peut révéler des réglages personnels.
Le diagnostic `storage_verified` n'active aucune source ni tâche : l'accord sur
le périmètre et le cycle réel restent nécessaires selon INSTALLATION.md.

## Contrôle local facultatif

[installation_diagnostics.py](../tools/installation_diagnostics.py) classe les
observations fournies sans contacter GitHub. Une valeur inconnue n'est pas False.
Les champs de capacité doivent provenir du schéma réel et des vérifications permises.
`change_permissions=false` et `activate_business=false` restent systématiques.

Recette : `python -m unittest discover -s tests -p test_installation_diagnostics.py -v`.
Les fixtures couvrent notamment Only select repositories, 404 ambigu, dépôt public,
dépôt vide, scaffold partiel et reprise avec décisions conservées. Ce sont des
contrôles de décision synthétiques, pas une validation des droits d'un compte réel.
