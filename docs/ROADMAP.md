# Feuille de route proposée

Date : 20 septembre 2026. **Proposition de l'étude ; aucune phase n'est activée.**

## Phase 0 — Vérifier les capacités et l'existant

Relire le code, les tests et les derniers reçus de `chatgpt-cost-router` et `loriq-watch-scheduler`. Recenser séparément les capacités de Chat interactif et de la tâche planifiée. Vérifier les droits du compte, la lecture d'un registre, la persistance d'un checkpoint et les actions des connecteurs requis.

Comparer le coût et la complexité des briques candidates avant adoption. Ne pas interpréter leur documentation comme une preuve d'installation.

**Critère de sortie :** matrice de capacités sourcée, architecture minimale choisie, stockage privé identifié, inconnues et restrictions explicites.

## Phase 1 — Registre et briefing

Définir le profil personnalisable, le registre des affaires ouvertes et un inventaire d'abonnements. Conserver les sources, les dates, les inconnues et les états de validité. Prévoir une ingestion incrémentale et une correction simple par l'utilisateur.

Commencer sur des fixtures synthétiques, puis sur un périmètre de lecture explicitement autorisé. Ne pas envoyer de relances.

**Critère de sortie :** chaque affirmation importante et chaque échéance ont une preuve ou un statut d'incertitude ; le briefing réduit réellement le travail de revue.

## Phase 2 — Dossiers prêts à agir

Préparer relances, rendez-vous, comparatifs et lettres avec leurs pièces justificatives. Relire les derniers échanges avant de proposer l'action. Ne pas confondre absence de réponse et nécessité de relance, ni absence de trace et non-utilisation d'un abonnement.

**Critère de sortie :** décisions prêtes à arbitrer, tests des faux positifs, des réponses tardives, des doublons et des dossiers déjà résolus.

## Phase 3 — Mandats et exécution déléguée

Concevoir une extension de mandat borné en examinant d'abord les approbations exactes existantes. Lier l'autorisation aux comptes, ressources, destinataires, catégories d'action, plafonds, délais et conditions d'arrêt. Respecter toutes les confirmations imposées par les services.

Introduire journalisation, relecture après écriture et réconciliation. Ne jamais promettre un « exactement une fois » universel pour un fournisseur externe : gérer les résultats inconnus de manière conservatrice.

**Critère de sortie :** aucun double effet dans les scénarios testés ; pas d'action hors mandat ; preuves de résultat et cas d'incertitude correctement conservés.

## Phase 4 — Extensions mesurées

Élargir aux documents, à l'agenda et aux projets selon les capacités démontrées et la valeur constatée. N'introduire graphe, multi-agent, nouvelle API ou nouveau runtime qu'avec un besoin non couvert et un gain mesuré.

## Indicateurs

Mesurer engagements manqués, fausses relances, doublons, actions non autorisées, erreurs de mémoire, interventions inutiles, corrections utilisateur, temps de revue, coût par dossier et affaires réellement résolues.

Les taux et seuils d'acceptation doivent être décidés avec le propriétaire ; aucun niveau de fiabilité n'est annoncé par ce dossier documentaire.
