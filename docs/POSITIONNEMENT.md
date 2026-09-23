# ALFRED : noyau de continuité et d'état

Décision de cadrage du 23 septembre 2026, issue du
[retour produit #6](https://github.com/bacoco/alfred-chatgpt/issues/6).
Ce document définit le périmètre du kit ; il n'active aucune instance.
La [comparaison documentaire du 22 septembre](https://github.com/bacoco/alfred-chatgpt/blob/68a1f154b6375c4fba1eb1a791582d604847196d/docs/POSITIONNEMENT.md)
reste consultable avec ses sources et limites, sans être présentée comme une étude actualisée.

## Le besoin qui justifie ALFRED

Un secrétaire persistant suit des affaires qui traversent plusieurs jours, sources
et décisions. Sa valeur recherchée est de reprendre **la même affaire**, pas de
refaire chaque matin un résumé indépendant ni de connecter tous les services.
Les domaines peuvent varier : projet, démarche, correspondance, rendez-vous,
abonnement. Le besoin de continuité, et non le nom du domaine, justifie le kit.

Sans état à conserver, utiliser Chat ou une tâche native compatible directement.
Une recherche ponctuelle n'exige pas un registre d'affaires. Une répétition seule
ne justifie pas une couche d'orchestration supplémentaire.

## Le plus petit noyau à préserver

| Responsabilité | Contrat existant à réutiliser | Ce qu'il ne faut pas dupliquer |
| --- | --- | --- |
| Identifier une affaire et relier ses preuves | STATE.md et CASE_IDENTITY.md ; state/cases.json privé | Un registre par source ou une fusion par seul titre. |
| Respecter les décisions | STATE.md ; state/decisions.json privé | Une autre autorité fondée sur un email ou une suggestion. |
| Reprendre la couverture et le travail interrompu | CYCLE.md et STATE.md ; checkpoints/runtime privés | Une deuxième file ou un nouveau cycle qui ignore pending. |
| Réconcilier les effets et écrire sous contrôle | STATE.md et WRITE_RECOVERY.md ; reçus privés | Un retry aveugle ou un moteur d'actions sans mandat. |
| Qualifier l'exécution et la livraison | SCHEDULER.md et SCHEDULER_OBSERVABILITY.md | Un scheduler ALFRED parallèle ou une notification assimilée à une réception. |

ChatGPT fournit le raisonnement ; le scheduler natif fournit le réveil ; les
connecteurs fournissent les accès permis ; GitHub privé fournit le stockage.
ALFRED fixe leur protocole de continuité. Les aides Python locales contrôlent des
invariants ; elles ne sont ni un daemon ni un moteur sémantique de remplacement.

## Une séquence qui montre la différence

Scénario synthétique : une invitation, des échanges et des événements d'agenda
sont reliés au même rendez-vous après vérification. Le propriétaire le reporte.
Au cycle suivant, ALFRED conserve ce report, rattache un nouveau message à l'affaire
existante et ne recrée pas une relance à partir d'un ancien signal.
Si la fusion initiale était fausse, une correction sépare les dossiers sans perdre
les sources ni l'historique. Si une écriture est incertaine, lire l'état réel avant
une nouvelle tentative. Cette continuité est le résultat attendu.

## Limites de la V1 et conditions d'extension

« Noyau V1 à préserver » est une priorité de maintenance, pas une certification
de production. Le [bilan externe](RETEX-2026-09-22.md) reste une preuve rapportée,
liée à une ancienne révision et à son instance. Les nouveaux tests structurels ne
certifient ni les rapprochements sémantiques sur des mails réels ni les accès futurs.

Avant toute extension, documenter : l'affaire persistante à mieux suivre ; le manque
observé ; la réutilisation examinée ; le contrat minimal ; les droits et données
nécessaires ; les tests de régression ; le retour arrière. Sans gain de continuité
identifiable, ne pas ajouter la fonction au noyau.

Ne pas lancer un assistant universel, multiplier les agents, installer une base
sémantique ou ajouter des dizaines de connecteurs par défaut. Une nouvelle fiche
reste inactive jusqu'à son mandat et sa recette. Gmail demeure optionnel.
Les décisions d'instance et permissions actuelles ne changent pas avec ce cadrage.

## Critères de conservation

Préserver une affaire stable entre deux cycles, toutes ses provenances et les
décisions antérieures. Réduire doublons et interventions inutiles, sans masquer
les incertitudes. Prouver chaque effet avant de le qualifier de réussi.
Mesurer ces résultats dans une recette autorisée plutôt que compter les connecteurs.
La [feuille de route](ROADMAP.md) applique ces critères aux prochains changements.
