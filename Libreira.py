import mysql.connector

db = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'admin'
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS biblioteca")
cursor.execute("use biblioteca")

def verifica_presenza_utenti():
    cursor.execute("USE biblioteca")
    cursor.execute("SELECT COUNT(*) FROM utenti")
    risultato = cursor.fetchone()
    return risultato[0] > 0

def crea_libro():
    try:
        sql_crea = "create table if not exists libri(" \
        "id int auto_increment primary key," \
        "titolo varchar(100) not null," \
        "autore varchar(100) not null," \
        "id_prestito int," \
        "unique(titolo, autore)," \
        "foreign key(id_prestito) references utenti(id))"
        cursor.execute(sql_crea)
    except mysql.connector.Error as err:
        print(f"Qualcosa è andato storto: {err}\n")
    except:
        print("Errore creazione tabella\n")


def crea_utente():
    try:
        sql_crea = "create table if not exists utenti(" \
        "id int auto_increment primary key," \
        "username varchar(100) unique not null," \
        "nome varchar(100)," \
        "password varchar(100) not null unique," \
        "ruolo enum('utente', 'bibliotecario'))"
        cursor.execute(sql_crea)
    except mysql.connector.Error as err:
        print(f"Qualcosa è andato storto: {err}\n")
    except:
        print("Errore creazione tabella\n")

def signup(username, nome, password, ruolo):
    try:
        sql_signup = "insert into utenti(username, nome, password, ruolo) values (%s, %s, %s, %s)"
        cursor.execute(sql_signup, (username, nome, password, ruolo))
        db.commit()
        print("Utente registrato correttamente\n")
        return ruolo
    except mysql.connector.Error as err:
        print(f"Qualcosa è andato storto: {err}\n")
    except:
        print("Errore nell'inserimento\n")

def login(username, password):
    try:
        cursor.execute("SELECT id, ruolo FROM utenti WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchone()
        print(result)
        print(result[0], result[1])
        if result:
            print(f"Login effettuato come '{username}' di tipo '{result[1]}'\n")
            return result[0], result[1]
        else:
            print("Credenziali errate.\n")
            return None, None
        
    except mysql.connector.Error as err:
        print(f"Qualcosa è andato storto: {err}\n")
    except:
        print("Errore nell'inserimento\n")

def inserisci_utente(nome):
    if not isinstance(nome, str):
        print("Errore: il nome deve essere una stringa")
        return
    
    if not nome.strip():
        print("Errore: il nome non può essere vuoto")

    try:
        sql_insert = "insert into utenti(nome) values(%s)"
        cursor.execute(sql_insert, (nome,))
        db.commit()
        print("Utente inserito correttamente\n")
    except mysql.connector.Error as err:
        print(f"Qualcosa è andato storto: {err}\n")
    except:
        print("Errore nell'inserimento\n")

    
def inserisci_libro(titolo, autore):
    if not isinstance(titolo, str) or not isinstance(autore, str):
        print("Errore: titolo e autore devono essere stringhe.")
        return
    
    if not titolo.strip() or not autore.strip():
        print("Errore: titolo e autore non possono essere vuoti.")
        return

    sql_verifica = "select count(*) from libri where titolo = %s and autore = %s"
    cursor.execute(sql_verifica, (titolo, autore))
    risultato = cursor.fetchone()

    if risultato[0] > 0:
        print("Il libro già è presente nella biblioteca!")
        return
    
    try:
        sql_insert = "insert into libri(titolo, autore) values(%s, %s)"
        cursor.execute(sql_insert, (titolo, autore))
        db.commit()
        print("Libro inserito correttamente\n")
    except mysql.connector.Error as err:
        print(f"Qualcosa è andato storto: {err}\n")
    except:
        print("Errore nell'inserimento\n")


def visualizza_libri():
    try:
        str_select = "select * from libri"
        cursor.execute(str_select)

        results = cursor.fetchall()
        for result in results:
            print(result)
    except mysql.connector.Error as err:
        print(f"Qualcosa è andato storto: {err}\n")
    except:
        print("Errore nella visualizzazione\n")

def visualizza_utenti():
    try:
        str_select = "select * from utenti"
        cursor.execute(str_select)

        results = cursor.fetchall()
        for result in results:
            print(result)
    except mysql.connector.Error as err:
        print(f"Qualcosa è andato storto: {err}\n")
    except:
        print("Errore nella visualizzazione\n")
    
def cerca_libri_per_autore(autore):
    if not isinstance(autore, str):
        print("Errore: l'autore deve essere una stringa.")
        return
    if not autore.strip():
        print("Errore: l'autore non può essere vuoto")
        return

    try:
        sql_cerca = "select * from libri where autore = %s"
        cursor.execute(sql_cerca, (autore,))

        results = cursor.fetchall()
        if results == []:
            print("Non è stato trovato nessuno libro\n")
        else:
            for result in results:
                print(result)
    except mysql.connector.Error as err:
        print(f"Qualcosa è andato storto: {err}\n")
    except:
        print("Errore nella visualizzazione\n")

def cerca_libri_per_titolo(titolo):
    if not isinstance(titolo, str):
        print("Errore: il titolo deve essere una stringa.")
        return
    if not titolo.strip():
        print("Errore: il titolo non può essere vuoto")
        return

    try:
        sql_cerca = "select * from libri where titolo = %s"
        cursor.execute(sql_cerca, (titolo,))

        results = cursor.fetchall()
        if results == []:
            print("Non è stato trovato nessuno libro\n")
        else:
            for result in results:
                print(result)
    except mysql.connector.Error as err:
        print(f"Qualcosa è andato storto: {err}\n")
    except:
        print("Errore nella visualizzazione\n")

def prendi_in_prestito(id_utente, id_libro):
    if not isinstance(id_utente, int) or not isinstance(id_libro, int):
        print("Errore: gli id devono essere interi")
        return

    if not id_utente or not id_libro:
        print("Errore: gli id non possono essere vuoti.")
        return
    
    try:
        sql = "select count(*) from libri where id = %s"
        cursor.execute(sql, (id_libro,))

        result = cursor.fetchone()

        if not result:
            print("Libro non presente")
        else:
            sql = "select id_prestito from libri where id = %s"
            cursor.execute(sql, (id_libro, ))

            result = cursor.fetchone()

            if result == (None,):
                sql_update = "update libri set id_prestito = %s"
                cursor.execute(sql_update, (id_utente,))
                db.commit()
                print("Libro preso in prestito corettamente")
            else:
                print("Libro già preso in prestito")
    except mysql.connector.Error as err:
        print(f"Qualcosa è andato storto: {err}\n")
    except:
        print("Errore nel prestito\n")


crea_utente()
crea_libro()

print("Benvenuto in biblioteca Der Bücherwurmloch:\n")
while True:
    scelta = int(input("1) Login\n" \
    "2) Registrati\n"))

    if scelta == 1:
        if not verifica_presenza_utenti():
            print("Nessun utente presente:\n")
        else: 
            username = input("Username: ")
            password = input("Password: ")
            id, ruolo = login(username, password)
            break
            
    if scelta == 2:
        ruolo = ""
        username = input("Username: ")
        nome = input("Nome: ")
        password = input("Password: ")
        while ruolo not in ["Utente", "Bibliotecario", "utente", "bibliotecario"]:
            ruolo = input("Ruolo: (Utente, Bibliotecario)")
            if ruolo not in ["Utente", "Bibliotecario", "utente", "bibliotecario"]:
                print("Per favore scegli un'opzione valida\n")
                
        ruolo = signup(username, nome, password, ruolo)
        sql_recupera_id = "select id from utenti where username = %s"
        cursor.execute(sql_recupera_id, (username,))
        id = cursor.fetchone()[0]
        break

while True:
    if ruolo.lower() == 'bibliotecario':
        scelta = int(input("Cosa vuoi fare?\n" \
    "1) Inserire un libro\n" \
    "2) Visualizzare gli utenti\n" \
    "3) Visualizzare i libri\n" \
    "4) Cerca libro per titolo\n" \
    "5) Cerca libro per autore\n" \
    "6) Esci\n"))
        if scelta == 1:
            titolo = input("Qual è il titolo del libro?\n")
            autore = input("Come si chiama l'autore?\n")
            inserisci_libro(titolo, autore)
        elif scelta == 2:
            visualizza_utenti()
        elif scelta == 3:
            visualizza_libri()
        elif scelta == 4:
            titolo = input("Come si chiama il libro da cercare?\n")
            cerca_libri_per_titolo(titolo)
        elif scelta == 5:
            autore = input("Come si chiama l'autore?\n")
            cerca_libri_per_autore(autore)
        elif scelta == 6:
            print("Saluti dalla biblioteca Der Bücherwurmloch!\n")
            db.close()
            break
        else:
            print("Valore non valido\n")
            continue

    elif ruolo.lower() == 'utente':
        scelta = int(input("Cosa vuoi fare?\n" \
    "1) Visualizzare i libri\n" \
    "2) Cerca libro per titolo\n" \
    "3) Cerca libro per autore\n" \
    "4) Prendere in prestito un libro\n"
    "5) Esci\n"))
        if scelta == 1:
            visualizza_libri()
        elif scelta == 2:
            titolo = input("Come si chiama il libro da cercare?\n")
            cerca_libri_per_titolo(titolo)
        elif scelta == 3:
            autore = input("Come si chiama l'autore?\n")
            cerca_libri_per_autore(autore)
        elif scelta == 4:
            visualizza_libri()
            id_libro = int(input("Qual è l'id del libro da prestare?\n"))
            prendi_in_prestito(id, id_libro)
        elif scelta == 5:
            print("Saluti dalla biblioteca Der Bücherwurmloch!\n")
            db.close()
            break
        else:
            print("Valore non valido\n")
