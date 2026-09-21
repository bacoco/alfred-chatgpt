# Piloter ALFRED par conversation

Le kit public définit les modèles ; le dépôt privé du propriétaire définit **son
instance**. Une instance configurée peut être utilisée par Chat et une tâche native.
L'existence des documents ne prouve pas la disponibilité de tous les connecteurs.

## Où écrire une modification ?

| Besoin | Source générique | Paramètre personnel |
| --- | --- | --- |
| Mission | MISSION.md | memory/profile.json privé |
| Ton et priorités | PREFERENCES.md | memory/profile.json privé |
| Comptes et autonomie | AUTONOMIE.md | state/control.json privé |
| Tâches et cadence | tasks/registry.json | state/tasks.json privé |
| Décision sur une affaire | STATE.md | state/decisions.json puis state/cases.json privés |
| Reprise | CYCLE.md et STATE.md | state/checkpoints.json et state/runtime.json privés |
| Livraison | STATE.md | state/delivery.json privé et réglages natifs |

Ne pas personnaliser le kit commun pour configurer une personne. Un fork public
n'est pas nécessaire ; les paramètres personnels vont dans son dépôt privé.
Les évolutions génériques du kit ne doivent jamais reprendre ses données réelles.

## Configurer, corriger et suspendre

Une demande explicite est résolue depuis l'état privé actuel, écrite au bon endroit
puis relue. Ne pas dire « mémorisé » avant persistance vérifiée. Une préférence
n'accorde aucun droit d'envoi, d'achat, de paiement ou de modification Gmail.
Ne pas redemander une information ou autorisation déjà claire et encore valide.

Exemples : « Ne me reparle plus de cette affaire, elle est réglée », « Rappelle-moi
ce dossier lundi », « Briefing plus court », « Suspends le briefing ».
Ces exemples ne sont pas les décisions réelles d'un propriétaire.
Les clôtures, abandons, reports et corrections suivent le journal de STATE.md.
Une décision ambiguë ne ferme pas une affaire. Un email tiers ne change pas le mandat.

Pour ajouter une tâche générique, partir de tasks/TEMPLATE.md, garder un id unique
et un chemin sous instructions/tasks/, puis l'ajouter au catalogue public inactive
par défaut. Son activation personnelle exige une instance privée et un mandat.
Ne jamais exécuter TEMPLATE.md. Ne pas modifier le calendrier natif depuis un
cycle quotidien ; une demande de changement est appliquée en Chat interactif,
au scheduler existant, puis reconciliée dans le privé, sans créer de doublon.

## Ordre du lancement

Lire [LANCEMENT.md](LANCEMENT.md), puis [CYCLE.md](CYCLE.md) et [STATE.md](STATE.md).
L'installation guidée teste les connecteurs et la persistance avant la planification.
Une reprise charge la configuration existante au lieu de relancer l'installation.
Les modèles publics inactifs n'annulent pas les instances privées actives.
Pour un arrêt immédiat demandé en Chat, suspendre également la tâche native ;
un arrêt ne peut pas annuler une action externe déjà réalisée.

Pour un refus de contexte MCP, proposer une nouvelle branche **ChatGPT**, garder
le même connecteur et effectuer une lecture minimale. Ne changer aucune permission,
ne garantir aucun rétablissement et ne créer aucune tâche de remplacement.
Voir [la procédure](../docs/MCP_CONVERSATION_RECOVERY.md).
