# 1. random számok generálása

import random

Ltalaj = []

for i in range(0, 20):
      Ltalaj.append(random.randint(0, 9))

print(Ltalaj)

# 2. legmagasabb pont

maxMagassag=0
for magassag in Ltalaj:
    if(maxMagassag<magassag):
        maxMagassag=magassag

print(maxMagassag)

#3. legalacsonyabb szárazföld

minMagassag=9
for magassag in Ltalaj:
    if(magassag!=0):
        if(minMagassag>magassag):
            minMagassag=magassag

print(maxMagassag-minMagassag)

#4. melyik több

vizDb=0
for magassag in Ltalaj:
    if(magassag==0):
        vizDb +=1

if(vizDb>10):
    print("Vízből van több")    
elif (vizDb==10):
    print("egyenlő számú víz és sziget van")
else:
    print("szárazföldből van több")





