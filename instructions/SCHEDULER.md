# Scheduler natif d'une instance ALFRED

Ce fichier est utilisé une fois la configuration et le test interactif prêts.
La demande directe du propriétaire et ses limites sont obligatoires ; ce document
n'autorise aucune nouvelle tâche. Réutiliser une tâche existante avant toute création.

## Préparer le raccordement

Lire le contrôle et state/tasks.json privés. Résoudre cadence et fuseau déjà choisis.
Une heure explicitement demandée utilise exact_schedule ; « le matin » sans heure
reste flexible_schedule, avec horaire approximatif annoncé. Ne jamais imposer le
fuseau ou l'horaire de l'auteur. Aucun webhook, Work ou autre voie implicite.
Relire la liste native : réutiliser l'identifiant conservé ; après résultat incertain,
rechercher la tâche par ses références exactes avant une nouvelle création.
Si aucune action native n'est exposée, conserver le prompt préparé dans le privé
et signaler « scheduler non créé », sans simuler une installation.

## Prompt de cycle à construire et enregistrer en privé

Préfixer le prompt par le bloc complet MCP-CONVERSATION-RECOVERY-v1 de LANCEMENT.md.
Remplacer PRIVATE_REPO et PRIVATE_BRANCH par la destination vérifiée. Ne pas laisser
de variable non résolue ; garder comptes détaillés, préférences et calendriers privés.
Le scheduler ne doit pas exécuter INSTALLATION.md, ni créer un dépôt à chaque réveil.

```text
Exécute un cycle ALFRED dans Chat uniquement : aucun Work, Codex, Agent mode,
GitHub Actions ni API de modèle externe. Utilise les connecteurs de l'instance,
sans substitution. Le résultat est rendu dans le Chat de cette tâche, pas envoyé
par Gmail en remplacement d'une notification.

Résous main de bacoco/alfred-chatgpt et applique instructions/CYCLE.md,
instructions/STATE.md et leurs références au même SHA. Vérifie le dépôt privé
PRIVATE_REPO sur PRIVATE_BRANCH avant les données ; lis README.md, AGENTS.md,
state/control.json et les chemins d'état déclarés. Reprends cette instance ;
ne lance pas l'installation et ne réinitialise aucun registre.

Sélectionne les seules instances privées actives, dues et autorisées. Les modèles
publics désactivés par défaut ne remplacent pas ce contrôle. Respecte tout arrêt
privé ; ne modifie ni mandat, ni horaire, ni permissions, ni instructions publiques.
Vérifie le compte source exact, effectue de vraies lectures et reprends les fenêtres
pending avant de collecter les nouveautés, avec les budgets privés. Les extraits
ne sont pas des lectures intégrales. Ne fais aucune mutation de messagerie en observe.

Lis les décisions privées avant le briefing. Respecte les résolutions, abandons,
reports et corrections ; ne rouvre pas une affaire depuis un message ancien.
Utilise le verrou coopératif et les écritures conditionnelles ; réconcilie tout
résultat incertain. Sauvegarde uniquement les résumés minimaux, affaires, décisions
reconnues, observations et reçus dans l'instance privée, puis relis-les.
N'avance le checkpoint qu'après couverture et persistance vérifiées. Un cycle
inachevé reste pending ; aucun faux PASS. Préserve les anciennes éditions.

Rends priorités, décisions attendues, échéances, changements et preuves utiles,
sans alerte répétitive sur un sujet inchangé. Distingue résultat sauvegardé,
sortie Chat, notification configurée et réception confirmée. En cas d'accès refusé,
donne outil/erreur exacte, conserve l'état autorisé et ne crée aucun remplacement.
```

## Écrire les preuves du raccordement

Conserver les retours réels dans state/tasks.json (native_scheduler) et setup :
identifiant, titre, VEVENT, timing_mode, état actif et date de vérification.
Activer scheduler_enabled uniquement en cohérence avec la tâche autorisée réellement
créée. En cas d'écriture privée perdue après création, retrouver d'abord cette tâche,
puis réconcilier ; ne pas en créer une autre pour réparer le premier essai.
Un réglage natif modifié doit être relu et réconcilié dans le privé.
Un compte rendu de création ne valide pas encore les connecteurs du prochain réveil.

La sortie Chat, la sauvegarde et les notifications ne sont pas interchangeables.
Signaler des notifications désactivées/inconnues ; les contrôles natifs disponibles
peuvent ne pas permettre de les changer. Ne pas inventer de paramètre d'outil.
La réception n'est confirmée qu'avec une preuve distincte.
Source : [Scheduled tasks](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt),
notamment Settings > Notifications ; consultée le 22 septembre 2026.
