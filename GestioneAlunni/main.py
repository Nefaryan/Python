import visualizzaStudente, aggiungiStudente, modificaStudente, eliminaStudente
import time

while True:
    with open ("ultimaMatricola.txt", "r") as fileL:
        matricola = int(fileL.read())

    scelta = input("Benvenuto nella Gestione degli studenti\n" \
    "Digita 1 per AGGIUNGERE uno studente\n" \
    "Digita 2 per VISUALIZZARE gli studenti con i loro voti\n" \
    "Digita 3 per MODIFICARE o ELIMINARE i voti di uno studente\n" \
    "Digita 4 per ELIMINARE uno studente con i suoi voti\n" \
    "Digita ESCI per uscire dal programma\n")

    if scelta.lower() == "esci":
        print("Arrivederci!")
        break
    elif scelta == "1":
        ultimaMatricola = aggiungiStudente.addStudent(matricola)
        with open ("ultimamatricola.txt" , "w") as fileS:
            fileS.write(str(ultimaMatricola))
        time.sleep(3)
    elif scelta == "2":
        visualizzaStudente.printStudents()
        time.sleep(3)
    elif scelta == "3":
        modificaStudente.changeVoti()
        time.sleep(3)  
    elif scelta == "4":
        eliminaStudente.deleteStudent()
        time.sleep(3) 