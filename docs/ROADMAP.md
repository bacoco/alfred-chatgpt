# Feuille de route — préserver le noyau de continuité

Cadrage du 23 septembre 2026 après le [retour produit #6](https://github.com/bacoco/alfred-chatgpt/issues/6).
Aucune phase ni nouvelle permission n'est activée par ce document.
La [proposition initiale du 20 septembre](https://github.com/bacoco/alfred-chatgpt/blob/68a1f154b6375c4fba1eb1a791582d604847196d/docs/ROADMAP.md)
est conservée dans l'historique ; elle n'est pas un état de déploiement.

## 1. Stabiliser le noyau existant

Appliquer le [positionnement](POSITIONNEMENT.md) : affaire canonique, décisions,
provenance, checkpoints, réconciliation et livraison observable. Ne pas créer un
second scheduler ni refaire les registres privés pour ajouter ces précisions.

Les compléments de reprise, identité, installation et observation sont des contrats
et contrôles du kit. Ils ne règlent pas à eux seuls les causes de refus ou retards
externes. Conserver leur diagnostic et les limites de preuve.

Critère : non-régression sur les invariants et lecture des effets réellement produits ;
aucun écrasement, double effet ou élargissement d'autorisation dans la recette exécutée.

## 2. Revalider une instance à la nouvelle révision

Suivre [MISE-EN-SERVICE.md](MISE-EN-SERVICE.md) sous mandat borné. Tester d'abord des
fixtures, puis les sources autorisées. Deux cycles successifs doivent conserver les
mêmes affaires et décisions, gérer les nouveaux signaux et préserver la provenance.
Tester aussi séparation d'une fusion erronée, interruption, conflit, refus explicite,
réponse tardive et résultat de scheduler non encore observable.

Les 29 PASS du [bilan externe](RETEX-2026-09-22.md) ne sont pas relabellisés comme
preuve de la révision nouvelle. Une capacité interactive ne valide pas la surface
planifiée. Une tâche créée ne prouve ni le cycle exécuté ni la réception du briefing.

Critère : reçus privés de la révision testée, couverture et relecture vérifiées,
limites nommées, puis seulement activation de la cadence expressément convenue.

## 3. Ajouter une action seulement si une affaire le justifie

Réutiliser les contrats existants de mandat, approbation et réconciliation avant
toute nouvelle action déléguée. Vérifier comptes, ressources, destinataires, plafonds,
conditions d'arrêt et capacité effective. Pas de relance d'essai sur un tiers réel
pour simplement obtenir un test vert. Les fixtures ne prouvent pas un envoi réel.

Critère : besoin de continuité documenté, absence d'action hors mandat, preuve de
l'effet, reprise sans répétition aveugle et retour arrière défini.

## 4. Extensions mesurées, pas catalogue universel

Une nouvelle source ou mission doit démontrer ce qu'elle apporte à une affaire
persistante et pourquoi les outils existants ne suffisent pas. Définir couverture,
identité, reprise, confidentialité et tests avant ajout. Garder la fiche inactive
par défaut. Une extension n'exige ni un autre modèle ni un moteur d'agents par principe.

Sans besoin de continuité, préférer une conversation ou une tâche native compatible
simple. Ne pas transformer toute demande ponctuelle en infrastructure ALFRED.

## Indicateurs

Mesurer engagements manqués, doublons, fausses relances, erreurs de fusion,
provenances perdues, décisions oubliées, interventions inutiles et temps de revue.
Distinguer résultats constatés, scénarios synthétiques et fonctionnalités non testées.
Les seuils sont convenus avec le propriétaire ; aucune fiabilité universelle n'est
annoncée à partir de la seule publication de ce kit.
