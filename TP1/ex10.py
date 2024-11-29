def fusionner_dicts(dict1,dict2):
        fus= dict1.copy()
        for key, value in dict2.items():
                fus[key] =fus.get(key,0) +value
        return fus
A = {"nom":1 ,
     "prenom":2}
B = {"nom":1 ,
     "nat":3}
print(fusionner_dicts(A,B))