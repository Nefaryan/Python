def deleteStudent():
    print("Sei nella modalità di Eliminazione di uno Studente!")
    with open("Studenti.txt", "r") as fileL:
        studenti = fileL.readlines()
    
    matricola_input = input("Inserire matricola dello studente da modificare: ")
    flag = False
    while flag == False:
        for i in range(len(studenti)):
            riga = studenti[i].replace('\n', '')
            parti = riga.split()
            if parti[0] == matricola_input:
                print("Studente trovato:", riga)
                nuova_riga = ""
                studenti[i] = nuova_riga
                print(f"Studente eliminato\n")
                flag =  True
                break
        if flag == False:
            matricola_input = input("Matricola non trovata. RIPROVA: ")
    
    if flag:
        with open("Studenti.txt", "w") as fileL:
           fileL.writelines(studenti)
        print("Eliminazione completata.")
