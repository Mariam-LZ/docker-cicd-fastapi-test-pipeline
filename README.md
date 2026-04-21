# Docker — Mise en place d’un pipeline CI/CD de tests pour API FastAPI

Projet réalisé dans le cadre de la formation **DataScientest** – module **Docker**.

## Objectif

Concevoir une chaîne de tests automatisés conteneurisée afin de valider une **API de sentiment analysis** avant déploiement.

L’objectif était de simuler un pipeline **CI/CD** capable d’exécuter plusieurs scénarios de tests sur une API FastAPI déployée dans Docker.

---

## Environnement technique

| Composant | Technologie |
|----------|-------------|
| Conteneurisation | Docker |
| Orchestration | Docker Compose |
| API testée | FastAPI |
| Langage de test | Python |
| Librairies | Requests, OS |
| Logs | Volumes Docker |

---

## API testée

Image utilisée :

```bash
datascientest/fastapi:1.0.0