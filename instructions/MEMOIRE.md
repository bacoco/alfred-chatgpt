# Mémoire privée de chaque instance

Le kit public reste générique. Chaque propriétaire choisit **son propre dépôt
GitHub privé**, sa branche et son connecteur déjà autorisé. Ne jamais reprendre
le dépôt personnel de l'auteur comme valeur implicite d'une nouvelle installation.
Ne changer ni le connecteur ni ses permissions pour contourner un refus.

Avant toute donnée personnelle, vérifier le dépôt exact et sa visibilité privée.
Lire README.md, AGENTS.md et state/control.json. Les instances de tâches,
préférences, décisions et checkpoints sont définis par [STATE.md](STATE.md).
Leur emplacement doit être conservé dans le contrôle privé et le contexte de
lancement. Le catalogue public ne doit contenir ni comptes ni dossiers personnels.

Réutiliser les registres existants. Une reprise de conversation ne réinitialise
ni affaires, ni profil, ni autorisations, ni historique. tests/fixtures/ reste
strictement synthétique et exclu des briefings. Les données et décisions réelles
ne vont jamais dans le kit public, ses issues, ses tests ou une recherche web.

Le choix du stockage ne vaut pas autorisation d'importer tous les comptes.
Respecter le mandat courant : une restriction privée peut arrêter les lectures
ou les écritures. Tester chaque capacité dans la surface réellement utilisée.
Une preuve en Chat interactif ne prouve pas l'exécution planifiée.

Relire le SHA courant avant remplacement et vérifier le contenu après écriture.
Pour les changements cohérents multi-fichiers, appliquer le commit dérivé de la
base relue et la mise à jour sans force décrits dans STATE.md. En cas de conflit
ou de résultat incertain, réconcilier au lieu de réécrire aveuglément.

Ce stockage n'est pas un coffre de secrets. Aucun mot de passe, token, clé privée,
lien de confirmation à usage unique, export brut ou pièce très sensible dans Git.
Conserver des références et résumés minimaux. L'historique Git conserve les versions
anciennes ; retirer un fichier de main n'efface pas cet historique.
