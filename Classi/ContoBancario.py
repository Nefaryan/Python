from decimal import Decimal

class ContoBancario:

    def __init__(self, titolare, saldo_iniziale=0):
        self.titolare = titolare
        self.__saldo = Decimal("0.00")
        self.deposita(saldo_iniziale)

    def get_titolare(self):
        return self.__titolare

    def set_titolare(self, valore):
        if isinstance(valore, str) and valore.strip():
            self.__titolare = valore.strip().title()
        else:
            print("Il titolare deve essere una stringa non vuota.")

    titolare = property(get_titolare, set_titolare)

    def get_saldo(self):
        return self.__saldo

    saldo = property(get_saldo)

    def deposita(self, importo):
        importo = Decimal(importo)
        if importo > 0:
            self.__saldo += importo.quantize(Decimal("0.01"))
        else:
            print("L'importo da depositare deve essere positivo.")

    def preleva(self, importo):
        importo = Decimal(importo)
        if importo > 0 and importo <= self.__saldo:
            self.__saldo -= importo.quantize(Decimal("0.01"))
        else:
             print("Importo non valido o fondi insufficienti.")

    def visualizza_saldo(self):
        return f"{self.__saldo:.2f} €"

    def __repr__(self):
        return f"<ContoBancario titolare={self.titolare} saldo={self.__saldo:.2f}€>"




print("=== Benvenuto nella banca ===")
nome = input("Inserisci il nome del titolare: ")
saldo = input("Inserisci il saldo iniziale: ")

conto = ContoBancario(nome, saldo)

while True:
    print("\n--- MENU ---")
    print("1. Deposita denaro")
    print("2. Preleva denaro")
    print("3. Visualizza saldo")
    print("4. Cambia intestatario")
    print("0. Esci")

    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        imp = input("Importo da depositare: ")
        conto.deposita(imp)
        print("Deposito effettuato.")
    elif scelta == "2":
        imp = input("Importo da prelevare: ")
        conto.preleva(imp)
        print("Prelievo effettuato.")
    elif scelta == "3":
        print(f"Saldo attuale: {conto.visualizza_saldo()}")
    elif scelta == "4":
        nuovo_nome = input("Nuovo nome intestatario: ")
        conto.titolare = nuovo_nome
        print(f"Intestatario aggiornato: {conto.titolare}")
    elif scelta == "0":
        print("Uscita. Grazie per aver usato il nostro servizio!")
        break
    else:
        print("Scelta non valida. Riprova.")
