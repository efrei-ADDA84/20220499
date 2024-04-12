READ ME

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


J'ai ensuite commit mon code sur GitHub 

Fin ReadMe