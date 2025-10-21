# ProjetPacNam

Pour commencer, exécutez la commande `./setup.sh` qui permetera d'installer l'environement

Vous avez les fichiers `pacnam.py` et `ghost.py` a compléter.

## Le fichier `pacnam.py`

Vous avez les atttributs suivant a votre disposition : 

- **self.size**         (Taille en pixel d'une case de la grille)

- **self.speed**        (Vitesse du PacNam)

- **self.life**         (Points de vie du PacNam)

- **self.dt**           (Le delta de temps, pour adapté le mouvement à la fréquence d'image (vous n'avez pas a le modifier))

- **self.pos.\***       (Position x (self.pos.x) et y (self.pos.y) du PacNam sur la grille)

- **self.start_pos**    (Position de départ du PacNam (utile pour le mettre a sa position de départ))

- **self.score**        (Score du PacNam)

- **self.power_up**     (Vous dis si PacNam a sont power_up (True) ou pas (False))

- **self.timer**        (Durée de recupération du power-up)

- **self.make.maze**    (Un tableau a deux dimention (une liste de liste) qui représente les murs (1) et les espaces ou PacNam peux aller (0))

**Note** : Pour accéder à une case en particulié, vous pouvez faire self.maze.maze[ligne][colonnes]

- **self.maze.points**  (Même structure que précédement, mais qui représente les points (1) les power-ups (2) et les espaces vides (ni points ni power-up) (0))

Dans ce fichier, vosu decrais faire les méthodes : 

- **move_\*()**         (Permet au PacMan de bouger à gauche/droite/haut/bas dans le labirythe, en testant s'il vas pas dans un mur. Vous devez modifier les variables `self.pos.x` et `self.pos.y`. *Vous devrez utilisé self.dt dans cette fonction en la multipliant par la vitesse du PacNam*)

- **kill()**            (PacNam c'est fait touché ! Vous devez lui enlever une vie et le remettre a sa position de départ)

- **eat()**             (Permet a PacNam de manger les points et incrémenté son score et mettre a jour son power_up)

- **power()**           (Permet a PacNam de gardé son power_up pendant 10 secondes. (self.timer sera utilisé ici)

## Le fichier `maze.py`

Il manque la méthode **check_end()** qui renvois `False` si tous les points ont été mangé par PacNam (ou sinon `True`)

## Le Fichier `ghost.py`

*Les attributs `self.size`, `self.maze.maze`, `self.maze.points` et `self.dt` représente la même chose que dans `pacnam.py`*



