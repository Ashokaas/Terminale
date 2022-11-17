def delta(liste:list):
    liste_a_retourner = [liste[0]]
    for val in range(1, len(liste)):
        val_temp = liste[val] - liste[val-1]
        liste_a_retourner.append(val_temp)
    return liste_a_retourner

print(delta([1000, 80, 80, 100]))