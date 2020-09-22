status : [![CircleCI](https://circleci.com/gh/jean-charles-gibier/PurBeurre.svg?style=shield)](https://app.circleci.com/pipelines/github/jean-charles-gibier/PurBeurre)

# PurBeurre
Projet 8 DaPy

 La société "Pur beurre" souhaite un site dont les exigences sont décrites dans 
 [le document suivant :](https://openclassrooms.com/fr/paths/68/projects/159/assignment)


installation:
Git clone de ce projet + tests + migrations 

````
pip install -r requirements.txt
export SECRET_KEY=`python -c 'import random, string; print("".join([random.choice(string.printable) for _ in range(24)]))'`
export CODECOV_TOKEN=9db8d8a5-bd6d-40c2-a691-fc5d1b830f21
# pour purger la base
python ./manage.py purge
# pour alimenter la base 
python ./manage.py filler 4000
````

Admin local :<br>
    127.0.0.1:8000/user/admin/