# Rendre ALFRED fonctionnel

Date : 20 septembre 2026. **Plan d'exécution, pas attestation de déploiement.**

## Ce qui est livré

L'étude, les règles de développement et le [kit d'instructions](../instructions/README.md)
sont des documents versionnés. Les trois fiches de tâches sont désactivées.
Le chargeur, le stockage d'affaires, les connecteurs métier raccordés, le moteur
de cycle et la tâche native ALFRED restent à installer ou implémenter et à tester.
Aucun compte personnel n'a été lu et aucune automatisation n'a été créée pour cet ajout.

## Ordre recommandé

| Étape | Travail concret | Preuve attendue avant de passer à la suite |
| --- | --- | --- |
| 1. Contrat et capacités | Relire les deux dépôts existants ; mapper lecture GitHub, messagerie, stockage et approbations par surface. | Un reçu par capacité réellement testée ; pas de déduction depuis un README. |
| 2. État privé | Choisir un stockage existant accessible depuis Chat et la tâche ; séparer connaissances, affaires, mandats et journal. | Écrire puis relire une fixture synthétique ; reprendre dans un contexte neuf. |
| 3. Cycle interactif | Raccorder le chargement de ce dossier, le registre, les checkpoints et les trois fiches, d'abord sur fixtures. | Briefing sourcé et propositions sans écritures externes ; correction et suspension reconnues. |
| 4. Premier périmètre réel | Après autorisation, lire une portion bornée d'une messagerie et préparer les dossiers. | Sujets exacts, sources vérifiables, aucune relance inappropriée sur le lot revu. |
| 5. Planification | Autoriser puis tester une exécution native ponctuelle avant la récurrence. | Même accès et même persistance qu'en Chat ; résultats relus dans la vraie tâche. |
| 6. Actions déléguées | Ajouter d'abord les brouillons approuvés, puis certaines actions sous mandat borné. | Relecture des effets, reprise sans doublon, blocage sur révocation ou résultat incertain. |

Ne pas mettre les étapes 4 à 6 en route du seul fait de publier ce plan.
Le premier objectif utile est « un briefing fiable et des dossiers prêts à agir »,
pas l'automatisation immédiate de tous les comptes.

## Réutilisation avant nouveau code

[Chat-first Operations](https://github.com/bacoco/chatgpt-cost-router) est le candidat
pour les mandats, approbations, journaux et réconciliations. Relire à une révision
exacte `chat_ops/`, `operation_contracts/`, les tests et `docs/DEPLOYMENT_STATUS.md`.
Leur existence documentée ne démontre pas leur rattachement à ce Chat.

[loriq-watch-scheduler](https://github.com/bacoco/loriq-watch-scheduler) fournit des
pistes pour les réservations, checkpoints et reprises. Vérifier ses contrats métier
avant extension ; ALFRED ne doit pas hériter d'une publication publique de veille.
Garder ses occurrences séparées des longues collectes des autres projets.

Ne pas installer Basic Memory, un graphe ou plusieurs agents pour réussir ce premier
cycle si un stockage privé plus simple, déjà disponible, couvre le besoin. Un moteur
sémantique supplémentaire ou une API de modèle n'est pas un prérequis retenu.

## Contrats minimaux à implémenter

Le chargeur fixe un SHA par cycle, valide le registre et ne lit que les fiches
référencées. Les corrections ordinaires s'appliquent au cycle suivant ; les nouveaux
droits demandent un accord distinct. Le statut `enabled` n'est pas un mandat.
La cadence textuelle est résolue une fois avant activation puis conservée en privé.

L'état des affaires conserve identifiant, provenance, statut, échéance, prochaine
action et dernière vérification. Une correction remplace la valeur courante sans
faire disparaître la preuve précédente. Les instances personnelles restent privées.

L'état des cycles conserve version des consignes, occurrence, réservation,
checkpoints, effets connus et inconnus. Un cycle interrompu reprend sans dupliquer
un effet extérieur. Les champs exacts doivent réutiliser les contrats existants.

Le pilote natif fait les vrais appels de connecteurs et enregistre leurs retours.
Ajouter une classe de moteur ou un prompt ne raccorde pas automatiquement les outils.
Un stockage inaccessible bloque la persistance : ne pas simuler une mémoire durable.

## Planification et capacités produit

L'aide officielle consultée le 20 septembre 2026 décrit des tâches récurrentes
pouvant utiliser des applications compatibles, sous réserve du compte et des droits.
Les actions peuvent attendre une approbation. Les fichiers déposés dans un projet
ne constituent pas une mémoire automatiquement accessible à sa tâche.

La cible reste un réveil périodique natif ChatGPT, puis sélection des travaux dus
depuis l'état privé. Les déclenchements événementiels documentés passent par Work :
ne pas y basculer implicitement. Modifier le registre GitHub ne modifie pas à lui
seul l'horaire de la tâche native ; tout changement de réveil doit être réconcilié.

Sources produit : [Scheduled tasks](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt)
et [Connected apps](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt).
Ce constat documentaire ne vaut pas test du compte ni garantie de quota.

## Recette minimale

Tester une correction de préférence, l'ajout d'une fiche désactivée, une suspension,
un identifiant en doublon, un chemin invalide, une source inaccessible, une réponse
tardive, deux cycles concurrents, une permission révoquée et un résultat d'envoi perdu.
Introduire une instruction hostile dans une source synthétique et vérifier qu'elle
ne modifie ni les permissions ni les destinataires ni la destination des données.

En cas de blocage de la tâche native, garder la version interactive et documenter
la capacité manquante ; pas de bascule silencieuse vers Work, Codex ou GitHub Actions.
Mesurer temps de revue, fausses alertes, engagements manqués et doublons plutôt que
nombre de messages produits. Un test local n'est pas une preuve de fonctionnement planifié.
