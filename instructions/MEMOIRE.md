# Mémoire privée — décision du propriétaire

Le 20 septembre 2026, le propriétaire a choisi un **dépôt GitHub privé distinct**
comme mémoire persistante. Le dépôt public `alfred-chatgpt` conserve uniquement le
kit. Cette décision remplace les consignes historiques excluant tout usage de Git
pour la mémoire ; les secrets et exports bruts restent exclus de tous les dépôts.

Dans le contexte personnel autorisé, la cible choisie est `bacoco/alfred-private`,
branche `main`, via **GitHub — chatgpt**. Le nom est une configuration de connexion,
pas un droit d'accès. Vérifier la visibilité privée et le compte avant les données.
Si cette vérification échoue, signaler le blocage sans substituer de stockage.

Lire le README privé, ses règles et `state/control.json` avant les dossiers.
Les registres `state/cases.json`, `state/subscriptions.json` et
`memory/profile.json` sont initialement vides. Les données de test sous
`tests/fixtures/` ne sont jamais des affaires ni des préférences réelles.
Les journaux et contenus privés restent exclusivement dans le dépôt privé.

Toute modification d'un fichier existant exige une lecture de son SHA courant,
une écriture conditionnelle et une vérification après écriture. Une réponse perdue
est à réconcilier. Le premier test séquentiel ne prouve pas la concurrence sûre.

Le choix et l'initialisation du stockage n'autorisent pas l'import de mails,
l'activation des tâches, les brouillons Gmail ni les envois. Une entrée de contrôle
ne remplace jamais un mandat. Les horaires et permissions restent inchangés.

Les résultats du test sont consignés dans le dépôt privé. La reprise effective
dans une nouvelle conversation et l'exécution planifiée demandent encore un test
sur chacune de ces surfaces. Aucun nouveau moteur ou service d'agent n'est installé.
