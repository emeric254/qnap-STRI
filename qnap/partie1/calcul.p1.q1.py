import math

for c in range(1,50+1):
    for p in range(1,70+1):
        numerateur = pow(p,c) * 1.0 / math.factorial(c)
        denominateur = 0
        for i in range(0,c):
            denominateur += pow(p,i) * 1.0 / math.factorial(i)
        #~ print(numerateur)
        #~ print(denominateur)
        print( str(c) + " " + str(p) + " " + str(numerateur / denominateur))
