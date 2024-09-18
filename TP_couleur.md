# TP Couleur

Vous devez traiter au moins jusqu’à la question 12, l’ensemble des comptes rendus est à rendre pour une semaine après le dernier TP. Le travail est à effectuer en binôme. Une séance plus un peu de temps en plus doit suffire. 
Le travail est à faire en autonomie par binôme. Le but est de s’habituer à travailler en consultant des ressources pertinentes sur internet en cas de besoin. L'usage de chaptèGPT est permis par contre, vous devrez fournir votre prompt de session (lien url fourni par chat-gpt par exemple). Il est fortement conseillé de ne pas copier/coller les codes mais de les retaper pour laisser à cvotre cerveau le temps de les assimiler

## Objectif

On s’intéresse au tracking par un drone volant d'une boule de couleur, c'est-à-dire aux technologies permettant le comportement suivant :  
[Vidéo du comportement](https://www.youtube.com/watch?v=_3697dtyOz4)

Le fichier [balls_tracker.py](couleur/balls_tracker.py)
contient un exemple de code ( associé à un ensemble de vidéos.)

## Question 1
Tester ce code avec Python (V3):

```bash
python balls_tracker.py
```
(Comme vous pouvez le constater, par défaut le code  utilise la vidéo ball.mp4 comme source d'entrée).
Quelle est votre conclusion sur le but de ce code ?

## Question 2

Proposez un code qui permet de choisir la couleur considérée parmi les 4 suivantes (bleu, rose, jaune ou vert)

<img src="img/4_balles.jpg" height="300">

Vous pourrez vous inspirer des documents suivants :

[Lien 1](https://docs.opencv.org/3.2.0/df/d9d/tutorial_py_colorspaces.html)

[Lien 2](https://stackoverflow.com/questions/10948589/choosing-correct-hsv-values-for-opencv-thresholding-with-inranges)

[Lien 3](https://www.learnopencv.com/color-spaces-in-opencv-cpp-python/)

Je vous propose aussi de regarder la vidéo suivante sur la représentation des couleurs 

[<img src="https://img.youtube.com/vi/CF4wuPLBaAA/hqdefault.jpg" width="600" height="300"
/>](https://www.youtube.com/embed/CF4wuPLBaAA?autoplay=1)

Tester ce code sur la vidéo ball3.mp4 et faites une copie d'écran pour chaque couleur correctement traquée . Joindre le code dans le rapport.


### Question 3

Le code fourni (ou plus précisément sa version originale [ici](https://github.com/fabricejumel/OpenCV-Python-Hacks/blob/master/greenball_tracker.py)) peut être utilisé pour le contrôle d'un drône.  
Cela est fait dans le projet suivant :  
https://github.com/fabricejumel/ARDroneAutoPylot  
et plus précisément dans le code suivant :  

https://github.com/fabricejumel/ARDroneAutoPylot/blob/master/opencv/autopylot_agent.py  

Expliquer ce code (avec le plus de détail possible (`autopylot_agent.py`)) et le lien avec le `greenball_tracker.py`.  
Quelle est le comportement ? Comment est gérée la « distance » à l'objet traqué ?

### Question 4
Quelle serait le comportement du drône si 2 boules de mêmes couleurs sont déplacées devant lui ?  
Ce comportement ne semble pas pertinent, pourquoi ?

Le code suivant :  
https://github.com/JJLewis/ColorTracking-ARDrone2.0-Python/blob/master/Code/track.py  
Donne à priori une solution à ce problème ?  
Essayer d'expliquer comment.

### Question 5
Proposer une modification du code `greenball_tracker` (en vous inspirant ou pas du code précédent) qui donne un comportement équivalent. Tester ce code si possible sur `ball2.mp4`.

### Question 6
Faites fonctionner votre code précédent en prenant en compte la couleur rose sur la vidéo `ball4.mp4`.

### Question 8
A priori votre code passe d'une boule à l'autre, comment est-il possible de rester toujours sur la même ?  
Si ce n’est pas le cas ou si la vidéo proposée ne permet pas de tester, créer votre propre vidéo pour mettre en évidence le problème (Utiliser l’outil `cheese` sous Linux et une caméra pour cela).

### Question 9
Proposer un code qui résout ce problème. *(Question difficile)*

### Question 10
Mettez en place un code permettant l’apprentissage de la couleur d’un objet se trouvant au milieu de l’image.

### Question 11
En considérant que l’on connait la taille de la balle, proposer un code qui cherche à calculer la position de la balle dans un repère cartésien ou sphérique centré sur la caméra. Proposer une procédure d’étalonnage.

### Question 12 (Bonus)
Si on fait l’hypothèse que l’objet est une balle (ronde), montrer comment on peut prendre en compte l’information et reconstituer le cercle de contour de cette balle.
