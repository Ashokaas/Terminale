def factorielle(n:int):
    if n == 1:
        return 1
    else:
        return n * factorielle(n-1)
    

def nombre_de_chiffres(n:int):
    if n < 10: 
        return 1
    else:
        return 1 + nombre_de_chiffres(n // 10)
    
    
def nombre_de_bits_1(n:int):
    if n == 0:
        return 0
    else:
        return n % 2 + nombre_de_bits_1(n // 2)
    
    
def appartient(v:int or float, l:list, i:int):
    if l[i] == v:
        return True
    elif l[i] == l[-1]:
        return False
    else:
        return appartient(v, l, i+1)

#print(appartient(46, [12, 68, 36, 45, 75], 2))

global x
x = 0
def hanoi(n:int, td:int, ta:int):
    global x
    x += 1
    if n == 1:
        print(f"Déplacement du disque {n} de la tour {td} à la tour {ta}")
    else:
        hanoi(n-1, td, 6-td-ta)
        print(f"Déplacement du disque {n} de la tour {td} à la tour {ta}")
        hanoi(n-1, 6-td-ta, ta)
        
hanoi(8, 1, 3)
print(x)

def coeff_bino(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return coeff_bino(n-1, k-1) + coeff_bino(n-1, k)
    
#print(coeff_bino(10, 2))

def pascal(n):
    pasc = [[1]]
    for e in range(1, n):
        k = [1]
        for i in range(1, e):
            k.append(pasc[e-1][i] + pasc[e-1][i-1])
        k.append(1)
        pasc.append(k)
    return pasc

#print(pascal(4))

import turtle
def flocon_koch(n, l):
    if n == 0:
        turtle.forward(l)
    else:
        flocon_koch(n-1, l/3)
        turtle.left(60)
        flocon_koch(n-1, l/3)
        turtle.right(120)
        flocon_koch(n-1, l/3)
        turtle.left(60)
        flocon_koch(n-1, l/3)
        
for i in range(3):
    flocon_koch(2, 300)
    turtle.right(120)
        
turtle.done()
    