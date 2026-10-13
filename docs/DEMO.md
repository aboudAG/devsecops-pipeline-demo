# Scénario De Démonstration

## Démo 1 : Faire Échouer Un Test Puis Corriger

1. Modifier temporairement `app/test_main.py`.
2. Remplacer le résultat attendu de `/add/7/5` par `13`.
3. Committer et pousser sur une branche de test.
4. Ouvrir l'onglet Actions et montrer que le job `lint-and-test` échoue.
5. Corriger le test en remettant `12`.
6. Committer et pousser.
7. Montrer que le pipeline repasse au vert.

## Démo 2 : Faire Échouer Un Scan De Sécurité Puis Corriger

1. Ajouter temporairement une dépendance vulnérable avec version fixée dans `requirements.txt`.
2. Committer et pousser sur une branche de test.
3. Ouvrir l'onglet Actions et montrer que le job `security-scans` échoue sur Trivy si la vulnérabilité correspond au seuil `HIGH` ou `CRITICAL`.
4. Remplacer la dépendance par une version corrigée ou la supprimer si elle n'est pas nécessaire à l'application.
5. Committer et pousser.
6. Montrer que le pipeline repasse au vert.

## Démo 3 : Vérifier La Publication GHCR

1. Fusionner ou pousser une modification sur `main`.
2. Ouvrir le job `build-scan-publish`.
3. Vérifier que les étapes de connexion et publication GHCR s'exécutent uniquement sur `main`.
4. Ouvrir l'onglet Packages du dépôt ou du profil GitHub.
5. Rendre le package public si tu veux l'afficher dans ton portfolio.

## Captures D'écran À Ajouter Au README

1. Vue du dépôt GitHub avec l'arborescence du projet.
2. Onglet Actions avec un pipeline réussi.
3. Détail du job `lint-and-test`.
4. Détail du job `security-scans`.
5. Détail du job `build-scan-publish`.
6. Échec volontaire d'un test.
7. Échec volontaire d'un scan Trivy.
8. Package visible dans GitHub Container Registry.
9. Workflow `deploy-kind` lancé manuellement si tu présentes le bonus Kubernetes.
