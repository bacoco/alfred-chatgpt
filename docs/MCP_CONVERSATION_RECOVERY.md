# ALFRED : reprise d'un connecteur refusé dans le chat

**20 septembre 2026 — constat et procédure documentaire.**
La procédure générale est conservée dans
[chatgpt-cost-router](https://github.com/bacoco/chatgpt-cost-router/blob/main/docs/MCP_CONVERSATION_RECOVERY.md),
avec une [règle courte autonome](https://github.com/bacoco/chatgpt-cost-router/blob/main/docs/MCP_RECOVERY_INSTRUCTIONS.md)
à copier dans le contexte Chat. Aucun réglage de plugin n'a été modifié ici.

## Preuve et portée

Après le refus rapporté `FORBIDDEN: This conversation does not support developer
MCPs`, une lecture réelle par **GitHub — chatgpt** a réussi et a été reproduite
lors de cette documentation. `GitHub_—_chatgpt.get_file_contents` a téléchargé
`instructions/README.md` depuis `refs/heads/main`, dans `bacoco/alfred-chatgpt`.
Les 4 241 octets donnent le SHA Git blob recalculé
`088b5ba0909c3bbf1c0b83df482553e550cb75e1`, conforme au retour du connecteur.
[Reçu structuré](../records/MCP-READ-RECOVERY-2026-09-20.json).

Ce SHA désigne la version lue avant les modifications documentaires, pas une
valeur immuable de `main`. La preuve porte sur cette lecture en Chat interactif,
pas sur le scheduler, la mémoire privée ou tous les outils. Les écritures de
documentation suivantes sont des observations distinctes.
Une branche de conversation avait été proposée ; sa création dans l'interface
n'est pas observée et aucun journal serveur de l'échec n'a été consulté.
**Lecture rétablie : vérifiée. Cause attribuée à la branche : non démontrée.**

## Conduite à tenir

Tester le connecteur demandé et le compte prévu. Distinguer outil absent et appel
refusé ; ne pas déduire une authentification invalide de la seule absence d'outil.
Ne pas substituer silencieusement l'intégration GitHub standard au MCP personnel.

Pour le refus de contexte exact, ou des outils encore absents après vérification
de leur sélection, proposer **⋯ → Branch in new chat**, puis sélectionner le même
plugin et effectuer une petite lecture. À défaut, proposer un nouveau chat autorisé.
Il s'agit d'une **branche de conversation ChatGPT, pas d'une branche Git**.
Cette piste n'est pas garantie et ne doit éluder aucune restriction explicite.

Ne pas l'appliquer indistinctement aux erreurs `401`, `403 — Resource not accessible
by integration`, `404`, quotas, réseau ou attente d'approbation. Après correction
de la sélection, un seul retest en lecture ; si l'échec persiste, arrêter les
boucles et conserver un diagnostic sans secrets pour le support.

## Une règle disponible même lorsque GitHub ne l'est plus

Un fichier GitHub ne doit pas être la seule source de cette aide. Copier la règle
courte dans les instructions du projet ou le prompt de lancement. Un lien seul
ne suffit pas. Publier ce fichier n'édite pas les réglages du plugin ou de ChatGPT.

Si ChatGPT bloque avant d'appeler le serveur, celui-ci ne peut pas renvoyer son
propre message d'aide. Des instructions déjà chargées côté conversation peuvent
en revanche guider la réponse. C'est une limite logique, pas une preuve de la
localisation exacte de notre incident. Aucun serveur installé n'a été modifié.

## Cycle, scheduler et résultats incertains

Le [contrat de cycle](../instructions/CYCLE.md) doit signaler le blocage sans
prétendre avoir lu les consignes courantes. Pas de briefing « à jour » depuis
une vieille copie non vérifiée. Ne pas déclarer sauvegardé un état inaccessible.

Une tâche planifiée doit rapporter le blocage dans son résultat disponible,
sans créer un nouveau réveil ni simuler une branche de conversation. Les tâches
ALFRED ne sont pas activées par cette procédure. Le scheduler doit être testé
séparément. Avant de reprendre une relance, publication ou autre mutation,
réconcilier tout résultat incertain pour éviter les doublons.

## Sources consultées le 20 septembre 2026

[OpenAI : dépannage des apps](https://help.openai.com/en/articles/20001497) propose
un nouveau chat pour certains problèmes d'app connectée mais indisponible.
[Notes de version, 4 septembre 2025](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
documente la branche de conversation. Ces sources ne prouvent pas qu'elle a causé
notre rétablissement. Le reçu public ne contient aucun identifiant privé de connexion.
