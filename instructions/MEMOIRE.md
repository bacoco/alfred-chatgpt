# Mémoire privée de chaque instance

Le kit reste générique. Chaque propriétaire choisit **son propre dépôt GitHub privé**,
sa branche et son connecteur autorisé. Ne jamais utiliser celui de l'auteur par défaut.
Ne changer ni le connecteur ni ses permissions pour contourner un refus.

## Créer la structure à la première installation

[INSTALLATION.md](INSTALLATION.md) applique [le modèle privé](../templates/private/README.md)
et son manifeste versionné. Le modèle fournit les registres initiaux et les premières
instructions locales, sans données réelles. Chat remplit ensuite les choix validés.
La création de dépôts, l'écriture de fichiers et la planification sont vérifiées
séparément. Une instance existante ne reçoit pas une recopie aveugle du modèle.

## Reprendre les données

Avant toute donnée personnelle, vérifier le dépôt exact et sa visibilité privée.
Lire README.md, AGENTS.md, state/control.json et les chemins qu'il déclare.
[STATE.md](STATE.md) définit tâches, préférences, décisions et checkpoints.
L'emplacement privé reste dans le contrôle et le contexte de lancement.
Le catalogue public ne contient aucun compte ni dossier personnel.

Réutiliser les registres existants, sans reset du profil, affaires, mandats ou historique.
Les fixtures synthetic=true restent sous tests/ et sont exclues des briefings.
Les données et décisions réelles ne vont ni dans le kit public ni dans une recherche web.
Le choix du stockage n'autorise pas l'import de tous les comptes. Respecter le
mandat et les restrictions privées. Un test interactif ne prouve pas un test planifié.

Relire le SHA courant avant remplacement et vérifier après écriture. Pour un lot
cohérent : arbre basé sur le commit relu, commit enfant, mise à jour sans force,
selon STATE.md. En cas de conflit ou résultat incertain, réconcilier avant répétition.

Aucun mot de passe, token, clé privée, lien à usage unique, export brut ou pièce
très sensible dans Git. Conserver des références et résumés minimaux. L'historique
conserve les versions anciennes ; retirer un fichier ne l'efface pas de l'historique.
