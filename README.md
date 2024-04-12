READ ME tp1 ALVAREZ MATTIAS

Création du wrapper :

Pour tester le code ainsi que l'API :
set LAT=31.2504 
set LONG=-99.2506
set API_KEY=31220f0006c68573ef6356f764a483a9


pour executer le code :
python tp1devopps.py


Résultats: 
C:\Users\matti\OneDrive\Documents\20220499>python tp1devopps.py
Météo actuelle:
Température: 18.45 °C
Conditions météorologiques: mist


Création de l'image Docker :
docker build -t weatherapp .

Pour tester le code avec l'image : 
docker run --env LAT="31.2504" --env LONG="-99.2506" --env API_KEY=31220f0006c68573ef6356f764a483a9 weatherapp

Push de l'image sur DockerHub :
docker tag weatherapp mattias937/20220499
==> puis appuyer sur "push to hub"

Pour récupérer l'image : 
docker pull weatherapp mattias937/20220499


Bonus :

0 CVE (trivy) trivy image maregistry/api:1.0.0
0 lint errors on Dockerfile (hadolint) docker run --rm -i hadolint/hadolint < Dockerfile
Aucune données sensibles stockées dans l'image (i.e: openweather API key


Sur windows : 
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy image weatherapp
docker run --rm -i hadolint/hadolint < Dockerfile

J'ai ensuite commit mon code sur GitHub 

Fin ReadMe


Readmetp2
Ce projet vise à configurer un workflow GitHub Actions pour transformer un wrapper Python en une API Flask, construire automatiquement une image Docker et la publier sur Docker Hub à chaque push sur GitHub.

J'ai premièrement configuré un workflow GitHub Action pour automatiser la construction et la publication d'une image Docker.
J'ai créé un docker-build.yaml pour mettre à jour l'image docker dès qu'on push sur github.
J'ai modifié les settings sur git hub pour y ajouter mes ID et password Dockerhub.


Test de l'API, dans un cmd : 
docker run -p 8081:8081 --env API_KEY=190cfca07aff8b6a629657b083d72998 mattias937/20220499

Et dans un autre cmd :
curl "http://localhost:8081/?lat=5.902785&lon=102.754175"

ce qui renvoie : 
{"description":"overcast clouds","temperature":29.26}

J'ai ensuite fait le bonus en ajoutant hadolint au workflow github.

Fin read me tp2.





























