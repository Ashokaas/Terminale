import rectangle as r
import math

rectangle_1 = r.Rectangle(largeur=10, hauteur=10)
assert rectangle_1.calculer_aire() == 100, 'aire fausse'
assert rectangle_1.get_largeur() == 10, "largeur fausse"
assert rectangle_1.calculer_ratio() == 1, "ratio faux"
assert rectangle_1.calculer_perimetre() == 40, "perimètre faux"
assert round(rectangle_1.calculer_diagonale(), 1) == round(math.sqrt(200), 1), "perimètre faux"

a = 1
for _ in range(10):
    a -= 0.1
    a = round(a, 1)
    print(a) 