# Contrat d'un cycle — à raccorder au runtime

**Ce fichier décrit le pilote attendu ; aucun exécuteur n'est livré avec ce dossier.**
Ne pas lancer un cycle réel, activer des tâches ou lire une messagerie sur la seule
base de ces instructions. Il faut une demande et un périmètre autorisés.

## Entrée canonique

Dépôt : `bacoco/alfred-chatgpt`. Branche proposée : `main`.
À chaque réveil autorisé, résoudre la branche en SHA et lire toutes les consignes
et fiches de ce cycle à ce même SHA. Garder cette révision dans le reçu privé.
Ne pas utiliser une copie ancienne conservée uniquement dans la conversation.

Charger [MISSION.md](MISSION.md), [PREFERENCES.md](PREFERENCES.md),
[AUTONOMIE.md](AUTONOMIE.md) et [tasks/registry.json](tasks/registry.json),
puis seulement les fiches sélectionnées sous `instructions/tasks/`.
Rejeter chemin sortant du répertoire, URL arbitraire, doublon d'identifiant,
mode inconnu ou fiche manquante. Ne pas exécuter `TEMPLATE.md`.
La grande analyse historique n'a pas à être relue à chaque réveil.

## GitHub indisponible au démarrage

Appliquer la [procédure MCP](../docs/MCP_CONVERSATION_RECOVERY.md) si elle est déjà
connue du contexte de lancement. Distinguer outil absent, refus de conversation
et droits GitHub. Ne pas déclarer les consignes chargées si leur lecture échoue.
En Chat interactif, proposer une branche de conversation autorisée pour un refus
de contexte persistant, puis un retest de lecture, sans garantir la réparation.
En tâche planifiée, signaler le blocage dans le résultat accessible ; ne pas créer
une nouvelle tâche ou simuler une nouvelle conversation. Sauver un reçu seulement
si le stockage est disponible et autorisé. Aucun effet incertain n'est rejoué.

## Sélection et préparation

Vérifier les instructions reconnues du propriétaire, l'état d'activation privé,
le mandat et les capacités actuelles, séparément pour Chat et Scheduled Tasks.
Le catalogue JSON n'est ni un registre d'exécution ni un stockage de permissions.
Sélectionner les tâches demandées (`enabled: true`) ET autorisées ET dues selon
leur calendrier privé validé. Un compte ou un connecteur manquant bloque la tâche
concernée ; ne pas prétendre que ses sources ont été vérifiées.

Charger les derniers checkpoints, affaires et occurrences en cours. Réconcilier
les effets incertains avant de traiter de nouvelles actions sur la même affaire.
Réserver chaque occurrence dans l'état privé pour éviter les courses concurrentes.
Les champs de cadence en langage naturel ne doivent pas être réinterprétés à chaque
réveil : utiliser le calendrier déjà approuvé, avec sa version et son fuseau.

## Exécution bornée

Proposer un plan adapté au résultat attendu, puis traiter les nouveautés autorisées
et les affaires dues, dans le budget du cycle. Distinguer preuve et interprétation.
Les contrôles d'identité, de budget, de schéma et de permissions sont déterministes ;
la compréhension et la rédaction appartiennent à ChatGPT.

Avant chaque écriture, relire le contrôle d'arrêt et les autorisations actuelles.
Si la révision de politique a changé, arrêter les nouveaux effets et revalider.
Une simple modification de ton ne doit pas obliger à redemander tous les accès.
Un élargissement de périmètre ne doit jamais être adopté comme une correction banale.

Ne pas marquer une occurrence terminée avant vérification du résultat. Sauver les
checkpoints confirmés ; les pages ou éléments non traités restent à reprendre.
Au redémarrage, reprendre l'état sans renvoyer les actions déjà réalisées ou inconnues.
Ne pas convertir un blocage en boucle de tentatives ni en appel à un autre modèle.

## Sortie

Rendre un briefing utile : décisions, préparations, actions vérifiées, couverture,
inconnues et prochaine échéance connue. Le journal détaillé reste privé.
Un reçu comprend au minimum : identifiant de cycle, SHA des instructions,
version du mandat, tâches sélectionnées, états, sources traitées et checkpoints.
Un reçu ne contient pas de secret et ne doit pas être publié automatiquement.

## Prompt court pour un futur réveil

> Dans ChatGPT Chat, pour bacoco/alfred-chatgpt, lis instructions/CYCLE.md sur
> main et applique-le avec les seuls comptes, tâches et mandats privés déjà
> autorisés. Relis les instructions GitHub à chaque cycle. Si le stockage privé,
> les capacités ou l'autorisation manquent, rends le blocage sans effet externe.
> N'active rien, ne change aucun droit et ne bascule pas vers Work, Codex ou une API.
> Si GitHub refuse le contexte ou reste sans outil après sélection vérifiée,
> distingue ce cas des permissions GitHub. En Chat, propose une nouvelle branche
> de conversation autorisée et un test de lecture ; en tâche, signale le blocage.
> Ne garantis pas la reprise et ne répète aucune écriture au résultat incertain.

Ce prompt devra être intégré et testé dans une vraie tâche après autorisation.
Le coller dans un fichier GitHub ne crée pas de Scheduled Task.
