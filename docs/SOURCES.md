# Sources et statut des références

Date du dossier : **20 septembre 2026**.

## Comment lire ce registre

Les références ci-dessous sont les liens de l'analyse initiale, normalisés pour rester utilisables hors de ChatGPT. **Référence enregistrée ne signifie pas référence vérifiée pendant l'export.** Aucun nouvel audit web des produits ou papers n'a été réalisé lors de la sauvegarde.

Deux documents du dépôt existant ont été effectivement relus par le connecteur pendant l'export : `docs/DEPLOYMENT_STATUS.md` (S02) et `docs/FLEET_OPERATOR_RELAY.md` (S09). Une recherche a aussi retourné des extraits des guides d'installation et du script d'installation des profils. Cela ne prouve pas que les machines ou les services décrits soient actuellement disponibles.

Les prix, limites d'abonnement, disponibilités d'applications, noms de projets, dates d'archivage, versions et scores doivent être revalidés à leur source primaire avant une décision. Les tableaux de l'analyse contiennent des appréciations de pertinence, pas des résultats de tests d'ALFRED.

## Dépôts existants à réutiliser

<a id="s01"></a> **S01 — Chat-first Operations & Fleet Operator.** [README](https://github.com/bacoco/chatgpt-cost-router/blob/main/README.md). Source de l'analyse initiale ; non relue intégralement pendant cet export.

<a id="s02"></a> **S02 — Déploiement documenté.** [DEPLOYMENT_STATUS.md](https://github.com/bacoco/chatgpt-cost-router/blob/main/docs/DEPLOYMENT_STATUS.md). Relu à l'export ; blob `c8edbb22aa21941cde6ab34616cf07c69938093e`. Document du 11 septembre 2026, note du 19 septembre. Évidence historique, pas télémétrie en direct.

<a id="s03"></a> **S03 — État courant du travail A/B.** [CURRENT.md](https://github.com/bacoco/chatgpt-cost-router/blob/main/.chatgpt/CURRENT.md). Source de contexte de la conversation.

<a id="s04"></a> **S04 — Moteur d'opérations.** [chat_ops/engine.py](https://github.com/bacoco/chatgpt-cost-router/blob/main/chat_ops/engine.py). Source du constat sur idempotence, approbations exactes et états incertains dans l'analyse initiale. Relire le code à la révision retenue avant réutilisation.

<a id="s05"></a> **S05 — Catalogue d'actions.** [chat_ops/catalog.py](https://github.com/bacoco/chatgpt-cost-router/blob/main/chat_ops/catalog.py). Le comportement de confirmation rapporté par l'étude doit être vérifié avec le catalogue et ses données effectives.

<a id="s06"></a> **S06 — Architecture A/B.** [ARCHITECTURE.md](https://github.com/bacoco/chatgpt-cost-router/blob/main/docs/ARCHITECTURE.md). Principes de séparation, provenance et réconciliation.

<a id="s07"></a> **S07 — Loriq Watch Scheduler.** [README](https://github.com/bacoco/loriq-watch-scheduler/blob/main/README.md). Référence de la fabrique de veille et du runtime multiplexé.

<a id="s08"></a> **S08 — Contrats du multiplexage.** [tech_watch/multiplex.py](https://github.com/bacoco/loriq-watch-scheduler/blob/main/tech_watch/multiplex.py). Chemin cité dans l'analyse initiale ; existence, révision et contraintes `kind="watch"`, `scheduler-techno/`, jours entiers à revalider.

<a id="s09"></a> **S09 — Relais Fleet.** [FLEET_OPERATOR_RELAY.md](https://github.com/bacoco/chatgpt-cost-router/blob/main/docs/FLEET_OPERATOR_RELAY.md). Relu à l'export ; blob `fee6280676703fac8d00f1981f43b4dca18090f7`. Les recherches dans [INSTALLATION.md](https://github.com/bacoco/chatgpt-cost-router/blob/main/docs/INSTALLATION.md) et [ab_host_install.py](https://github.com/bacoco/chatgpt-cost-router/blob/main/scripts/ab_host_install.py) indiquent les profils initiaux `smoke` et `validate-release` ; aucun profil de création de dépôt n'a été identifié.

## Documentation OpenAI — capacités à revalider par compte et surface

<a id="s10"></a> **S10 — Tâches dans ChatGPT.** [Aide officielle](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt). Référence enregistrée depuis l'analyse initiale ; pas de validation actuelle du support des applications, de la cadence ou de l'accès aux fichiers. Un test réel du scheduler reste nécessaire.

<a id="s11"></a> **S11 — Applications/connecteurs dans ChatGPT.** [Aide officielle](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt). Vérifier droits, écritures, approbations, disponibilité et politique de données du plan et de chaque application.

<a id="s12"></a> **S12 — Présentation de Pulse.** [Introducing ChatGPT Pulse](https://openai.com/index/introducing-chatgpt-pulse/). Référence produit, pas preuve de disponibilité sur le compte ni d'exécution de secrétariat.

## Projets et produits

<a id="s13"></a> **S13 — Karpathy, LLM Wiki.** [Gist cité](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). Pattern documentaire évoqué par l'analyse ; ni application autonome ni contrôle de permissions.

<a id="s14"></a> **S14 — LifeOS / PAI.** [Dépôt indiqué dans l'analyse](https://github.com/danielmiessler/LifeOS). Le nom du projet, la filiation à PAI et l'environnement Claude Code/Bun restent à confirmer ; ne pas traiter un renommage allégué comme un fait certifié.

<a id="s15"></a> **S15 — Basic Memory.** [Dépôt](https://github.com/basicmachines-co/basic-memory). Candidat à la mémoire documentaire.

<a id="s16"></a> **S16 — Intégration ChatGPT de Basic Memory.** [Documentation indiquée](https://docs.basicmemory.com/integrations/chatgpt/). Documentation fournisseur à distinguer d'une application installée et utilisable en tâche.

<a id="s17"></a> **S17 — Khoj.** [Dépôt](https://github.com/khoj-ai/khoj). Référence de second cerveau et assistant auto-hébergeable.

<a id="s18"></a> **S18 — Graphiti.** [Dépôt](https://github.com/getzep/graphiti). Distinguer le logiciel, les services Zep et les coûts de leurs dépendances.

<a id="s19"></a> **S19 — Mem0.** [Dépôt](https://github.com/mem0ai/mem0). Vérifier la version libre, les fonctions hébergées, les modèles requis et le protocole exact des chiffres annoncés.

<a id="s20"></a> **S20 — Letta / MemGPT.** [Dépôt cité](https://github.com/letta-ai/letta). Le renvoi allégué vers Letta Code et l'archivage du serveur V1 ne sont pas revérifiés ici.

<a id="s21"></a> **S21 — Second Me.** [Dépôt](https://github.com/mindverse/Second-Me). Personnalisation et double numérique ; maturité et exigences techniques à vérifier.

<a id="s22"></a> **S22 — OpenClaw.** [Dépôt](https://github.com/openclaw/openclaw). Référence d'assistant généraliste ; vérifier les limites de sandbox et les droits des outils dans la version choisie.

<a id="s23"></a> **S23 — Hermes Agent.** [Dépôt](https://github.com/NousResearch/hermes-agent). Capitalisation d'expérience, compétences et runtime distinct de ChatGPT.

<a id="s24"></a> **S24 — Inbox Zero.** [Dépôt](https://github.com/elie222/inbox-zero). Workflows de correspondance à examiner avant réimplémentation.

<a id="s25"></a> **S25 — LangChain Agents from Scratch.** [Dépôt](https://github.com/langchain-ai/agents-from-scratch). Référence pédagogique.

<a id="s26"></a> **S26 — Executive AI Assistant.** Projet mentionné dans l'analyse, mais **aucune URL canonique propre n'était individualisée dans la référence donnée**. Retrouver le dépôt exact et vérifier l'assertion d'archivage au 27 juillet 2026 avant de la réutiliser. Ne pas inventer une adresse pour compléter la bibliographie.

<a id="s27"></a> **S27 — Lindy.** [Site fournisseur](https://www.lindy.ai/). Le montant de 29,99 $ et le forfait de 3 000 crédits viennent de l'analyse initiale ; non revalidés à l'export, ne constituent pas un devis ni un prix garanti.

<a id="s28"></a> **S28 — Fyxer.** [Site fournisseur](https://www.fyxer.com/). Référence commerciale et ergonomique, non testée ici.

<a id="s29"></a> **S29 — Wallos.** [Dépôt](https://github.com/ellite/Wallos). Deux marqueurs de citation défectueux de l'analyse ont été remplacés par cette référence au dépôt nommé. Vérifier API et fonctions IA avant de les retenir.

<a id="s30"></a> **S30 — Paperless-ngx.** [Dépôt](https://github.com/paperless-ngx/paperless-ngx). Gestion documentaire envisagée comme brique, pas comme décideur.

<a id="s31"></a> **S31 — Actual Budget.** [Dépôt](https://github.com/actualbudget/actual). Budget et rapprochements financiers facultatifs.

<a id="s32"></a> **S32 — n8n.** [Dépôt](https://github.com/n8n-io/n8n). Vérifier la licence applicable aux composants et à l'usage retenus.

<a id="s33"></a> **S33 — Activepieces.** [Point d'entrée du dépôt nommé](https://github.com/activepieces/activepieces). Mentionné avec n8n dans l'étude, sans audit distinct ; ne pas lui attribuer automatiquement toutes les caractéristiques de n8n.

## Papers et benchmarks

<a id="s34"></a> **S34 — Proactive Agent.** [arXiv:2410.12361](https://arxiv.org/abs/2410.12361). Anticipation des besoins et contrôle des interventions.

<a id="s35"></a> **S35 — LongMemEval.** [arXiv:2410.10813](https://arxiv.org/abs/2410.10813). Mémoire à long terme, temporalité, mise à jour et abstention.

<a id="s36"></a> **S36 — LongMemEval-V2 / AgentRunbook, attribution de l'analyse.** [arXiv:2605.12493](https://arxiv.org/abs/2605.12493), [version HTML citée](https://arxiv.org/html/2605.12493). Vérifier titre, version, date, protocole, score de 72,5 % et latence : ces éléments sont conservés depuis l'analyse, pas certifiés par la sauvegarde.

<a id="s37"></a> **S37 — PersonaMem-v3.** [Dépôt indiqué](https://github.com/bowen-upenn/PersonaMem-v3). Vérifier existence, version, méthodologie, provenance des données et conclusions avant incorporation aux tests.

<a id="s38"></a> **S38 — Zep: A Temporal Knowledge Graph Architecture for Agent Memory.** [arXiv:2501.13956](https://arxiv.org/abs/2501.13956). Mémoire temporelle et relations.

<a id="s39"></a> **S39 — MemGPT.** [arXiv:2310.08560](https://arxiv.org/abs/2310.08560). Hiérarchie de mémoire ; pas une démonstration de fiabilité administrative.

<a id="s40"></a> **S40 — AssistantBench.** [arXiv:2407.15711](https://arxiv.org/abs/2407.15711). Évaluation de tâches web ; ne pas reporter des résultats historiques sur les modèles actuels.

<a id="s41"></a> **S41 — AgentDojo.** [arXiv:2406.13352](https://arxiv.org/abs/2406.13352). Attaques par injection et défenses dans des environnements agentiques.

<a id="s42"></a> **S42 — CaMeL: Defeating Prompt Injections by Design.** [arXiv:2503.18813](https://arxiv.org/abs/2503.18813), [HTML v2 citée](https://arxiv.org/html/2503.18813v2). Séparation de confiance et politiques ; ne pas revendiquer les garanties de cette architecture sans l'implémenter et la tester.

## Règle pour la suite

Avant adoption d'un projet ou citation d'un résultat, consigner date de consultation, URL, version ou commit, nature de la preuve et éventuelles limites. Séparer déclarations du fournisseur, résultats indépendants, tests réalisés et choix d'architecture. Un lien absent ou une source non vérifiée reste visible au lieu d'être inventé.
