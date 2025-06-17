class Libro:
    casa_editrice = "Rizzoli"
    
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        # Include anche la casa editrice nella descrizione
        return (f"Il libro '{self.titolo}' è stato scritto da {self.autore}, "
                f"ha {self.pagine} pagine ed è pubblicato da {Libro.casa_editrice}.")


class Biblioteca:
    def __init__(self):
        # Lista per memorizzare tutti i libri
        self.libri = []

    def aggiungi_libro(self):
        # Chiede i dati all’utente e crea un nuovo oggetto Libro
        titolo = input("Inserisci il titolo del libro: ")
        autore = input("Inserisci l'autore del libro: ")
        
        while True:
            try:
                pagine = int(input("Inserisci il numero di pagine: "))
                break
            except ValueError:
                print("Inserisci un numero valido!")

        nuovo_libro = Libro(titolo, autore, pagine)
        self.libri.append(nuovo_libro)
        print("Libro aggiunto con successo!\n")

    def stampa_libri(self):
        # Mostra tutti i libri presenti in biblioteca
        if not self.libri:
            print("Nessun libro presente nella biblioteca.\n")
            return

        print("\n Elenco dei libri in biblioteca:")
        for libro in self.libri:
            print(libro.descrizione())
        print()



biblioteca = Biblioteca()

while True:
    scelta = input("Cosa vuoi fare?\n1. Aggiungi un libro\n2. Mostra tutti i libri\n3. Esci\nScelta: ")

    if scelta == "1":
        biblioteca.aggiungi_libro()
    elif scelta == "2":
        biblioteca.stampa_libri()
    elif scelta == "3":
        print("Arrivederci!")
        break
    else:
        print("Scelta non valida. Riprova.")

