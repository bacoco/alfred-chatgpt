# ALFRED — Votre secrétaire personnel généraliste dans ChatGPT

**Un secrétaire qui s'adapte à vos objectifs, conserve le contexte que vous lui
confiez et suit ce qui reste à faire — dans votre vie professionnelle ou personnelle.**

Vous définissez son rôle : suivre un projet, préparer un dossier, organiser vos
priorités, vous aider à rechercher et décider, ou accompagner une démarche.
ALFRED relie les informations autorisées, prépare le travail, conserve vos décisions
et vérifie les résultats des actions que vous lui déléguez.
**La gestion des mails est un cas d'usage, pas la définition d'ALFRED.**

## Installer votre ALFRED

Ouvrez un nouveau **chat ChatGPT**, puis copiez ce paragraphe. La configuration
se fait ensuite par discussion : vous décrivez vos besoins, Chat prépare les
fichiers de votre instance et vérifie les accès nécessaires.

```text
Dans ce Chat uniquement, installe mon secrétaire ALFRED à partir de https://github.com/bacoco/alfred-chatgpt : lis instructions/INSTALLATION.md, génère mon propre dépôt GitHub privé à partir de templates/private/manifest.json, puis guide-moi pour choisir missions, sources, préférences et cadence, teste un cycle réel et crée le scheduler natif convenu. Conserve mes réglages et résultats dans mon dépôt privé, modifiables ensuite par conversation ; reprends une instance existante sans l’écraser. Si le connecteur est refusé par cette conversation, propose une nouvelle branche Chat avec le même connecteur, sans changer ses permissions, puis vérifie l’accès par une lecture, sans garantir le rétablissement.
```

**Vous n'avez ni code ni fichiers JSON à écrire.** Le kit fournit les
[16 fichiers initiaux du dépôt privé](templates/private/README.md).
Chat vous aide à choisir missions, informations confiées, sources, niveau d'autonomie,
forme des résultats et éventuelle cadence. **Gmail n'est pas obligatoire** :
ne connectez que les services utiles aux missions retenues.

Pour l'instance persistante, il faut un accès GitHub capable de lire **et d'écrire**
dans votre dépôt privé. Sa création automatique exige aussi une action de création
de dépôt ; sinon le guide vous accompagne sur cette seule étape manquante.
La planification exige des tâches natives accessibles sur votre compte.
L'installation teste ces capacités et signale ce qui manque ; le paragraphe
ne crée pas des permissions. [Parcours détaillé](instructions/INSTALLATION.md).

Une instance existante est reprise, sans second dépôt, second scheduler ni remise
à zéro. Aucun fork public n'est nécessaire pour vos réglages personnels.

## Un même secrétaire, des missions différentes

Ces exemples servent à définir **votre** ALFRED. Leur réalisation dépend des sources
accessibles, des outils autorisés et, pour un suivi automatique, d'une tâche
raccordée et testée ; ils ne sont pas des intégrations toutes livrées d'avance.

| Votre besoin | Le résultat que vous pouvez lui demander de préparer ou suivre |
| --- | --- |
| Projets et objectifs | Un état d'avancement, les décisions prises, les blocages et les prochaines actions. |
| Réunions et dossiers | Une synthèse des documents disponibles, les points à discuter et les engagements à suivre. |
| Recherche et veille | Une synthèse sourcée, une comparaison d'options et les changements pertinents pour une décision. |
| Organisation personnelle | Le suivi d'une démarche, d'un événement à préparer ou d'échéances que vous lui confiez. |
| Connaissances et apprentissage | Des notes structurées, des explications adaptées et un suivi des questions à approfondir. |
| Correspondance, si vous la choisissez | Les réponses attendues, les informations utiles et les actions à préparer. |

Le rôle n'est pas figé. Un même ALFRED peut combiner plusieurs missions compatibles
avec ses accès, ou se concentrer sur un seul objectif. Les connecteurs sont des
moyens d'accès ; ils ne définissent pas le métier du secrétaire.

## Ce qu'ALFRED ajoute à une conversation ponctuelle

Son intérêt est la **continuité** : des préférences enregistrées, des dossiers suivis,
des décisions conservées et un travail qui reprend au lieu de repartir de zéro.
La mémoire durable est explicite, dans votre dépôt privé : elle ne repose pas sur
la supposition que ChatGPT se souviendra automatiquement de toutes les conversations.

Vous pouvez corriger son fonctionnement en lui parlant : « Ce projet est terminé »,
« Reprends ce dossier lundi », « Voici ma nouvelle priorité », « Fais une synthèse
plus courte ». ALFRED enregistre la décision autorisée, applique le changement et
relit ce qui a été sauvegardé. Résolution ou abandon arrête les rappels ; un report
conserve la date convenue. [Personnalisation](instructions/README.md).

Un résultat peut être demandé dans Chat ou lors d'un réveil natif convenu.
La tâche planifiée relit les instructions et l'état privé ; elle ne réinstalle
pas ALFRED. Une modification d'horaire doit aussi être appliquée à la tâche native.

## Ce qui existe, et ce qui demande une extension

Le dépôt fournit le **kit de configuration**, le modèle de mémoire privée et les
contrats de suivi, décision, reprise et vérification. Il n'est pas un serveur
autonome : Chat exécute les instructions avec les outils réellement disponibles.

Le [catalogue actuel](instructions/tasks/registry.json) contient trois modèles :
**briefing**, **préparation de relances** et **revue d'abonnements**.
Ce sont des points de départ, pas les frontières du projet.
Une nouvelle famille de tâches doit avoir une [fiche](instructions/tasks/TEMPLATE.md),
être référencée au catalogue, associée à une instance privée autorisée, puis testée.
Décrire un besoin ne suffit pas à livrer un connecteur ou une automatisation manquante.

La configuration peut privilégier un premier résultat utile en lecture et préparation.
Les envois, publications, modifications d'agenda ou autres actions sur un service
exigent chacun un outil disponible, un mandat explicite et une vérification.
Une réussite sur une source ne valide ni toutes les autres sources ni le prochain
réveil automatique. [Faisabilité et comparaison des approches](docs/POSITIONNEMENT.md).

## Deux dépôts, deux rôles

| Kit public partagé | Votre instance privée |
| --- | --- |
| Mission, instructions et modèles génériques | Vos objectifs, préférences, comptes et autorisations |
| Modèle initial sans données personnelles | Vos affaires, décisions, notes minimales et résultats |
| Contrats de cycle et de vérification | Vos tâches, points de reprise et reçus |

La structure privée est générée depuis le [manifeste](templates/private/manifest.json) :
`memory/` pour les préférences, `state/` pour la configuration et le suivi,
`briefings/` pour les restitutions, `records/` pour les preuves.
Les exemples sous `tests/fixtures/` restent fictifs.
Aucune donnée de l'auteur ni d'une autre installation n'est copiée.

## Limites pratiques et confidentialité

La voie prévue est **ChatGPT Chat + connecteurs autorisés + dépôt GitHub privé
+ tâches natives lorsque disponibles**. Pas de serveur ALFRED à héberger, ni
d'API de modèle externe à configurer pour cette voie. Ce n'est pas un assistant
local hors ligne. Aucun basculement implicite vers Work, Codex, Agent mode,
GitHub Actions ou un autre moteur d'agents.

Les accès dépendent du compte, du connecteur et de la surface utilisée.
L'app GitHub standard est documentée en lecture seule ; elle ne suffit donc pas
à promettre l'installation avec écriture à tout le monde. Vérifier les actions
du connecteur choisi, sans le remplacer silencieusement.
[GitHub dans ChatGPT](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt)
et [applications connectées](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt).

Un document fourni dans une conversation n'est pas automatiquement accessible à
une tâche planifiée. Pour le suivi durable, prévoir une source relisible autorisée
ou une synthèse minimale enregistrée dans le privé. Les déclenchements événementiels
décrits comme passant par Work ne font pas partie de cette voie Chat uniquement.
[Documentation des tâches](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt).

**Résultat sauvegardé, sortie dans Chat, notification et réception sont distincts.**
Les notifications natives se règlent dans ChatGPT → Settings → Notifications.
Elles n'autorisent pas un envoi via Gmail et ne prouvent pas sa réalisation.

Ne placer aucune donnée personnelle dans le kit public, ses issues ou ses exemples.
Aucun mot de passe, token, clé privée, lien à usage unique ou export brut sensible
dans les dépôts. Git privé conserve son historique : ce n'est pas un coffre de
secrets. ChatGPT, GitHub et les services connectés gardent leurs propres règles
de traitement des données.

## Si un connecteur est refusé dans ce chat

Pour un refus visant la conversation — notamment `This conversation does not support
developer MCPs` ou `This conversation is restricted to developer MCPs` — essayer
une nouvelle branche **ChatGPT** avec **le même connecteur et le même compte**,
puis vérifier par une lecture minimale. Ne modifier aucune permission.

Il ne s'agit pas d'une branche Git. Cette piste **n'est pas un correctif garanti**.
Un quota, une authentification ou des droits manquants ne sont pas automatiquement
un problème de conversation. En tâche planifiée, signaler le blocage sans créer
une autre tâche ni prétendre ouvrir un nouveau chat.
[Procédure détaillée](docs/MCP_CONVERSATION_RECOVERY.md).

## Documentation

- [Installation](instructions/INSTALLATION.md), [modèle privé](templates/private/README.md) et [scheduler](instructions/SCHEDULER.md)
- [Personnalisation](instructions/README.md), [mission](instructions/MISSION.md), [cycle](instructions/CYCLE.md) et [état](instructions/STATE.md)
- [Mise en service et recette](docs/MISE-EN-SERVICE.md), [positionnement et sources](docs/POSITIONNEMENT.md)
- [Analyse fondatrice](docs/ANALYSE-2026-09-20.md), [sources historiques](docs/SOURCES.md), [feuille de route](docs/ROADMAP.md)

Nom de travail inspiré du majordome de Batman. Projet indépendant, sans affiliation
revendiquée à DC, OpenAI ni aux projets comparés.
