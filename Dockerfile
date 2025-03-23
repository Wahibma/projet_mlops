# Utilisation d'une image Python légère
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier requirements.txt en premier pour optimiser le cache
COPY requirements.txt /app/

# Installer les dépendances AVANT de copier tout le projet
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Maintenant, copier le reste des fichiers du projet
COPY . /app/

# Définir la commande d'exécution
CMD ["python", "app.py"]  