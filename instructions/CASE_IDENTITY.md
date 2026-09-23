# Identité canonique des affaires

Contrat complémentaire de STATE.md, à lire avant tout rapprochement de signaux.
Référence : [issue #3](https://github.com/bacoco/alfred-chatgpt/issues/3).
Utiliser state/cases.json et state/decisions.json existants, jamais un registre parallèle.

## Ce qui identifie une affaire

Une affaire représente un objet métier suivi dans le temps, pas un titre, un mail
ou un événement. Garder son identifiant existant stable quand ses sources évoluent.
Un titre normalisé sert à trouver des candidats, jamais à prouver leur identité.
Un fingerprint de présentation n'est pas une clé métier ni une autorisation de fusion.

Traiter deux niveaux séparés :
- signal exact : source + compte exact + identifiant natif, avec portion explicite
  lorsqu'un même document concerne plusieurs affaires ;
- objet métier : référence métier fiable (par exemple UID de rendez-vous, dépôt et
  workflow, dossier fournisseur), participants, dates et liens de provenance cohérents.

Ne pas fusionner deux workflows parce qu'ils partagent un message d'erreur.
Une notification d'une nouvelle tentative peut enrichir le même incident ; une
nouvelle exécution indépendante peut être une autre affaire. Vérifier la continuité.
Pour Calendar, confronter UID, dates/fuseaux et participants aux invitations Gmail.
Un événement automatique et un événement explicite ne sont pas nécessairement identiques.
Une référence fiable contradictoire prime sur une ressemblance de titre.

## Décision avant projection

Relire les décisions du propriétaire et les affaires candidates, y compris fermées.
Décider entre SAME_OBJECT, DISTINCT_OBJECT et UNCERTAIN, avec raisons et preuves.
En UNCERTAIN, garder un candidat à arbitrer ; ne pas fusionner ou déclencher deux
relances concurrentes. N'inventer ni score de confiance ni référence manquante.
Une séparation explicite par le propriétaire prime sur le rapprochement automatique.

SAME_OBJECT enrichit l'affaire canonique avec l'union des références, sans doublon
exact. DISTINCT_OBJECT crée une affaire seulement si l'objet n'existe pas déjà.
Une nouvelle source n'est pas en soi un changement matériel ni une réouverture.
Resolve/drop/snooze et leur état de rappel restent appliqués. Un signal ancien,
réindexé ou présent dans l'overlap ne les annule pas. Un changement réellement
matériel est exposé avec preuve ; toute transition suit la décision ou le mandat
courant de STATE.md, sans élargissement implicite des droits.

## Représentation compatible avec les instances existantes

Ne pas renommer les IDs existants ni réécrire tous les dossiers à la lecture du kit.
Pour une affaire effectivement traitée, ajouter progressivement les métadonnées
manquantes sous un objet `identity`, après relecture et écriture autorisées :

```json
{
  "canonical_case_id": "CASE-SYNTHETIC-A",
  "source_refs": ["gmail/test/message-1", "calendar/test/event-1"],
  "aliases": [],
  "identity_reason": "Même rendez-vous selon les références vérifiées"
}
```

Exemple exclusivement synthétique. En privé, chaque référence doit résoudre vers
la provenance minimale déjà conservée ; aucune clé secrète ni contenu brut.
`aliases` ne contient que les anciens IDs d'affaires fusionnées, pas les titres.
Conserver dans la projection canonique toutes les références de l'affaire fusionnée.
Garder aussi l'ancienne affaire avec son ID, ses références, son historique et un
pointeur direct vers le canonique. Interdire cycles, cibles absentes et chaînes
opaques d'alias. Les rappels utilisent uniquement l'affaire canonique.

Le journal de décision garde operation_id, IDs concernés, références avant/après,
raison, preuve de la décision, date observée et projection_status. Pour une
correction propriétaire, utiliser le type `correct` existant et supersedes.
Journal d'abord, projection ensuite ; reprise d'une projection pending avant un
nouveau rapprochement. Une même operation_id est NOOP après relecture vérifiée.

## Corriger une mauvaise fusion

Conserver l'événement de fusion dans l'historique, puis journaliser la séparation.
Restaurer les anciens IDs quand ils existent, répartir les références selon les
preuves et enlever uniquement les alias devenus faux. Les références communes
peuvent rester dans plusieurs affaires si leurs portions et rôles sont explicites.
Ne perdre aucune provenance ; ne pas réactiver un rappel fermé sans décision.
Une séparation est une nouvelle projection, pas un effacement de l'ancienne preuve.

## Validation sans second moteur sémantique

[case_identity.py](../tools/case_identity.py) valide des **projections** : case_id
reprend l'ID existant, les champs d'identity sont aplatis pour le contrôle, status
reprend l'état courant. Le validateur n'impose pas de migration du fichier source.
Il contrôle liens, alias, doublons exacts, préservation des références et décisions
protégées. authorized_reopens ne contient que les IDs dont la transition a déjà
été autorisée et vérifiée ; le paramètre ne crée aucune permission.
Il n'infère pas qu'un mail et un rendez-vous sont le même objet : Chat doit établir
et consigner ce jugement. Aucun embedding, service, compte ou tâche supplémentaire.

## Recette reproductible

`python -m unittest discover -s tests -p test_case_identity.py -v`

Les fixtures du test couvrent : cinq notifications d'un incident ; deux workflows
voisins ; invitation + fil + deux événements ; même titre mais dates distinctes ;
séparation manuelle ; ancien signal après resolve/drop/snooze ; cycles d'alias,
provenance perdue et doublons exacts. Les groupements attendus sont synthétiques.
Les tests automatisés vérifient les invariants des projections, pas la qualité du
jugement sémantique sur des mails réels. Sur une instance autorisée, rejouer deux
cycles puis une correction manuelle et conserver les reçus privés ; ne pas présenter
la campagne historique comme une validation de cette nouvelle révision.
