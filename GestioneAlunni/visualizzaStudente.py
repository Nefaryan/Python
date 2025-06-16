def printStudents():
    with open ("Studenti.txt", "r") as fileL:
        contenutoFile = fileL.read()
    
    print("Sei nella modalità di Visualizzazione degli studenti\nElenco degli studenti con i loro voti:")
    print(contenutoFile)