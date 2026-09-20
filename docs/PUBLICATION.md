# Publication du dossier dans GitHub

## État au 20 septembre 2026

Le propriétaire a créé **`bacoco/alfred-chatgpt`**, puis l'a ajouté aux dépôts autorisés pour l'intégration GitHub. La visibilité observée est **publique** ; elle n'a pas été modifiée.

La branche `main` conserve le dossier documentaire : analyse, sources, feuille de route, instructions et historique. Aucun runtime ni scheduler n'est activé par cette publication.

Le [compte rendu d'export initial](../records/EXPORT-2026-09-20.md) reste une trace historique du blocage précédent. Il ne faut plus exécuter une commande de création de dépôt pour cette cible.

## Mettre à jour depuis ChatGPT

1. Lire le dépôt et les fichiers existants via le connecteur autorisé.
2. Vérifier que la modification relève uniquement de `bacoco/alfred-chatgpt` et ne contient pas de données privées.
3. Publier les fichiers en préservant les changements existants ; ne pas forcer une référence Git qui aurait évolué.
4. Relire la branche, le commit et les contenus ou empreintes Git attendus.
5. Conserver les résultats incertains et les réconcilier avant toute répétition.

Une permission affichée dans les métadonnées du dépôt n'est pas, à elle seule, la preuve que l'intégration peut écrire. La preuve est le résultat réel d'une écriture autorisée et sa relecture.

## Variante locale, seulement dans un environnement déjà autorisé

```bash
git clone https://github.com/bacoco/alfred-chatgpt.git
cd alfred-chatgpt
git status
# Modifier et vérifier uniquement les documents autorisés.
git diff
# Créer ensuite un commit ciblé et le pousser sans --force.
```

Ne pas placer de token dans ce dépôt ni dans une commande partagée. Ne pas remplacer l'historique distant par celui de l'ancien bundle local : les contenus ont été transférés, pas cet historique.

## Limites

La publication documentaire ne certifie ni les assertions de l'étude initiale, ni la disponibilité des connecteurs dans une tâche, ni l'exécution de fonctions de secrétariat. Revalider les sources et les capacités avant implémentation.
