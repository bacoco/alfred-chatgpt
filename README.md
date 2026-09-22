# ALFRED — Personal secretary in ChatGPT Chat

**Un secrétaire personnel qui connaît ton contexte, suit tes affaires et vérifie les résultats.**
Nom de travail : ALFRED, en référence au majordome de Batman.

> Un second cerveau retrouve ce que tu sais. Un secrétaire sait aussi ce qui reste
> à faire, qui attend quoi, quand intervenir et si une action a réellement abouti.

## Installer son ALFRED : un paragraphe dans Chat

Ouvrir un nouveau ChatGPT **Chat**, sélectionner les connecteurs souhaités, puis
copier ce seul paragraphe. Chat prend en charge la structure et les fichiers ;
l'utilisateur choisit son secrétaire par la conversation.

```text
Dans ce Chat uniquement, installe mon secrétaire ALFRED à partir de https://github.com/bacoco/alfred-chatgpt : lis instructions/INSTALLATION.md, génère mon propre dépôt GitHub privé à partir de templates/private/manifest.json, puis guide-moi pour choisir missions, sources, préférences et cadence, teste un cycle réel et crée le scheduler natif convenu. Conserve mes réglages et résultats dans mon dépôt privé, modifiables ensuite par conversation ; reprends une instance existante sans l’écraser. Si le connecteur est refusé par cette conversation, propose une nouvelle branche Chat avec le même connecteur, sans changer ses permissions, puis vérifie l’accès par une lecture, sans garantir le rétablissement.
```

Le parcours est : **kit public → dialogue → dépôt privé généré → test réel → scheduler**.
L'entrée précise est [INSTALLATION.md](instructions/INSTALLATION.md) ; elle utilise
les **seize fichiers prêts à copier** de [templates/private/](templates/private/README.md),
pas une description de structure à réinventer. Aucun JSON à écrire manuellement.
Les choix peuvent ensuite être corrigés dans Chat ; ils restent dans le privé.

**Prérequis vérifiés pendant l'installation :** lire le kit, écrire dans le dépôt
privé et utiliser les tâches natives. Créer automatiquement le dépôt exige en plus
une action de création de dépôts sur le connecteur choisi. Si elle manque, le guide
isole cette étape au lieu de prétendre l'avoir effectuée ; les fichiers sont déjà prêts.
La phrase ne fournit ni droits ni connecteurs. Pas de bascule vers un autre mode.

Une instance déjà configurée est **reprise**, pas réinstallée : retrouver sa tâche
native et ses registres, sans doublon ni remise à zéro. Aucun fork public nécessaire.
Le dépôt personnel de l'auteur n'est jamais la destination implicite d'un autre utilisateur.

## Ce qui est généré dans le dépôt privé

```text
README.md                       # instructions de reprise et personnalisation
AGENTS.md                       # règles locales et confidentialité
.gitignore
memory/profile.json             # préférences confirmées, initialement vides
state/control.json              # compte exact et mandat à configurer
state/tasks.json                # tâches et scheduler personnels
state/setup.json                # étapes d'installation et preuves
state/cases.json                 # affaires, vide au départ
state/decisions.json             # décisions du propriétaire
state/subscriptions.json         # abonnements, vide au départ
state/checkpoints.json           # couverture et reprises
state/runtime.json               # réservation de cycle
state/delivery.json              # sortie Chat et notifications
briefings/README.md              # emplacement des résultats
records/README.md                # emplacement des reçus
tests/fixtures/storage-probe.json # test fictif sans données réelles
```

Les réglages inconnus restent à compléter par dialogue ; aucun compte, horaire,
secret, mandat ni résultat de l'auteur n'est copié. Le contrôle initial est inactif,
puis l'installateur enregistre le périmètre accepté et active la lecture avant le
premier cycle utile. Le scheduler est raccordé après vérification, séparément.
Le [manifeste](templates/private/manifest.json) fixe les fichiers et leurs empreintes.

## Deux dépôts, deux rôles

| Kit public | Instance privée de chaque utilisateur |
| --- | --- |
| Mission et règles génériques | Préférences, comptes et mandats personnels |
| Catalogue de modèles de tâches | state/tasks.json : ses tâches actives |
| Contrat CYCLE.md et STATE.md | Affaires, décisions, checkpoints et reçus |
| Modèle initial sans données réelles | Analyses et briefings issus de ses sources |

Le `enabled:false` du catalogue public est un **défaut de modèle**, pas un arrêt
des installations existantes. L'activation vient de l'instance privée autorisée.
Les droits et limites des connecteurs restent obligatoires.

## Le modifier simplement en parlant

« Ce dossier est réglé », « Abandonne cette affaire », « Rappelle-moi lundi »,
« Raccourcis le briefing », « Change l'horaire du matin » : ALFRED retrouve le
contexte, enregistre la décision privée, applique le changement permis et le relit.
Une ambiguïté ne ferme pas une affaire. Une préférence ne donne aucun nouveau droit.
Les résolutions et abandons arrêtent les rappels ; les reports suivent la date convenue.
Un ancien message ne recrée pas une affaire fermée. Voir [STATE.md](instructions/STATE.md).

## Reprise et livraison

Le cycle reprend une fenêtre inachevée depuis son checkpoint vérifié. Il ne suppose
pas que la veille a réussi et ne rejoue pas les effets incertains. Un plafond atteint
garde les éléments restants. Extraits et lectures intégrales restent distingués.
**Sauvegarde, sortie Chat, notification configurée et réception sont quatre preuves.**
Les notifications se règlent dans ChatGPT Settings > Notifications (Push et/ou Email) ;
elles n'autorisent pas un envoi Gmail. [Source officielle](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt).

## Si un connecteur est refusé dans la conversation

Pour `This conversation does not support developer MCPs`,
`This conversation is restricted to developer MCPs`, ou des outils absents après
vérification de leur sélection : essayer **⋯ → Branch in new chat**, garder
**le même connecteur et le même compte**, puis une lecture minimale vérifiable.
C'est une branche **ChatGPT, pas Git**. Cette piste a été suivie d'un rétablissement
lors d'un test, mais **ce n'est pas une réparation garantie ni une causalité prouvée**.
Ne changer aucune permission. Un quota ou défaut de droits n'est pas un refus de contexte.
En tâche planifiée : rapporter l'erreur sans tâche de remplacement ni faux nouveau Chat.
[Procédure détaillée](docs/MCP_CONVERSATION_RECOVERY.md).

## Périmètre et confidentialité

Correspondance, affaires, échéances, abonnements, agenda, contacts et documents :
chaque source et action doit être autorisée. Observe n'active pas les mutations Gmail.
Chat raisonne et appelle ses connecteurs ; GitHub conserve le kit et, séparément, l'état.
Un fichier n'est ni un serveur ni une preuve d'exécution sur toutes les surfaces.
Aucun Work, Codex, Agent mode, GitHub Actions ou API de modèle externe implicite.

Aucun email réel, profil, facture, contrat, mandat personnel ni journal privé dans
ce dépôt public, ses issues ou ses fixtures. Aucun secret, token, clé privée,
lien à usage unique ou export brut très sensible dans aucun dépôt.
Le stockage Git privé conserve son historique ; ce n'est pas un coffre de secrets.

## Documentation

- [Installation guidée](instructions/INSTALLATION.md) et [modèle privé](templates/private/README.md)
- [Lancement / reprise](instructions/LANCEMENT.md) et [raccordement du scheduler](instructions/SCHEDULER.md)
- [Personnalisation](instructions/README.md), [cycle](instructions/CYCLE.md) et [état](instructions/STATE.md)
- [Mise en service et recette](docs/MISE-EN-SERVICE.md)
- [Analyse fondatrice](docs/ANALYSE-2026-09-20.md), [sources](docs/SOURCES.md), [feuille de route](docs/ROADMAP.md)

Projet indépendant ; aucune affiliation à DC ou OpenAI n'est revendiquée.
