# ALFRED — Personal secretary in ChatGPT Chat

**Un secrétaire personnel qui connaît ton contexte, suit tes affaires et vérifie que les actions aboutissent.**

Nom de travail : **ALFRED**, en référence au majordome de Batman. Dépôt : [`bacoco/alfred-chatgpt`](https://github.com/bacoco/alfred-chatgpt).

> Un second cerveau retrouve ce que tu sais. Un vrai secrétaire sait aussi ce qui reste à faire, qui attend quoi, quand intervenir et si l'action a réellement abouti.

## Statut

**Dossier de conception, pas une application déployée.** L'analyse du 20 septembre 2026 est conservée ici. Aucun scheduler n'a été créé, aucun compte personnel n'a été parcouru et aucune action de secrétariat n'a été activée pour constituer ce dossier.

Le dossier est publié sur la branche `main` de ce dépôt. Le [compte rendu d'export initial](records/EXPORT-2026-09-20.md) conserve l'historique du blocage antérieur ; il ne décrit pas l'état courant de la publication. Publier cette documentation ne déploie aucun agent.

## Lire l'étude

**[Analyse complète — 20 septembre 2026](docs/ANALYSE-2026-09-20.md)** : vision, existant à réutiliser, comparaison des projets, papers et benchmarks, architecture, scénarios métier, autonomie, confidentialité, coût et ordre de réalisation.

Les [sources](docs/SOURCES.md) remplacent les citations propres à l'interface ChatGPT par des références transportables. Les caractéristiques temporelles et les chiffres de l'analyse initiale ne sont pas certifiés par cet export ; leur statut est explicitement indiqué.

## Ce que vise ALFRED

| Domaine | Résultat recherché |
| --- | --- |
| Correspondance | Repérer les réponses attendues, préparer les relances, agir sous mandat et suivre le dossier jusqu'à sa résolution. |
| Abonnements | Tenir un inventaire vérifiable, anticiper les échéances et comparer les alternatives selon les besoins réels. |
| Agenda et contacts | Préparer les rendez-vous et rapprocher personnes, échanges et engagements. |
| Documents et projets | Relier les preuves, les décisions et les affaires ouvertes, au-delà de Gmail. |
| Mémoire personnelle | Conserver des connaissances et préférences datées, sourcées, corrigibles et portables. |

## Architecture cible

ChatGPT Chat assure la compréhension et le raisonnement. Un état durable conserve la connaissance, les affaires ouvertes et le journal des actions. Les connecteurs autorisés réalisent les opérations. Le code déterministe contrôle les mandats, les échéances, les doublons et les preuves de résultat.

Le wiki de connaissance, le registre des affaires et le journal d'exécution sont distincts. Une préférence n'est pas une permission. Un message envoyé n'est pas nécessairement une affaire résolue.

## Existant d'abord

Réutiliser ou étendre [Chat-first Operations](https://github.com/bacoco/chatgpt-cost-router) et les primitives de [loriq-watch-scheduler](https://github.com/bacoco/loriq-watch-scheduler). Étudier Basic Memory pour la connaissance, Inbox Zero pour les échanges et Wallos pour les abonnements, sans imposer leur adoption ni dupliquer leurs runtimes.

La cible reste **ChatGPT Chat + réveils périodiques**, sans bascule implicite vers Work, Codex, un autre modèle ou une API payante. Les capacités réellement disponibles doivent être vérifiées dans chaque surface, particulièrement en exécution planifiée. GitHub Actions n'est pas une voie d'exécution retenue.

## Confidentialité

Ce dépôt conserve la conception, pas la vie privée de l'utilisateur. Les emails, contrats, factures, secrets, journaux d'action et profils réels restent hors de Git. Utiliser des exemples synthétiques. Le dépôt créé par le propriétaire est **public**. Sa visibilité n'a pas été modifiée lors de la publication. Il ne doit jamais accueillir la mémoire personnelle ni les données réelles du futur secrétaire.

## Construire ensuite

Voir la [feuille de route](docs/ROADMAP.md), les [règles pour les agents](AGENTS.md) et le [mode de publication](docs/PUBLICATION.md). Ces documents cadrent la suite sans autoriser à eux seuls une exécution, une connexion ou un changement de permissions.

Projet indépendant. Les noms cités servent à identifier les inspirations et les intégrations envisagées ; aucune affiliation à DC ou OpenAI n'est revendiquée.
