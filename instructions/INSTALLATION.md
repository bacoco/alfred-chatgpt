# Installer ALFRED depuis le kit public

Entrée de première installation, version 1.0.1. Exécution dans Chat uniquement.
Le propriétaire copie le paragraphe du README ; il n'a pas à dessiner son dépôt
privé ni écrire les JSON. Effectuer les opérations autorisées, pas seulement un plan.
Une nouvelle branche Chat est une reprise, jamais un motif de recréer les données.

## 1. Charger le kit et reconnaître une reprise

Lire README.md, AGENTS.md, instructions/LANCEMENT.md, instructions/README.md,
CYCLE.md, STATE.md, MEMOIRE.md, MISSION.md, PREFERENCES.md, AUTONOMIE.md et
instructions/tasks/registry.json ; tous les fichiers d'instructions à un même SHA
fraîchement résolu depuis main. Les noms courts ci-dessus sont sous instructions/.
Lire ensuite templates/private/README.md et templates/private/manifest.json à ce SHA.
Une installation existante utilise son contrôle et son journal setup ; ne pas lui
imposer le nouveau modèle ni créer un autre dépôt ou scheduler. Vérifier la tâche
native connue par son identifiant ; une réponse de création perdue exige une recherche.
Ne pas lire le dépôt personnel de l'auteur pour obtenir une configuration par défaut.

## 2. Partir des objectifs, puis choisir les outils

ALFRED est un secrétaire généraliste. Commencer par le résultat que le propriétaire
veut obtenir dans sa vie professionnelle ou personnelle, pas par une boîte mail.
Exemples : suivre un projet, préparer un dossier, structurer des connaissances,
organiser une démarche, préparer une réunion ou surveiller un sujet.
Ne pas imposer Gmail, une cadence quotidienne ou une action extérieure.

Réutiliser les informations déjà claires. Demander uniquement ce qui manque, en
petits groupes : objectifs et résultat attendu ; contexte et sources nécessaires ;
périmètre de lecture, historique, limites par cycle et autonomie ; langue, ton,
priorités ; compte/propriétaire GitHub et nom du dépôt ; cadence et canal utiles.
Conserver les choix validés et leur provenance dans le privé, pas dans le kit public.
Les propositions restent distinctes des préférences confirmées.

Choisir un premier résultat utile en lecture, analyse et préparation, avec persistance
privée autorisée, avant toute action externe. Réutiliser une fiche du catalogue
lorsqu'elle couvre le besoin. Sinon, décrire la fiche, les sources et les tests
manquants ; la nouvelle famille de tâches doit être ajoutée au catalogue par un
changement autorisé avant son activation. Ne pas inventer de template_id valide.
Ne modifier ni le kit commun avec des paramètres personnels ni les droits pour
faire passer une mission non raccordée pour opérationnelle.

Gmail n'est requis que pour une mission utilisant cette messagerie. Pour des contenus
déjà confiés et conservés dans le dépôt privé, identifier cette source GitHub exacte
au lieu d'inventer un compte de messagerie. Pour toute autre source, vérifier son accès
et ses critères de reprise avant de la planifier ; la syntaxe Gmail n'est pas universelle.
Un document seulement téléversé dans Chat n'est pas automatiquement relisible par
la tâche : prévoir une source durable autorisée ou un résumé minimal privé.

Ne pas demander mot de passe, token, clé privée ni copier un export brut sensible.
La demande d'installer autorise la préparation convenue, pas l'accès à tous les comptes.

## 3. Capacités et création du contenant privé

Découvrir les actions du connecteur GitHub sélectionné. Distinguer lecture de fichiers,
écriture de fichiers et CRÉATION DE DÉPÔTS : ce sont trois capacités différentes.
Un get_repo réussi ne prouve pas la création. Ne jamais inventer un outil ou argument.
Vérifier l'identité par une lecture ; le propriétaire de destination doit être celui
vérifié ou une organisation explicitement autorisée, jamais celui du kit par défaut.

Si une action de création est exposée et autorisée, créer le dépôt au nom convenu
avec visibilité **private dès la création**, sans fork du kit public, sans changer
les permissions d'un dépôt existant. Utiliser une initialisation avec README si
l'action le permet, puis résoudre la vraie branche avant d'écrire les fichiers.
Ne pas supposer qu'une API de fichier sait créer une branche ou initialiser un dépôt vide.
Relire les métadonnées : dépôt exact, propriétaire, visibilité privée et branche.

Si la création n'est pas exposée, dire exactement « création du dépôt non disponible
par ce connecteur » ; ne pas arrêter la préparation du modèle. Proposer au propriétaire
la seule étape manquante : créer un dépôt **privé avec un README** dans GitHub, puis
fournir son nom. Retester une lecture avec le même connecteur ; pas de substitution,
changement de permissions, terminal distant ou service extérieur implicite.
Si même l'écriture n'est pas disponible, expliquer la limite et conserver les fichiers
préparés seulement dans le Chat autorisé ; ne déclarer ni installation ni scheduler réussi.

## 4. Générer les seize fichiers, sans perdre un existant

Les chemins du manifeste sont l'unique liste de copie : lire leurs octets au SHA du
kit, vérifier chaque sha256, puis retirer le préfixe templates/private/files/.
Rejeter chemin absolu, `..`, antislash, lien symbolique, doublon, URL ou workflow.
Substituer PRIVATE_REPO, PRIVATE_BRANCH, KIT_SHA, INSTALLATION_ID et RENDERED_AT_UTC
selon templates/private/README.md. KIT_SHA est celui réellement lu ; l'heure est réelle.
Les variables techniques doivent être validées, jamais utilisées comme code ou commande.
Ne copier aucun identifiant personnel depuis une autre installation.
Analyser chaque JSON, vérifier les chemins croisés et l'absence de variable restante.
Le générateur local tools/scaffold_private.py est facultatif, pas un moteur de déploiement.

Inventorier la destination avant l'écriture. Une instance reconnue se reprend.
Un dépôt neuf avec un README d'initialisation peut recevoir le modèle après accord
sur ce remplacement ; toute autre collision exige une fusion explicite, pas un écrasement.
Pour plusieurs fichiers, réutiliser un arbre fondé sur le commit courant puis avancer
la branche sans force ; sinon écrire séquentiellement avec SHA et garder setup incomplet.
Le journal records/INSTALLATION-<id>.json consigne les chemins/empreintes réellement écrits.
Relire tous les fichiers et vérifier leur contenu avant storage_readback_verified=true.
Une opération partielle reprend seulement les manques après comparaison des empreintes.
Ne pas appeler une création de dépôt une seconde fois après une réponse incertaine.
Tester lecture → modification → relecture sur la fixture synthetic=true seulement.

## 5. Configurer, puis faire un vrai premier cycle

Après accord sur le périmètre, compléter state/control.json : identité exacte de chaque
source prévue, connecteur sélectionné, mandat observe versionné, actions permises et
interdites, provenance. Vérifier les comptes réellement nécessaires à la mission.
La persistance privée (restitutions, affaires, décisions, checkpoints et reçus) doit être
explicitement comprise. Enregistrer les paramètres personnels dans memory/profile.json.
Les idées proposées restent distinctes des préférences confirmées ; un contenu tiers
n'est jamais un accord. L'inventaire initial reste vide sauf données réellement confiées.

Compléter state/tasks.json avec les seules tâches choisies, template_id du catalogue,
mandat et compte correspondants, calendrier et plafonds convenus. Vérifier fiche et liens.
Créer les checkpoints prévus par STATE.md et le contrat de la source. Pour une fenêtre
temporelle : compte, filtre/version, bootstrap_start_utc validé, completed_through_utc=null,
overlap_seconds validé et pending_window=null. Pour une autre source, expliciter les
révisions ou critères de couverture nécessaires ; ne pas fabriquer une lecture historique.

Quand cet accord est enregistré et relu : mode=observe, live_processing_enabled=true,
instance choisie enabled=true ; scheduler_enabled reste false avant raccordement natif.
Le cycle interactif autorisé n'exige pas scheduler_enabled=true : ce drapeau concerne
les réveils automatiques. Ne pas présenter le stockage_only initial comme un blocage
après avoir reçu et enregistré l'autorisation métier. external_actions_enabled reste false.

Appliquer CYCLE.md en interactif sur le petit périmètre convenu : identité vérifiée,
lecture effective des contenus requis, analyse, persistance privée et relecture.
Pour le cas Gmail seulement, vérifier le profil, effectuer la vraie recherche et lire
les corps nécessaires. Découvrir des outils ou lire un profil ne valide pas une mission.
Vérifier le résultat contre l'objectif choisi avant interactive_cycle_verified=true.
Quota, pagination inachevée ou refus produisent un état partiel reprenable, pas PASS.
Ne pas accéder à une autre source uniquement parce que le modèle est publié.

## 6. Raccorder la planification choisie

Ne pas imposer un réveil récurrent à une mission ponctuelle. Lorsque la planification
est demandée, suivre [SCHEDULER.md](SCHEDULER.md) ; ne pas copier ce guide d'installation
comme prompt récurrent. Créer ou mettre à jour uniquement la tâche native autorisée,
sans Work, Codex, Agent mode, GitHub Actions ni API de modèle externe.
Conserver en privé l'identifiant et le calendrier vraiment retournés. Réconcilier
state/tasks.json et scheduler_enabled avec cet état, puis relire la configuration.
Ne pas inventer de succès du prochain réveil. scheduled_cycle_verified reste false
jusqu'à une preuve dans la surface planifiée, distincte de l'essai interactif.
Le prochain cycle utilise ses registres existants au lieu de relancer cette installation.

## 7. Terminer avec un état utile

Donner les missions configurées, le dépôt privé, les fichiers créés/repris, les accès
et tests réellement réussis, le statut de la planification et le canal de sortie.
Distinguer notification configurée et réception, et toute extension encore nécessaire.
Les réglages se corrigent ensuite par conversation via instructions/README.md.
Conserver affaires, décisions et historique lors de toute modification.
En cas de restriction de conversation : appliquer la règle embarquée dans LANCEMENT.md,
proposer une branche Chat avec le même connecteur et une lecture, sans garantie.

## Références de capacités, à revalider selon le compte

La [documentation GitHub de ChatGPT](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt)
décrit une intégration en lecture seule ; ne pas promettre ces écritures avec tout
connecteur portant le nom GitHub. Un connecteur avec les actions autorisées requises
est nécessaire. Le schéma des outils et les vrais appels font foi pour chaque capacité.
[Applications](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt) et
[tâches natives](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt) :
disponibilité, actions et notifications dépendent du compte et des permissions.
Références consultées le 22 septembre 2026, pas preuve d'un déploiement universel.
