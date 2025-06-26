import mysql.connector

# Connessione al database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin"
)
cursor = mydb.cursor()

# Creazione database e tabella
cursor.execute("CREATE DATABASE IF NOT EXISTS SchoolDB")
cursor.execute("USE SchoolDB")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Registro (
        AlunnoID INT AUTO_INCREMENT PRIMARY KEY,
        Nome VARCHAR(50) NOT NULL,
        Voto_Ita FLOAT CHECK (Voto_Ita BETWEEN 0 AND 10),
        Voto_Math FLOAT CHECK (Voto_Math BETWEEN 0 AND 10)
    )
""")

# Funzione generica per insert/update/delete
def InsertUpdateDelete(tipo, val):
    if tipo == 1:
        sql = "INSERT INTO Registro (Nome, Voto_Ita, Voto_Math) VALUES (%s, %s, %s)"
    elif tipo == 2:
        sql = "UPDATE Registro SET Nome = %s, Voto_Ita = %s, Voto_Math = %s WHERE AlunnoID = %s"
    elif tipo == 3:
        sql = "DELETE FROM Registro WHERE AlunnoID = %s"
    cursor.execute(sql, val)
    mydb.commit()
    print( "Modifiche effettuate.\n")

# Visualizza tutti gli studenti
def SelectValues():
    cursor.execute("SELECT * FROM Registro")
    risultati = cursor.fetchall()
    if risultati:
        print("\nElenco studenti:")
        for r in risultati:
            print(r)
    else:
        print("Nessun alunno presente nel registro.\n")
    return risultati

# Visualizza medie
def SelectValuesAVG():
    cursor.execute("SELECT Nome, ROUND((Voto_Ita + Voto_Math)/2, 2) AS Media FROM Registro")
    risultati = cursor.fetchall()
    if risultati:
        print("\n Medie degli studenti:")
        for nome, media in risultati:
            print(f"{nome}: {media}")
    else:
        print("Nessun dato disponibile per calcolare medie.\n")

# Funzione per input voti con validazione
def get_valid_vote(materia):
    while True:
        try:
            voto = float(input(f"Inserisci voto {materia} (0-10): "))
            if 0 <= voto <= 10:
                return voto
            else:
                print("Il voto deve essere tra 0 e 10.")
        except ValueError:
            print("Inserisci un numero valido.")

# Loop menu principale
while True:
    try:
        opzione = int(input(
            "\nMenu Gestionale Scolastico:\n"
            "1 - Inserisci alunno\n"
            "2 - Modifica alunno\n"
            "3 - Elimina alunno\n"
            "4 - Visualizza alunni con medie\n"
            "5 - Esci\n"
            "Scelta: "
        ))

        if opzione == 1:
            nome = input("Inserisci nome alunno: ").strip()
            if not nome:
                print("Il nome non può essere vuoto.")
                continue
            voto_ita = get_valid_vote("Italiano")
            voto_math = get_valid_vote("Matematica")
            InsertUpdateDelete(1, (nome, voto_ita, voto_math))

        elif opzione == 2:
            result = SelectValues()
            if not result:
                continue
            idAlunno = input("Inserisci ID dell'alunno da modificare: ").strip()
            if not idAlunno.isdigit():
                print("ID non valido.")
                continue
            nome = input("Nuovo nome alunno: ").strip()
            if not nome:
                print("Il nome non può essere vuoto.")
                continue
            voto_ita = get_valid_vote("Italiano")
            voto_math = get_valid_vote("Matematica")
            InsertUpdateDelete(2, (nome, voto_ita, voto_math, idAlunno))

        elif opzione == 3:
            result = SelectValues()
            if not result:
                continue
            idAlunno = input("Inserisci ID dell'alunno da eliminare: ").strip()
            if not idAlunno.isdigit():
                print("⚠️  ID non valido.")
                continue
            InsertUpdateDelete(3, (idAlunno,))

        elif opzione == 4:
            SelectValuesAVG()

        elif opzione == 5:
            mydb.close()
            print("Connessione chiusa. Uscita dal programma.")
            break

        else:
            print("Opzione non valida. Scegli tra 1 e 5.")

    except ValueError:
        print("Inserisci un numero intero valido.")
