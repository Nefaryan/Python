class MembroSquadra:
    
    def __init__(self,nome, eta):
        self.nome = nome
        self.eta = eta
    
    def descrivi(self):
        print(f"{self.nome} ---- {self.eta}")

class Giocatore(MembroSquadra):
    def __init__(self, nome,eta, ruolo, numero_maglia):
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia

    def descrivi(self):
        super().descrivi()
        print(f"Ruolo: {self.ruolo}, maglia n° {self.numero_maglia}")

    def gioca_partita(self):
        print(f"{self.nome} ({self.ruolo}) scende in campo con il numero {self.numero_maglia}!")

class Allenatore(MembroSquadra):
   
    def __init__(self, nome, eta, anni_di_esperienza):
        super().__init__(nome, eta)
        self.anni_di_esperienza = anni_di_esperienza

    def descrivi(self):
        super().descrivi()
        print(f"Allenatore con {self.anni_di_esperienza} anni di esperienza")

    def dirige_allenamento(self):
        print(f"{self.nome} dirige l’allenamento, impartendo tattiche e motivando la squadra.")        
        
class Assistente(MembroSquadra):
    
    def __init__(self, nome, eta, specializzazione):
        super().__init__(nome, eta)
        self.specializzazione = specializzazione

    def descrivi(self):
        super().descrivi()
        print(f"Assistente specializzato in: {self.specializzazione}")

    def supporta_team(self):
        print(f"{self.nome} fornisce supporto al team come {self.specializzazione}.")


        
if __name__ == "__main__":

    g = Giocatore("Luca", 24, "Attaccante", 9)
    a = Allenatore("Mister Rossi", 50, 22)
    s = Assistente("Pippo",12,"Fisioterapista")
    
    
print("=== Descrizione del giocatore ===")
g.gioca_partita()

print("\n=== Allenamento ===")
a.dirige_allenamento()

print("\n==== Assistente ===")
s.supporta_team()
