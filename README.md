# ALFRED — Votre secrétaire persistant dans ChatGPT

**Suivre les mêmes affaires dans le temps, conserver vos décisions et reprendre
le travail sans repartir de zéro, même lorsque les informations viennent de plusieurs sources.**

ALFRED sert les dossiers qui vivent plusieurs jours ou semaines : un projet,
un rendez-vous à préparer, une démarche, une réponse attendue ou un abonnement.
Les mails sont des signaux possibles, pas la définition du produit. Gmail est optionnel.
L'unité de suivi est **l'affaire**, avec ses preuves, son état et sa prochaine action.

Pour une question, une recherche ou un résumé ponctuel, utilisez directement Chat.
Une tâche native compatible peut suffire pour une répétition sans état métier durable.
**ALFRED ne remplace ni ChatGPT ni son scheduler ; il n'est pas un passage obligatoire.**

## Installer votre ALFRED

Le parcours : vérifier les capacités ; créer ou reprendre votre dépôt privé ;
choisir une ou deux missions ; tester un cycle réel ; puis tester la planification
seulement lorsqu'elle est demandée. Les réglages se font par conversation.

Selon les capacités du connecteur, une étape manuelle peut être nécessaire :
créer un dépôt **privé** et vérifier son accès dans l'installation GitHub App.
Un README facilite l'initialisation ; la visibilité privée, elle, est bloquante.
ALFRED vérifie et reprend sans écraser l'existant ni changer les permissions.
[Diagnostic guidé](instructions/INSTALLATION_DIAGNOSTICS.md).

Ouvrez un nouveau **chat ChatGPT**, puis copiez ce paragraphe :

```text
Dans ce Chat uniquement, installe mon secrétaire ALFRED à partir de https://github.com/bacoco/alfred-chatgpt : lis instructions/INSTALLATION.md, génère mon propre dépôt GitHub privé à partir de templates/private/manifest.json, puis guide-moi pour choisir missions, sources, préférences et cadence, teste un cycle réel et crée le scheduler natif convenu. Conserve mes réglages et résultats dans mon dépôt privé, modifiables ensuite par conversation ; reprends une instance existante sans l’écraser. Si le connecteur est refusé par cette conversation, propose une nouvelle branche Chat avec le même connecteur, sans changer ses permissions, puis vérifie l’accès par une lecture, sans garantir le rétablissement.
```

Vous n'avez ni code ni JSON à écrire. Le kit fournit les
[seize fichiers initiaux](templates/private/README.md).
Il faut un connecteur GitHub autorisé à lire et écrire dans votre dépôt privé ;
la création d'un dépôt, l'écriture de fichiers et la planification sont des
capacités distinctes, à vérifier réellement. Le prompt ne crée aucun droit.

Une instance existante est reprise avec ses choix, sans second dépôt, second
scheduler, fork public ou remise à zéro. [Installation détaillée](instructions/INSTALLATION.md).

## Ce qui reste d'un cycle au suivant

```text
signaux autorisés → même affaire → état et décisions → prochaine action
                         ↑                                  ↓
                   réconciliation ← nouveaux éléments et résultats
```

Exemple synthétique : plusieurs mails et deux événements représentent un même
rendez-vous. ALFRED rattache leurs références à une affaire, après vérification,
plutôt que de créer une alerte par source. Deux rendez-vous distincts ne sont pas
fusionnés parce que leurs titres se ressemblent.

« C'est résolu », « Abandonne », « Reprends lundi » ou « Sépare ces deux dossiers »
sont des décisions à conserver et vérifier, pas des phrases à oublier au réveil
suivant. Un ancien signal ne rouvre pas une affaire close. Une réponse tardive doit
être relue avant de proposer une relance. Un doute reste visible, sans action forcée.

## Un noyau limité, des responsabilités claires

| Élément | Rôle dans la voie retenue |
| --- | --- |
| ChatGPT Chat | Comprendre, analyser et utiliser les outils autorisés. |
| Scheduler natif | Réveiller une tâche convenue ; pas conserver l'état métier. |
| Connecteurs | Lire les sources ou réaliser les actions explicitement autorisées. |
| GitHub privé | Conserver affaires, décisions, checkpoints et reçus minimaux. |
| ALFRED | Appliquer le protocole de continuité, d'identité et de réconciliation. |

Le [contrat de positionnement](docs/POSITIONNEMENT.md) définit ce noyau et les
conditions d'une extension. Pas de serveur ALFRED, second ordonnanceur, moteur de
mémoire parallèle ou catalogue universel ajouté pour ce besoin.
Les outils Python sous `tools/` sont des aides locales de rendu ou de validation ;
ils ne connectent pas les comptes et ne remplacent pas le jugement sémantique de Chat.

## Livré et vérifié ne veulent pas dire activé partout

Le dépôt fournit des instructions, un modèle privé, des contrats et des tests.
Le [catalogue](instructions/tasks/registry.json) contient briefing, relances et
abonnements, inactifs par défaut. Une mission supplémentaire exige une fiche,
un mandat, des sources et une recette ; aucune intégration n'est garantie par son nom.

La [recette externe du 22 septembre](docs/RETEX-2026-09-22.md) rapporte 29 scénarios
réussis sur sa révision et son instance. Ce n'est pas une nouvelle exécution de ces
tests, une certification universelle ni la validation des modifications ultérieures.
Les tests synthétiques du dépôt ne prouvent pas l'accès Gmail, Calendar ou Scheduler.
Les refus d'écriture et retards de visibilité du scheduler gardent leurs limites connues.

Une création de tâche ne prouve pas son exécution. Un résultat sauvegardé, une sortie
Chat, une notification configurée et une réception confirmée sont quatre états distincts.
Un résultat incertain se réconcilie avant toute reprise ; il ne justifie pas un doublon.

## Confidentialité et autonomie

Le kit public conserve seulement des règles génériques et exemples synthétiques.
Les comptes, mandats, préférences, affaires et reçus réels restent dans votre dépôt privé.
Aucun mot de passe, token, clé privée, export brut sensible ou lien à usage unique dans Git.
Git privé conserve son historique ; ce n'est pas un coffre de secrets.

Le mode observe prépare, analyse et persiste selon mandat, sans mutation Gmail/Calendar.
Les envois, labels, archives, modifications d'agenda et autres actions demandent chacun
un outil disponible, une autorisation actuelle et une preuve de résultat.
Aucune notification native ne vaut autorisation d'envoyer un mail en votre nom.

La voie retenue reste Chat + connecteurs autorisés + dépôt privé + réveils natifs
convenus. Aucun basculement implicite vers Work, Codex, Agent mode, GitHub Actions
ou une API de modèle externe. Aucune correction du kit ne réinitialise une instance
privée, n'élargit ses droits ou ne modifie ses horaires.

## Connecteur refusé dans une conversation

Pour `This conversation does not support developer MCPs` ou
`This conversation is restricted to developer MCPs`, proposer une nouvelle branche
**ChatGPT** avec **le même connecteur et compte**, puis vérifier une lecture minimale.
Ne changer aucune permission. Cette piste n'est pas une réparation garantie.
Une branche Git n'est pas une branche de conversation. Une restriction d'administrateur,
un quota ou une authentification ne se contourne pas par cette procédure.
En tâche planifiée, signaler le blocage, sans créer de tâche de remplacement.
[Procédure détaillée](docs/MCP_CONVERSATION_RECOVERY.md).

## Documentation

- [Installation](instructions/INSTALLATION.md), [modèle privé](templates/private/README.md), [personnalisation](instructions/README.md)
- [Mission](instructions/MISSION.md), [cycle](instructions/CYCLE.md), [état](instructions/STATE.md), [identité des affaires](instructions/CASE_IDENTITY.md)
- [Reprise d'écriture](instructions/WRITE_RECOVERY.md), [scheduler](instructions/SCHEDULER.md), [observation des cycles](instructions/SCHEDULER_OBSERVABILITY.md)
- [Mise en service](docs/MISE-EN-SERVICE.md), [positionnement](docs/POSITIONNEMENT.md), [feuille de route](docs/ROADMAP.md)
- [Analyse fondatrice](docs/ANALYSE-2026-09-20.md), [sources historiques](docs/SOURCES.md), [retour de recette](docs/RETEX-2026-09-22.md)

Nom de travail inspiré du majordome de Batman. Projet indépendant, sans affiliation
revendiquée à DC, OpenAI ni aux projets cités dans les études historiques.
