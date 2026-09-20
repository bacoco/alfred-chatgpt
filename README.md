# ALFRED — Personal secretary in ChatGPT Chat

**Un secrétaire personnel qui connaît ton contexte, suit tes affaires et vérifie que les actions aboutissent.**

Nom de travail : **ALFRED**, en référence au majordome de Batman. Dépôt : [`bacoco/alfred-chatgpt`](https://github.com/bacoco/alfred-chatgpt).

> Un second cerveau retrouve ce que tu sais. Un vrai secrétaire sait aussi ce qui reste à faire, qui attend quoi, quand intervenir et si l'action a réellement abouti.

## Statut

**Dossier de conception et kit d'instructions, pas une application déployée.**
L'analyse du 20 septembre 2026 est conservée ici. Le dossier `instructions/` permet
de préparer et versionner les consignes, préférences et tâches du futur secrétaire.
Ses trois tâches sont désactivées. Aucun scheduler ni accès à un compte personnel
n'a été activé pour constituer ce dossier.

Le dossier est publié sur `main`. Le [compte rendu d'export initial](records/EXPORT-2026-09-20.md)
conserve l'historique du blocage antérieur ; il ne décrit pas l'état courant de la
publication. Publier cette documentation ne déploie aucun agent.

## Piloter et rendre fonctionnel

**[Modifier les instructions et les tâches](instructions/README.md)** : mission,
préférences, autonomie, catalogue des tâches, fiches briefing/relances/abonnements
et modèle pour ajouter une tâche ponctuelle ou récurrente.

**[Étapes de mise en service](docs/MISE-EN-SERVICE.md)** : capacités réelles,
stockage privé, cycle interactif, premier périmètre autorisé, test planifié,
puis actions déléguées. Le [contrat de cycle](instructions/CYCLE.md) impose au futur
pilote de relire les consignes GitHub à chaque réveil ; ce pilote reste à raccorder.

## Lire l'étude

**[Analyse complète — 20 septembre 2026](docs/ANALYSE-2026-09-20.md)** : vision,
existant à réutiliser, comparaison des projets, papers et benchmarks, architecture,
scénarios métier, autonomie, confidentialité, coût et ordre de réalisation.

Les [sources](docs/SOURCES.md) remplacent les citations propres à l'interface ChatGPT
par des références transportables. Les caractéristiques temporelles et les chiffres
de l'analyse initiale ne sont pas certifiés par cet export ; leur statut est indiqué.

## Ce que vise ALFRED

| Domaine | Résultat recherché |
| --- | --- |
| Correspondance | Repérer les réponses attendues, préparer les relances, agir sous mandat et suivre les affaires jusqu'à leur résolution. |
| Abonnements | Tenir un inventaire vérifiable, anticiper les échéances et comparer selon les besoins réels. |
| Agenda et contacts | Préparer les rendez-vous et rapprocher personnes, échanges et engagements. |
| Documents et projets | Relier preuves, décisions et affaires ouvertes, au-delà de Gmail. |
| Mémoire personnelle | Conserver des connaissances et préférences datées, sourcées, corrigibles et portables. |

## Architecture cible

ChatGPT Chat comprend et raisonne. Un état durable privé conserve connaissance,
affaires et journal. Les connecteurs autorisés réalisent les opérations. Le code
déterministe contrôle les mandats, dates, doublons et preuves de résultat.
Le wiki, le registre des affaires et le journal sont distincts. Une préférence n'est
pas une permission. Un message envoyé n'est pas nécessairement une affaire résolue.

## Existant d'abord

Réutiliser ou étendre [Chat-first Operations](https://github.com/bacoco/chatgpt-cost-router)
et les primitives de [loriq-watch-scheduler](https://github.com/bacoco/loriq-watch-scheduler).
Étudier Basic Memory, Inbox Zero et Wallos sans imposer leur adoption ni dupliquer
leurs runtimes. Aucun changement de voie d'exécution n'est implicite.

La cible reste **ChatGPT Chat + réveils périodiques**, sans bascule vers Work,
Codex, un autre modèle ou une API payante. Vérifier les capacités dans chaque
surface, particulièrement en exécution planifiée. Pas d'exécution via GitHub Actions.

## Confidentialité

Ce dépôt est **public** : il conserve la conception et des consignes génériques,
pas la vie privée de l'utilisateur. Emails, contrats, factures, secrets, profils,
paramètres des tâches personnelles, mandats et journaux réels restent hors Git.
Les exemples sont synthétiques. La visibilité du dépôt n'a pas été modifiée.

## Construire ensuite

Voir la [feuille de route](docs/ROADMAP.md), les [règles pour les agents](AGENTS.md)
et le [mode de publication](docs/PUBLICATION.md). Ces documents cadrent la suite
sans autoriser à eux seuls une exécution, une connexion ou un changement de droits.

Projet indépendant ; aucune affiliation à DC ou OpenAI n'est revendiquée.
