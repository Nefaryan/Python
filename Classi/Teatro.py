class Posto:
    def __init__(self, numero, fila):
        self._numero = numero
        self._fila = fila
        self._occupato = False
    
    def prenota(self):
        if self._occupato:
            print("Il posto", self._fila + str(self._numero), "è già occupato.")
            return False
        self._occupato = True
        print("Prenotato posto", self._fila + str(self._numero))
        return True   
    
    def libera(self):
        if not self._occupato:
            print("Il posto", self._fila + str(self._numero), "è già libero.")
            return False
        self._occupato = False
        print("Il posto", self._fila + str(self._numero), "è stato liberato.")
        return True    
    
    def numero(self):
        return self._numero

    def fila(self):
        return self._fila

    def occupato(self):
        return self._occupato

    def __repr__(self):
        stato = "X" if self._occupato else "O"
        return self._fila + str(self._numero) + " [" + stato + "]"
    
class PostoVIP(Posto):
    
    def __init__(self, numero, fila, servizi_extra):
        super().__init__(numero, fila)
        self._servizi_extra = servizi_extra
    
    def servizi_extra(self):
        return self._servizi_extra

    
    def prenota(self):
        if super().prenota():
            print(f"Servizio Vip: {self.servizi_extra()}")

class PostoStandard(Posto):
    def __init__(self, numero, fila, costo_online=2):
        super().__init__(numero, fila)
        self._costo_online = costo_online

    def prenota(self):
        if super().prenota():
            print(f"Supplemento online: {self._costo_online} €")

class Teatro:
    def __init__(self):
        self._posti = []

    def aggiungi_posto(self, posto):
        self._posti.append(posto)

    def prenota_posto(self, numero, fila):
        for p in self._posti:
            if p.numero() == numero and p.fila().lower() == fila.lower():
                p.prenota()
                return
        print("Posto non trovato.")

    def mostra_posti_occupati(self):
        trovati = False
        for p in self._posti:
            if p.occupato():
                print(p)
                trovati = True
        if not trovati:
            print("Nessun posto occupato.")


if __name__ == "__main__":
    t = Teatro()
    t.aggiungi_posto(PostoVIP(1, "A", "Champagne, Lounge"))
    t.aggiungi_posto(PostoStandard(2, "A"))
    t.aggiungi_posto(PostoStandard(3, "B"))
    t.aggiungi_posto(PostoVIP(4, "B", "Parcheggio riservato"))

    t.prenota_posto(1, "A")
    t.prenota_posto(3, "B")
    t.prenota_posto(1, "A") 

    t.mostra_posti_occupati()