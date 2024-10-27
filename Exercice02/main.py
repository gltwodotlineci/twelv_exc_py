students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

name = input("Entrez le nom de l'étudiant : ")
if name not in  students.keys():
     print(f" L'étudiant {name} n'existe pas dans la liste.")
else:
     student = students[name]
     print(f"Notes de {name} :")
     total = 0
     for k, note in student.items():
          print(f"{k} : {note}")
          total += note

     print(f"Moyenne de {name} : {float(total)/3}")
