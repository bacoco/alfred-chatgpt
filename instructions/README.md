# Piloter ALFRED

**Dossier de consignes modifiables, pas un agent déjà installé.**
Le propriétaire peut corriger une règle, préciser une préférence, ajouter une
mission ou en suspendre une depuis GitHub ou en le demandant dans ChatGPT.
Les changements doivent être écrits dans le bon fichier puis relus sur GitHub.

## Où modifier quoi ?

| Besoin | Fichier canonique |
| --- | --- |
| Changer le résultat global attendu | [MISSION.md](MISSION.md) |
| Modifier le ton, les priorités ou le format du briefing | [PREFERENCES.md](PREFERENCES.md) |
| Définir les limites d'autonomie | [AUTONOMIE.md](AUTONOMIE.md) |
| Changer le chargement des consignes et le déroulement d'un cycle | [CYCLE.md](CYCLE.md) |
| Ajouter, suspendre ou prioriser une tâche ; proposer sa cadence | [tasks/registry.json](tasks/registry.json) |
| Décrire le résultat d'une nouvelle tâche | [tasks/TEMPLATE.md](tasks/TEMPLATE.md) |

`AGENTS.md` guide le développement du projet. Ce dossier guide le comportement
métier d'ALFRED. Une issue sert à discuter une évolution ; elle n'est pas une
instruction exécutable. Seules les fiches référencées au registre sont candidates.

## Ajouter une tâche

Copier `tasks/TEMPLATE.md` sous un nom stable, puis compléter son objectif,
ses sources nécessaires, son résultat attendu et ses limites. Ajouter au registre
un objet de même structure que les exemples existants, avec un `id` unique,
le chemin de la fiche et `enabled: false`. Une tâche peut être récurrente ou
ponctuelle (`schedule_kind: recurring` ou `once`). Ne pas exécuter le modèle.

Les champs `cadence` expriment une demande en langage naturel, pas une expression
cron opérationnelle. Avant activation, la cadence doit être résolue en calendrier
précis avec fuseau, première échéance et règle de rattrapage ; conserver ce
calendrier dans l'état privé. Une priorité plus petite passe avant une plus grande.

`enabled: true` signifie « exécution demandée », jamais « pouvoir accordé ».
L'exécution exige aussi un runtime actif, les capacités vérifiées et un mandat
privé couvrant les comptes et les actions. Aucun de ces éléments n'est créé ici.

## Corriger, suspendre, reprendre

Modifier une fiche conserve son `id` : ne pas créer un doublon pour la corriger.
Mettre `enabled: false` demande sa suspension au prochain point de contrôle.
Reprendre exige de relire l'état privé : ne pas relancer les anciennes occurrences
ni les effets incertains. Ne pas supprimer un historique d'exécution pour repartir.

Exemples de demandes dans ChatGPT :

> Dans ALFRED, prépare les relances après sept jours ouvrés, sans les envoyer.

> Ajoute une tâche générique de comparaison annuelle des assurances, désactivée.

> Suspends la comparaison des abonnements ; conserve le briefing.

La conversation doit produire une modification vérifiée du dépôt, pas seulement
une promesse de mémorisation. Une consigne nominative ou confidentielle va dans
la configuration privée, jamais dans les fichiers publics ou une issue publique.

## Prise en compte par le futur runtime

Chaque cycle charge les consignes à une révision Git unique selon [CYCLE.md](CYCLE.md).
Les corrections ordinaires restent dans le mandat existant. Un nouveau compte,
un envoi, une dépense ou des droits plus larges exigent une autorisation séparée.
Une modification Git ne reprogramme pas toute seule une Scheduled Task ChatGPT.

Le futur pilote devra relire ce dossier à chaque réveil. Tant qu'il n'est pas
raccordé et testé, aucun changement ici ne déclenche une action réelle.
Pour un arrêt immédiat, suspendre aussi la tâche native dans ChatGPT ; une
suspension ne peut pas annuler un mail déjà envoyé.

## Public / privé

Ce dépôt est public : il conserve le kit, des règles génériques et des exemples.
Le profil réel, les identifiants de comptes, destinataires, affaires, factures,
mandats, échéances personnelles et reçus restent dans un stockage privé hors Git.
Les instances personnelles des tâches utilisent ce stockage, sans exposer leurs
paramètres dans le catalogue public. Ne jamais placer une clé ou un jeton ici.

Prochaine étape : [mise en service](../docs/MISE-EN-SERVICE.md).

## Si GitHub est connecté mais inutilisable dans ce chat

Voir la [reprise MCP documentée](../docs/MCP_CONVERSATION_RECOVERY.md).
Après vérification de la sélection, un refus visant le contexte peut justifier
une nouvelle branche **de conversation ChatGPT**, puis un retest de lecture.
Ce n'est ni un correctif garanti, ni une branche Git, ni une autorisation nouvelle.
La règle courte doit aussi être présente dans le contexte de lancement : un lien
GitHub seul ne permet pas d'obtenir l'aide lorsque GitHub est bloqué.
