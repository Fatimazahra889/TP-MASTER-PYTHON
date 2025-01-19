import json
dict={"etudiant1": {
        "nom": "Alice",
        "age": 20,
        "ville": "LA"
    },
    "etudiant2": {
        "nom": "Bob",
        "age": 22,
        "ville": "NY"
    },
    "etudiant3": {
        "nom": "Charlie",
        "age": 21,
        "ville": "SA"
    }}
with open('TP5\ex5\etudiants.json','w') as file:
    json.dump(dict,file, indent=4)
with open('TP5\ex5\etudiants.json','r')as file:
    data=json.load(file)
    for key, student in data.items():
        print(f"{key}: Nom - {student['nom']}, Âge - {student['age']}, Ville - {student['ville']}")
