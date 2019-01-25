# Vendredi 11 Janvier
#def main() :
 #   print("Ceci est la fonction main.")
 #   a = 5
 #   for i in range(1, 20): #pour i dans [1;20[
 #       a = a * 7 + 13
 #   print(a)
#main()

#Suite de Syracuse
#On part d'un nombre, s'il est pair on divise par 2 
#sinon on le multiplie par 3 et on ajoute 1 et on recommence

def calcul(n) :
    i = 0
    while n != 1:
        if n % 2 == 0 :
            n = n / 2
        else :
            n = n * 3 + 1
        i = i + 1
    return i

def main() :
    a = 0
    b = 0
    for i in range(1,1001):
        s = calcul(i)
        if b <= s:    
            a = i
            b = s
            print(a,b)
main()     