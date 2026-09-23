# Reprise d'écriture partielle ou incertaine

Complément obligatoire de STATE.md lors d'une installation partielle ou d'une
écriture dont le résultat n'est pas certain. Référence :
[issue #2](https://github.com/bacoco/alfred-chatgpt/issues/2).
Les journaux restent dans les registres privés existants ; aucun deuxième moteur.

## Distinguer l'erreur avant la reprise

Un refus de sécurité, de permission ou d'approbation exige l'arrêt des écritures
concernées. Ne pas reformuler le contenu, changer son encodage, son chemin, son
compte ou son connecteur pour franchir le contrôle. Une absence de fichier prouvée
n'annule pas un refus de sécurité. Conserver l'erreur exacte sans secret.
La reprise requiert la résolution autorisée du blocage, pas une supposition de bug.

Un refus lié à la conversation suit LANCEMENT.md : proposer, en Chat interactif,
une branche Chat avec le même connecteur et compte, puis une lecture minimale,
sans changer les permissions ni garantir le rétablissement. Ne pas ouvrir ou
simuler une autre conversation depuis une tâche planifiée.

Un timeout ou une réponse perdue laisse l'effet UNCERTAIN. Une opération peut avoir
réussi malgré la réponse absente ; vérifier avant de reprendre, jamais réémettre
simplement parce que le délai est dépassé.

## Réconcilier depuis les preuves actuelles

1. Relire identité, dépôt privé, mandat et arrêt ; conserver le même operation_id.
2. Relire le journal, le commit attendu et chacun des fichiers concernés.
3. Comparer les octets à la version attendue figée avant la première écriture :
   - identiques : déjà appliqué, relire et enregistrer la preuve, aucune réécriture ;
   - absence réellement vérifiée : candidat à une création, pas une autorisation ;
   - contenu différent : CONFLICT, préserver et demander l'arbitrage nécessaire ;
   - lecture impossible, digest manquant ou 404 ambigu : UNCERTAIN, ne rien écrire.
4. Recontrôler autorisation et réservation avant toute action. Si le refus explicite
   subsiste, rester BLOCKED même lorsque le fichier manque.
5. Pour un incident de transport résolu avec absence prouvée et autorisation valide,
   au plus une tentative ciblée sur les seuls manques ; création conditionnelle,
   sans force, puis relecture. Un nouvel échec termine ce passage, sans boucle.

Le planificateur local facultatif [write_recovery.py](../tools/write_recovery.py)
compare des empreintes fournies. Il ne lit aucun compte, n'écrit rien et ne peut
lever un blocage : ses entrées doivent venir de vraies lectures autorisées.
`automatic_retry=false` reste systématique. Aucun résultat local ne prouve un
rétablissement du connecteur.

## Installation interrompue

Conserver le SHA du kit, installation_id et les cinq paramètres de rendu initiaux,
y compris rendered_at. Ne pas régénérer une date différente à chaque tentative.
Comparer au manifeste de cette installation, pas à un nouveau kit téléchargé.
Si les paramètres initiaux ne sont plus connus, arrêter et réconcilier ; pas de reset.
Un fichier personnalisé n'est pas un fichier manquant : le préserver.

Garder state/setup.json en `partial_scaffold_blocked` tant que tous les fichiers
requis n'ont pas été écrits et relus. La liste de manques, conflits et inconnues,
les empreintes attendues/observées et l'erreur vont dans records/INSTALLATION-<id>.json.
Si ce journal est lui-même inaccessible, rendre le diagnostic dans Chat sans
prétendre l'avoir persisté. Ne pas créer un second dépôt ou une tâche de secours.
`storage_readback_verified=true` exige la relecture de l'ensemble. Aucune activation
métier ou planifiée ne découle d'un scaffold partiel.

## Checkpoint interrompu après un reçu

Relire le reçu exact, sa couverture, les objets persistés et le checkpoint.
Un reçu incomplet n'autorise jamais l'avance de completed_through_utc.
Reprendre la même pending_window avant toute nouvelle fenêtre. Un reçu complet
revalidé peut justifier la seule transition manquante du checkpoint, sous contrôle
courant et écriture conditionnelle ; jamais une recollecte ou un second envoi aveugle.

## Recette synthétique

Exécuter `python -m unittest discover -s tests -p test_write_recovery.py -v`.
Vérifier succès perdu, absence prouvée, lecture inconnue, contenu concurrent,
installation partielle, révocation et refus de sécurité persistant.
Ces tests prouvent le plan de décision sans effets ; ils ne reproduisent ni ne
corrigent la cause plateforme du refus historique. L'issue #2 reste ouverte pour
cette cause et sa reproductibilité, même après intégration de cette reprise.
