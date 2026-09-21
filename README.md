# ALFRED — Personal secretary in ChatGPT Chat

**Un secrétaire personnel qui connaît ton contexte, suit tes affaires et vérifie les résultats.**
Nom de travail : ALFRED, en référence au majordome de Batman.

> Un second cerveau retrouve ce que tu sais. Un secrétaire sait aussi ce qui reste
> à faire, qui attend quoi, quand intervenir et si une action a réellement abouti.

## Installer son ALFRED : une phrase dans Chat

Dans un nouveau ChatGPT **Chat**, sélectionner les connecteurs que l'on souhaite
utiliser, puis copier :

```text
Installe ALFRED pour moi à partir de bacoco/alfred-chatgpt. Guide-moi pour définir ce que mon secrétaire doit faire, crée ou configure un dépôt GitHub privé séparé pour ma mémoire personnelle, teste les connecteurs réellement disponibles, puis mets en place avec mon accord un scheduler ChatGPT natif selon la cadence que je choisis. Reste en mode Chat uniquement et applique instructions/LANCEMENT.md.
```

Chat lit le kit, discute des missions, sources, priorités, ton et limites, puis
configure **le dépôt privé de cette personne**, teste lecture et persistance,
et crée la tâche native autorisée. Ni le nom du dépôt privé ni son horaire ne
sont imposés. Aucun mot de passe ni token ne doit être communiqué ou commité.
Si une capacité manque, le résultat indique précisément l'étape non réalisée.
La phrase amorce une installation guidée, pas un déploiement garanti sans accès.

Une instance déjà configurée est **reprise**, pas réinstallée : retrouver sa tâche
native et ses registres, sans doublon ni remise à zéro. Aucun fork public n'est
nécessaire pour personnaliser son secrétaire.

## Deux dépôts, deux rôles

| Kit public | Instance privée de chaque utilisateur |
| --- | --- |
| Mission et règles génériques | Préférences, comptes et mandats personnels |
| Catalogue de modèles de tâches | state/tasks.json : ses tâches réellement actives |
| Contrat CYCLE.md et STATE.md | Affaires, décisions, checkpoints et reçus |
| Documentation et exemples synthétiques | Analyses et briefings issus de ses sources |

Le `enabled:false` du catalogue public est un **défaut de modèle**, pas un arrêt
des installations existantes. L'activation vient de la tâche privée autorisée et
du contrôle privé courant. Les droits des connecteurs restent obligatoires.

## Le modifier simplement en parlant

Par exemple : « Ce dossier est réglé », « Abandonne cette affaire », « Rappelle-moi
lundi », « Raccourcis le briefing », « Change l'horaire du matin ».
ALFRED retrouve la configuration ou l'affaire, enregistre la décision privée,
applique la modification permise et relit le résultat. Une ambiguïté ne ferme
pas une affaire et une préférence ne donne aucun nouveau droit d'action.

Les décisions sont conservées dans state/decisions.json ; les résolutions et
abandons arrêtent les rappels, les reports suivent la date convenue. Un message
ancien ne recrée pas une affaire fermée. Voir [le contrat d'état](instructions/STATE.md).

## Reprise et livraison

Le cycle reprend une fenêtre inachevée et conserve un checkpoint de couverture
vérifié. Il ne suppose pas que la veille a réussi et ne recommence pas aveuglément
les actions. Un budget atteint garde les éléments non traités pour la reprise.
Les constats issus d'extraits sont distingués des messages lus intégralement.

**Briefing sauvegardé, résultat émis dans Chat, notification configurée et réception
confirmée sont quatre étapes distinctes.** La notification native se règle dans
ChatGPT Settings > Notifications (Push et/ou Email). Elle n'autorise pas ALFRED
à envoyer des mails via Gmail. Un canal désactivé reste signalé, sans faux succès.

## Si un connecteur est refusé dans la conversation

Pour `This conversation does not support developer MCPs`,
`This conversation is restricted to developer MCPs`, ou des outils absents après
vérification de leur sélection : essayer en Chat interactif **⋯ → Branch in new chat**,
conserver **le même connecteur et le même compte**, puis effectuer **une lecture
minimale vérifiable**. À défaut, essayer un nouveau Chat autorisé.

Il s'agit d'une **branche de conversation ChatGPT, pas d'une branche Git**.
Cette piste a été suivie d'un rétablissement lors d'un test, mais **ce n'est pas
un correctif garanti et sa causalité n'est pas démontrée**. Ne changer ni de
connecteur ni de permissions pour contourner un refus. Une erreur de quota,
d'authentification ou de droits n'est pas automatiquement un problème de contexte.
En tâche planifiée : rapporter le blocage, sans créer une tâche de remplacement
ni prétendre ouvrir une nouvelle conversation.
[Procédure détaillée](docs/MCP_CONVERSATION_RECOVERY.md).

## Périmètre et architecture

ALFRED vise correspondance, affaires, échéances, abonnements, agenda, contacts et
documents ; chaque source et chaque action nécessitent leur propre autorisation.
Commencer par le briefing observe n'active ni relances ni achats ni mutations Gmail.

ChatGPT Chat raisonne et appelle les connecteurs autorisés. GitHub conserve le kit
et, séparément, l'état privé. Les contrôles sont appliqués par le pilote Chat ;
un fichier d'instructions n'est ni un moteur serveur ni une preuve d'exécution.
Pas de bascule implicite vers Work, Codex, Agent mode, GitHub Actions ou une API
de modèle externe. Vérifier séparément chaque surface et chaque nouvelle version.

## Confidentialité

Aucun email réel, profil, facture, contrat, mandat personnel ni journal privé dans
ce dépôt public, ses issues ou ses fixtures. Aucun secret, token, clé privée,
lien de confirmation à usage unique ou export brut très sensible dans aucun dépôt.
Le stockage Git privé conserve son historique ; ce n'est pas un coffre de secrets.

## Documentation

- [Lancement et configuration guidée](instructions/LANCEMENT.md)
- [Où personnaliser quoi](instructions/README.md)
- [Contrat de cycle](instructions/CYCLE.md) et [état privé](instructions/STATE.md)
- [Mise en service et recette](docs/MISE-EN-SERVICE.md)
- [Analyse fondatrice](docs/ANALYSE-2026-09-20.md), [sources](docs/SOURCES.md), [feuille de route](docs/ROADMAP.md)

Projet indépendant ; aucune affiliation à DC ou OpenAI n'est revendiquée.
