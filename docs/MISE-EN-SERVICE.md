# Mise en service et vérification d'une instance

Mise à jour : 21 septembre 2026. Le kit public est réutilisable ; chaque instance
a ses propres accès, paramètres et preuves privées. Ne pas confondre existence
d'un fichier, exécution d'un cycle et réception d'une notification.

## Installer ou reprendre

Utiliser la phrase du README et [LANCEMENT.md](../instructions/LANCEMENT.md).
Reprendre d'abord l'existant : dépôt privé, tâche native, registres et accords.
Ne pas créer une nouvelle tâche ni remettre les données à zéro pour une mise à jour.
Le raisonnement et les appels restent en Chat, sans Work, Codex, Agent mode,
GitHub Actions ou API de modèle externe. Le texte d'un prompt ne peut pas modifier
les permissions ni garantir la surface d'exécution offerte par la plateforme.

## Configuration minimale cohérente

Vérifier le dépôt privé et ses droits avant les données. Tester le compte source
par une vraie lecture ; enregistrer l'adresse exacte, jamais « compte connecté ».
Conserver le mandat courant dans state/control.json, les tâches actives dans
state/tasks.json, et les préférences personnelles dans memory/profile.json.
Les fichiers privés de reprise, décisions et livraison suivent
[STATE.md](../instructions/STATE.md). Le catalogue public reste générique.

Fixer la cadence et le fuseau depuis l'accord du propriétaire et le retour du
scheduler, pas depuis une supposition. Les paramètres techniques prudents doivent
être nommés comme défauts modifiables, pas comme préférences prétendument exprimées.
Un envoi Gmail, un brouillon, un label ou une action sur un autre compte demande
un mandat spécifique. L'activation du briefing n'active aucune de ces actions.

## Recette observable

1. Lire Gmail réellement, analyser un lot borné et relier les affaires existantes.
2. Écrire et relire briefing, observations et reçu dans le dépôt privé.
3. Tester une décision synthétique isolée : report, résolution/abandon, rejeu sans doublon.
4. Tester les fenêtres fixes après jours manqués, l'interruption et la non-avance
   du checkpoint quand une page ou une lecture requise reste inachevée.
5. Mettre à jour la tâche native existante ; préserver son horaire et ses limites.
6. Distinguer test interactif et véritable exécution planifiée. Ne pas annoncer
   un succès du nouveau contrat en tâche planifiée sur la base d'un test en Chat.
7. Contrôler la livraison : fichier sauvegardé, sortie Chat, notifications activées,
   puis réception attestée. Un « PASS Gmail + mémoire » ne prouve que ces deux étapes.

Les anciens reçus restent des preuves de leur version ; ne pas les renommer en
preuves du contrat courant. Une couverture relative sans bornes exactes ne doit
pas être convertie en faux checkpoint. Un test incomplet conserve son diagnostic.

## Notifications

Les notifications natives de tâches ne sont pas des emails envoyés par ALFRED via
Gmail. Lire les champs réellement disponibles. S'ils sont désactivés ou si leur
modification n'est pas exposée par l'outil, enregistrer la limite sans inventer une
activation ni contourner via un autre canal. L'utilisateur peut contrôler ses
options dans ChatGPT : Settings > Notifications, Push et/ou Email.
Source officielle consultée le 21 septembre 2026 :
https://help.openai.com/en/articles/10291617-tasks-in-chatgpt
Le réglage disponible et la réception effective restent à vérifier pour chaque compte.

## Limites de cette version

Le contrat est exécuté par Chat avec ses connecteurs, pas par un moteur serveur
caché. Les réservations sont coopératives, les capacités peuvent varier selon la
surface, et la fiabilité sur plusieurs jours exige plusieurs preuves réelles.
Réutiliser l'état, les contrôles de base Git et les tâches existantes ; ne pas
installer un nouveau service d'agent pour masquer un blocage de connecteur.
