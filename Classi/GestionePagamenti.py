from abc import ABC, abstractmethod

# Classe astratta
class MetodoPagamento(ABC):
    @abstractmethod
    def effettua_pagamento(self, importo):
        pass

# Sottoclasse: Carta di Credito
class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di €{importo:.2f} effettuato con Carta di Credito.")

# Sottoclasse: PayPal
class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di €{importo:.2f} effettuato tramite PayPal.")

# Sottoclasse: Bonifico Bancario
class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di €{importo:.2f} effettuato tramite Bonifico Bancario.")

# Classe GestorePagamenti
class GestorePagamenti:
    def __init__(self, metodo: MetodoPagamento):
        self.metodo = metodo

    def paga(self, importo):
        self.metodo.effettua_pagamento(importo)

# Esempio d'uso
if __name__ == "__main__":
    # Lista di metodi di pagamento
    metodi = [
        CartaDiCredito(),
        PayPal(),
        BonificoBancario()
    ]

    # Simulazione pagamento con ciascun metodo
    for metodo in metodi:
        gestore = GestorePagamenti(metodo)
        gestore.paga(100.00)