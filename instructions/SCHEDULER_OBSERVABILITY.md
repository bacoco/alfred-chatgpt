# Observer une occurrence sans la rejouer

Complément obligatoire de SCHEDULER.md pour tout test ou contrôle du raccordement.
Référence : [issue #5](https://github.com/bacoco/alfred-chatgpt/issues/5).
Ce protocole n'est pas un autre scheduler. Il utilise les tâches et reçus existants.

## Identité et horloges séparées

Pour une occurrence, conserver en privé : task_id natif, operation_id, SHA du kit
épinglé, scheduled_for avec fuseau, début métier réellement connu, date de
persistance du reçu, last_run_time natif et date d'observation. Une valeur absente
reste null ; ne pas la déduire d'une autre horloge. Pour un récurrent, une preuve
de l'occurrence précédente ne valide jamais la suivante.

Réutiliser state/tasks.json.native_scheduler pour la configuration et
state/setup.json pour l'état de raccordement. Les observations détaillées peuvent
aller dans un objet scheduler_observation de setup, avec les références des reçus
sous records/. Ne pas inventer un registre concurrent ni réinitialiser l'instance.
Une absence de ces champs dans une ancienne instance signifie « non documenté ».

## États fondés sur les preuves

| Preuve observée pour l'occurrence exacte | État du contrôle |
| --- | --- |
| Tâche et configuration non vérifiées | scheduler_configuration_unverified |
| Tâche créée, horaire pas encore atteint | scheduler_created |
| Horaire dépassé, aucun run ni reçu attribuable | scheduler_run_uncertain |
| Run attribuable, mais traitement non encore validé | scheduler_run_observed_unverified |
| Reçu validé mais travail incomplet | scheduler_run_partial |
| Reçu BUSY, autre réservation en cours | scheduler_run_busy |
| Reçu de blocage réel | scheduler_run_blocked |
| Identité, surface ou révision incohérente | scheduler_evidence_mismatch |
| Cycle planifié, connecteurs, couverture, persistance et relecture vérifiés | scheduled_cycle_verified |

`is_enabled=true` ne prouve pas un démarrage ; `is_enabled=false` ne prouve pas
l'échec d'un one-shot terminé. Un last_run_time renseigné ne prouve ni la bonne
occurrence ni sa réussite. Un fichier intitulé « scheduled » ne prouve pas la surface.
Un cycle interactif ne remplace pas la preuve du cycle planifié.

## Quand DTSTART est dépassé et last_run_time est null

Rendre l'état incertain, sans conclure « jamais déclenché » ou « Gmail inaccessible ».
Relire la même tâche et rechercher les reçus associés à la même occurrence.
Vérifier provenance, surface planifiée, révision, empreintes, couverture et effets.
Un reçu complet réellement revalidé peut être disponible avant la métadonnée native.
Une donnée manquante impose la limite ; ne pas la remplacer par un ancien récit.

Ne pas reprogrammer la tâche, créer un remplacement, relancer un cycle ou envoyer
un email pour compenser une observation retardée. Un délai arbitraire ne prouve
pas la non-exécution. Définir le prochain contrôle et son budget dans le périmètre
convenu ; ne pas créer une surveillance supplémentaire sans demande du propriétaire.
Au prochain contrôle autorisé, reprendre la même identité. Les principes de
WRITE_RECOVERY.md s'appliquent aux effets incertains et aux erreurs explicites.

Une reprise autorisée exige la réconciliation préalable de l'état réel et de la
réservation ; elle garde le même operation_id et les fenêtres pending. Si une
replanification est explicitement décidée en Chat, conserver l'ancienne occurrence,
mettre à jour la même tâche native, relire et journaliser, sans perdre ses reçus.

## Preuve de mise en service et livraison

`scheduled_cycle_verified=true` exige un reçu du cycle exact, relu et validé,
attestant les lectures requises, la couverture et la persistance privée vérifiée.
Ne pas recopier un indicateur de succès d'une autre instance ou révision.
Le mode observe reste sans mutations Gmail/Calendar. Une recette réussie n'étend
pas le mandat ; la récurrence permanente exige une cadence convenue distincte.

Conserver séparément briefing sauvegardé, sortie Chat, notification configurée et
réception confirmée selon STATE.md. Le statut verified n'est pas une preuve de
notification reçue. Aucune notification native ne donne un mandat d'envoi Gmail.

## Outil de contrôle et recette

[scheduler_observation.py](../tools/scheduler_observation.py) classe des preuves
fournies sans I/O. Adapter les champs des reçus existants sans les réécrire ; chaque
flag True exige une vérification réelle. Il ne consulte aucun scheduler et toutes
ses autorisations de retry, replanification et remplacement restent false.

`python -m unittest discover -s tests -p test_scheduler_observation.py -v`

Tester absence tardive de last_run_time, reçu visible avant métadonnée, ancien reçu,
révision différente, essai interactif, couverture/relecture manquantes, BUSY et
horodatages incompatibles. Les timestamps de fixtures sont fictifs, pas un délai
garanti du produit. Aucun de ces tests locaux ne reproduit la latence plateforme.

Pour la recette réelle autorisée : un one-shot, relecture de sa configuration,
identité d'occurrence figée, contrôle des quatre horloges et revalidation des effets.
En cas d'incertitude, conserver le diagnostic sans multiplier les tâches.
L'issue #5 reste ouverte pour le suivi de la latence réelle ; ce correctif porte
sur son interprétation et l'absence de rejouement, pas sur le moteur de planification.
