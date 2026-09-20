# ALFRED — Personal secretary in ChatGPT Chat

**Un secrétaire personnel qui connaît ton contexte, suit tes affaires et vérifie que les actions aboutissent.**

Nom de travail : **ALFRED**, en référence au majordome de Batman. Dépôt : [`bacoco/alfred-chatgpt`](https://github.com/bacoco/alfred-chatgpt).

> Un second cerveau retrouve ce que tu sais. Un vrai secrétaire sait aussi ce qui reste à faire, qui attend quoi, quand intervenir et si l'action a réellement abouti.

## Installer ALFRED dans un nouveau Chat

Dans un nouveau ChatGPT Chat, connectez GitHub et les applications que vous voulez confier à ALFRED, puis copiez simplement cette phrase :

> **Installe ALFRED pour moi à partir de `bacoco/alfred-chatgpt`. Guide-moi pour définir ce que mon secrétaire doit faire, crée ou configure un dépôt GitHub privé séparé pour ma mémoire personnelle, teste les connecteurs réellement disponibles, puis mets en place avec mon accord un scheduler ChatGPT natif selon la cadence que je choisis. Reste en mode Chat uniquement et applique `instructions/LANCEMENT.md`.**

Cette phrase est volontairement courte : le Chat doit ensuite lire le dépôt public et utiliser ses instructions comme kit de construction.

ALFRED doit alors :
1. lire le dépôt public et charger `instructions/LANCEMENT.md`, `instructions/CYCLE.md`, la mission, les préférences, l'autonomie et le catalogue des tâches ;
2. discuter avec l'utilisateur pour définir **son** secrétaire : missions, ton, priorités, sources, horaires, niveau d'autonomie et actions interdites ;
3. créer ou configurer, avec accord de l'utilisateur, **un dépôt GitHub privé distinct** pour la mémoire et les résultats personnels ;
4. tester réellement les connecteurs choisis avant de considérer une capacité comme disponible ;
5. réaliser d'abord un petit cycle interactif vérifiable ;
6. créer ensuite, avec accord de l'utilisateur, une **Scheduled Task ChatGPT native** à l'horaire et à la cadence choisis ;
7. conserver les résultats privés, dossiers, checkpoints et préférences dans le dépôt privé et laisser ce dépôt public générique ;
8. permettre ensuite à l'utilisateur de retuner ALFRED simplement en discutant avec lui : modifier mission, priorités, cadence, sources, autonomie, tâches et préférences, puis enregistrer les changements au bon endroit.

Le dépôt privé n'a pas besoin de porter un nom imposé. Le Chat doit demander ou proposer un nom et vérifier qu'il est bien privé avant toute donnée personnelle.

## Si le connecteur ne fonctionne pas dans le Chat

Si le connecteur demandé est bien sélectionné mais que cette conversation renvoie par exemple :

- `This conversation does not support developer MCPs`
- `This conversation is restricted to developer MCPs`
- ou que les outils du même connecteur restent absents,

alors, en **Chat interactif**, utiliser **⋯ → Branch in new chat**, conserver **le même connecteur et le même compte**, puis refaire **une seule lecture minimale vérifiable**. À défaut, ouvrir un nouveau Chat autorisé et refaire ce test.

Il s'agit d'une **branche de conversation ChatGPT, pas d'une branche Git**. Cette méthode a été suivie d'un rétablissement de lecture lors d'un test ALFRED, mais **elle n'est pas une réparation garantie et sa causalité n'est pas démontrée**. Ne changez ni de connecteur ni de permissions pour contourner un refus.

En tâche planifiée, ALFRED ne peut pas créer lui-même une nouvelle conversation : il doit simplement rapporter le blocage. Voir [`docs/MCP_CONVERSATION_RECOVERY.md`](docs/MCP_CONVERSATION_RECOVERY.md).

## Personnaliser ALFRED

Le Chat de configuration doit utiliser ces fichiers comme source de vérité :

- [`instructions/MISSION.md`](instructions/MISSION.md) — ce qu'ALFRED doit accomplir ;
- [`instructions/PREFERENCES.md`](instructions/PREFERENCES.md) — ton, ordre des priorités, forme du briefing ;
- [`instructions/AUTONOMIE.md`](instructions/AUTONOMIE.md) — ce qu'il peut lire, préparer ou exécuter ;
- [`instructions/tasks/registry.json`](instructions/tasks/registry.json) — tâches disponibles et activation ;
- [`instructions/CYCLE.md`](instructions/CYCLE.md) — déroulement d'un réveil ;
- [`instructions/LANCEMENT.md`](instructions/LANCEMENT.md) — contexte autonome à charger au démarrage.

Les données personnelles, comptes, mandats, dossiers réels, échéances et résultats restent dans le dépôt privé de l'utilisateur.

## Ce que vise ALFRED

| Domaine | Résultat recherché |
| --- | --- |
| Correspondance | Repérer les réponses attendues, préparer les relances, agir sous mandat et suivre les affaires jusqu'à leur résolution. |
| Abonnements | Tenir un inventaire vérifiable, anticiper les échéances et comparer selon les besoins réels. |
| Agenda et contacts | Préparer les rendez-vous et rapprocher personnes, échanges et engagements. |
| Documents et projets | Relier preuves, décisions et affaires ouvertes, au-delà de Gmail. |
| Mémoire personnelle | Conserver des connaissances et préférences datées, sourcées, corrigibles et portables. |

## Architecture

ChatGPT Chat comprend et raisonne. Un état durable privé conserve connaissance, affaires et journal. Les connecteurs autorisés réalisent les opérations. Le code déterministe contrôle les mandats, dates, doublons et preuves de résultat.

La cible reste **ChatGPT Chat + réveils périodiques**, sans bascule implicite vers Work, Codex, GitHub Actions ou une API de modèle externe.

## Confidentialité

Ce dépôt est **public** : il conserve la conception et des consignes génériques, jamais la vie privée de l'utilisateur. Emails, contrats, factures, secrets, profils, paramètres personnels, mandats et journaux réels restent dans le dépôt privé.

Ne jamais stocker de mot de passe, token, clé privée ou export brut inutilement sensible dans Git.

## Documentation

- [Mise en service détaillée](docs/MISE-EN-SERVICE.md)
- [Contrat de cycle](instructions/CYCLE.md)
- [Prompt de lancement autonome](instructions/LANCEMENT.md)
- [Reprise d'un connecteur refusé](docs/MCP_CONVERSATION_RECOVERY.md)
- [Analyse fondatrice](docs/ANALYSE-2026-09-20.md)
- [Sources](docs/SOURCES.md)
- [Feuille de route](docs/ROADMAP.md)

Projet indépendant ; aucune affiliation à DC ou OpenAI n'est revendiquée.
