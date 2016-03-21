# -*- coding: utf-8 -*-

# module maths
import math

# boucle de variation de la charge
for p in range(1, 80+1):
    
    # boucle de variation de la capacite
    for c in range(p, p*2+1):
        
        # calcul du numerateur
        numerateur = pow(p, c) * 1.0 / math.factorial(c)
        
        # calcul du denominateur
        denominateur = 0
        for i in range(0, c):
            denominateur += pow(p, i) * 1.0 / math.factorial(i)
            
        # ecriture des resultats sur la sortie standarde
        print(str(c) + " " + str(p) + " " + str(numerateur / denominateur))
