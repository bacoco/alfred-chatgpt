# ALFRED généraliste : positionnement et faisabilité

Revue documentaire du 22 septembre 2026, avant modification du README.
Sources primaires uniquement ; ce document n'est ni un benchmark ni une installation
des projets cités. Leurs fonctions annoncées ne sont pas des fonctions livrées par ALFRED.

## Ce que font d'autres projets

| Projet et source primaire | Approche documentée | Ce que l'on retient pour ALFRED |
| --- | --- | --- |
| [Khoj — présentation](https://docs.khoj.dev/) et [fonctions](https://docs.khoj.dev/category/features/) | Assistant personnel, recherche dans des notes/documents et sur le web, rôles personnalisés et automatisations. | Partir des besoins et du contexte, sans réduire l'assistant à une application ; rendre visibles les usages de recherche et de connaissance. |
| [OpenClaw — présentation](https://docs.openclaw.ai/) et [configuration personnelle](https://docs.openclaw.ai/start/openclaw) | Assistant via une passerelle auto-hébergée, plusieurs canaux, outils, compétences et espace de travail initialisé avec des fichiers de contexte. | Une installation guidée et une structure de mémoire concrète ; des capacités explicitement raccordées, pas déduites d'une promesse. |
| [Letta — documentation](https://docs.letta.com/) | Agents à état persistant, usages personnels ou professionnels, mémoire, compétences et tâches récurrentes. | La continuité du contexte et la personnalisation constituent le socle ; les rôles sont des configurations, pas la définition du produit. |

La convergence ci-dessus est une interprétation de conception à partir de ces
sources, pas une affirmation d'équivalence entre produits. ALFRED ne reprend ni
leurs serveurs, ni leurs moteurs de mémoire, ni leurs canaux, ni leur exécution locale.
Aucune dépendance à ces projets n'est ajoutée.

## Ce que permet le kit examiné

Base examinée : `82a707bd5811b0a71a34b1a9d8513a9e12c004b6`.

[MISSION.md](../instructions/MISSION.md), [STATE.md](../instructions/STATE.md) et
[le modèle privé](../templates/private/manifest.json) séparent déjà contexte,
préférences, affaires, décisions, autorisations et preuves.
[CYCLE.md](../instructions/CYCLE.md) charge les tâches privées et les fiches
du catalogue ; [SCHEDULER.md](../instructions/SCHEDULER.md) construit un réveil
natif distinct de l'installation. Ce sont des instructions appliquées par Chat,
pas un service autonome garantissant chaque transition.

| Besoin | Faisabilité dans la voie Chat retenue |
| --- | --- |
| Définir un rôle, des objectifs et des préférences | Dialogue puis enregistrement privé selon autorisation ; aucune nécessité conceptuelle de connecter une messagerie. |
| Organiser et suivre une affaire | Réutilisation des registres d'affaires et de décisions ; la source et le prochain résultat attendu doivent être identifiés. |
| Analyser des notes, dossiers, projets ou sources publiques | Possible en Chat lorsque les contenus et outils sont accessibles ; leur persistance et leur relecture ultérieure se vérifient séparément. |
| Préparer une réunion ou une synthèse de recherche récurrente | Configurer une fiche compatible ou compléter le catalogue, autoriser les sources, puis tester dans la surface planifiée avant d'annoncer le service actif. |
| Exécuter une action dans un service | Exige l'action exacte du connecteur, le mandat, les approbations éventuelles et la relecture de l'effet. Aucun accès universel. |
| Installer sa mémoire privée | Seize fichiers génériques fournis ; création du dépôt et écriture de fichiers sont des capacités distinctes. |

Le catalogue actuel contient **briefing, relances et abonnements**.
Il ne constitue pas encore une bibliothèque universelle de missions prêtes à activer.
Une nouvelle famille de tâches exige une fiche versionnée, un identifiant au
catalogue, une instance privée, les sources et une recette. Ne pas simuler
l'exécution d'un `template_id` absent ni modifier le kit commun avec des données privées.
Le README présente donc des exemples configurables sans les annoncer tous installés.

Les fenêtres et identifiants de messagerie dans STATE.md ne s'appliquent pas
automatiquement à une autre source : une extension doit définir ses propres
critères de couverture, de changement et de reprise, sans perdre les contrôles.

## Vérification des capacités ChatGPT

[Applications connectées](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt),
consulté le 22 septembre 2026 : lecture et actions dépendent de l'app, du compte,
des permissions et de la surface. Les autorisations ne créent pas d'actions absentes.
Conséquence : choisir les outils après la mission, puis tester les capacités exactes.

[GitHub dans ChatGPT](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt),
consulté le même jour : l'app GitHub standard est décrite en lecture seule.
Le connecteur de cette édition expose lecture et écriture de fichiers, mais
aucune action de création de dépôt n'a été trouvée dans ses schémas exposés.
Ce constat de schéma n'est pas un test de création ni une propriété de tous les comptes.
Ne pas promettre une installation complète à toute personne ayant simplement connecté GitHub.

[Tâches natives](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt),
consulté le même jour : les tâches peuvent être ponctuelles ou récurrentes ;
leur disponibilité dépend du compte. Elles n'accèdent pas automatiquement aux
fichiers téléversés dans le projet. Les déclenchements événementiels documentés
via Work sont hors du périmètre Chat uniquement retenu ici.
Une sortie Chat, une notification configurée et sa réception sont des preuves distinctes.

## Conséquences éditoriales

Le README commence par l'intérêt d'un secrétaire généraliste, puis l'installation.
Les usages professionnels, personnels, documentaires et de recherche précèdent
l'exemple de correspondance. Gmail n'est ni un prérequis ni la mission par défaut.
La consigne de configuration commence par l'objectif et les critères de réussite,
puis choisit les sources et une tâche réellement raccordable.

Le socle générique, les modèles actuellement fournis et les extensions à réaliser
sont distingués. Les fichiers détaillés portent la technique ; le lecteur n'a pas
à recevoir un mode d'emploi séparé par mail pour démarrer.

## Portée de cette modification

Documentation et cadrage de la configuration seulement : aucune nouvelle intégration,
aucune migration privée, aucun élargissement d'autorisation, aucun changement de tâche native.
Les essais antérieurs ne sont pas réétiquetés comme preuve de toutes les missions.
Une installation chez un nouvel utilisateur et chaque nouvelle mission restent
à vérifier avec ses propres outils, données autorisées et critères de résultat.
