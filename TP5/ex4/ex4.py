import csv
with open('TP5\ex4\contacts.csv','w',newline='')as file:
    writer=csv.writer(file)
    field =["Nom","Age","Ville"]
    writer.writerow(field)
    writer.writerow(["Alice","30","Paris"])
with open('TP5\ex4\contacts.csv','r',newline='') as file:
    reader=csv.DictReader(file)
    for row in reader:
            print(f"Nom : {row['Nom']}, Age : {row['Age']}, Ville : {row['Ville']}")
print("File 'contacts.csv' created successfully!")