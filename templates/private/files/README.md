# Mon ALFRED — instance privée

Dépôt : `{{PRIVATE_REPO}}`, branche : `{{PRIVATE_BRANCH}}`.
Kit public : `bacoco/alfred-chatgpt`. Révision de création : `{{KIT_SHA}}`.

## Commencer ou reprendre dans Chat

> Reprends mon ALFRED dans {{PRIVATE_REPO}} sur {{PRIVATE_BRANCH}} : vérifie que
> le dépôt est privé, lis README.md, AGENTS.md et state/control.json, puis reprends
> la configuration ou le cycle selon state/setup.json, sans réinitialiser mes données.

La structure est prête ; l'état réel figure dans `state/setup.json` et les reçus.
Un fichier généré n'est pas une preuve d'accès Gmail ni de scheduler installé.
L'installation guidée complète les paramètres avec le propriétaire : aucun JSON
n'a besoin d'être écrit à la main. Réutiliser les réponses déjà données dans Chat.

| Fichier | Rôle |
| --- | --- |
| `state/setup.json` | Progression de l'installation et preuves ; reprise sans doublon. |
| `state/control.json` | Compte exact, mandat, limites et arrêt global. |
| `state/tasks.json` | Tâches personnelles, cadence, identifiant de la tâche native. |
| `memory/profile.json` | Missions, ton et préférences confirmées. |
| `state/cases.json` | Affaires réelles, références et prochaines actions. |
| `state/decisions.json` | Décisions explicites : régler, abandonner, reporter, corriger. |
| `state/checkpoints.json` | Couverture vérifiée et fenêtres à reprendre. |
| `state/runtime.json` | Réservation coopérative de l'exécution courante. |
| `state/delivery.json` | Résultat Chat et notifications, sans inventer une réception. |
| `state/subscriptions.json` | Inventaire d'abonnements, vide tant que non alimenté. |
| `briefings/` et `records/` | Résultats et reçus privés. |
| `tests/fixtures/` | Tests fictifs exclus des affaires et des briefings. |

## Personnaliser par conversation

« Raccourcis le briefing », « Ce dossier est réglé », « Reporte ce sujet à lundi »
ou « Change l'horaire » : retrouver le contexte, sauvegarder puis relire le changement.
Ces exemples ne constituent pas des décisions réelles sur les affaires.
La tâche native existante est modifiée, pas dupliquée. Les droits restent distincts.

## Limites

L'état initial n'active ni messagerie ni scheduler : la procédure INSTALLATION.md
écrit le mandat convenu avant le premier cycle, puis raccorde la tâche native.
Mode Chat uniquement. Aucun Work, Codex, Agent mode, GitHub Actions ou modèle externe.
Aucun secret, mot de passe, token, lien à usage unique ou export brut dans Git.
Ce dépôt doit rester privé ; jamais de copie des données dans le kit public.
Le stockage Git conserve les anciennes versions, ce n'est pas un coffre de secrets.
En cas de refus de contexte : branche Chat, même connecteur, une lecture de contrôle,
sans changer les permissions ni garantir un rétablissement ; voir AGENTS.md.
