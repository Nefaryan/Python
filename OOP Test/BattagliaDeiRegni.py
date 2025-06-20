import random
from abc import ABC, abstractmethod

class Soldato(ABC):
    def __init__(self, nome, attacco, difesa, salute, costo):
        self.__nome = nome
        self.__attacco = attacco
        self.__difesa = difesa
        self.__salute = salute
        self.max_salute = salute
        self.__costo = costo
        self.__abilità_usata = False

    def get_nome(self):
        return self.__nome

    def get_attacco(self):
        return self.__attacco

    def get_difesa(self):
        return self.__difesa

    def get_salute(self):
        return self.__salute

    def get_costo(self):
        return self.__costo

    def è_vivo(self):
        return self.__salute > 0

    def difenditi(self, danno):
        danno_effettivo = max(0, danno - self.__difesa)
        self.__salute -= danno_effettivo
        return danno_effettivo

    def stato(self):
        print(f"{self.__nome} - Salute: {self.__salute}")

    def cura(self, punti):
        self.__salute = min(self.max_salute, self.__salute + punti)

    def abilità_usata(self):
        return self.__abilità_usata

    def segna_abilità_usata(self):
        self.__abilità_usata = True

    @abstractmethod
    def attacca(self, target):
        pass

    @abstractmethod
    def usa_abilità_speciale(self, alleati, nemici):
        pass

class Cavaliere(Soldato):
    def __init__(self, nome):
        super().__init__(nome, attacco=30, difesa=20, salute=100, costo=200)
        self._assorbimento_attivo = False

    def attacca(self, avversario):
        danno = self.get_attacco()
        if random.random() < 0.2:
            danno *= 2
            print(f"Colpo critico di {self.get_nome()}!")
        print(f"{self.get_nome()} attacca {avversario.get_nome()} con {danno} danni.")
        danno_subito = avversario.difenditi(danno)
        print(f"{avversario.get_nome()} subisce {danno_subito} danni!")

    def difenditi(self, danno):
        if self._assorbimento_attivo:
            danno = danno // 2
            print(f"{self.get_nome()} riduce il danno grazie allo scudo sacro!")
            self._assorbimento_attivo = False
        return super().difenditi(danno)

    def usa_abilità_speciale(self, alleati, nemici):
        if not self.abilità_usata():
            self._assorbimento_attivo = True
            self.segna_abilità_usata()
            print(f"{self.get_nome()} attiva Scudo Sacro!")

class Arciere(Soldato):
    def __init__(self, nome):
        super().__init__(nome, attacco=20, difesa=10, salute=80, costo=150)

    def attacca(self, avversario):
        danno = self.get_attacco()
        print(f"{self.get_nome()} scocca una freccia a {avversario.get_nome()} per {danno} danni.")
        danno_subito = avversario.difenditi(danno)
        print(f"{avversario.get_nome()} subisce {danno_subito} danni!")

    def usa_abilità_speciale(self, alleati, nemici):
        if not self.abilità_usata():
            print(f"{self.get_nome()} usa Pioggia di Frecce!")
            for n in nemici:
                if n.è_vivo():
                    danno = self.get_attacco() // 2
                    n.difenditi(danno)
                    print(f" - {n.get_nome()} subisce {danno} danni da frecce!")
            self.segna_abilità_usata()

class Mago(Soldato):
    def __init__(self, nome):
        super().__init__(nome, attacco=25, difesa=5, salute=70, costo=180)

    def attacca(self, avversario):
        energia = random.randint(10, 40)
        print(f"{self.get_nome()} lancia un incantesimo su {avversario.get_nome()} con {energia} danni.")
        avversario.difenditi(energia)

    def usa_abilità_speciale(self, alleati, nemici):
        if not self.abilità_usata():
            fantasma = SoldatoFantasma(f"Fantasma_{self.get_nome()}")
            alleati.append(fantasma)
            print(f"{self.get_nome()} evoca {fantasma.get_nome()}!")
            self.segna_abilità_usata()

class Guaritore(Soldato):
    def __init__(self, nome):
        super().__init__(nome, attacco=0, difesa=10, salute=60, costo=170)

    def attacca(self, alleati):
        vivi = [a for a in alleati if a.è_vivo() and a != self]
        if vivi:
            target = random.choice(vivi)
            cura = random.randint(15, 30)
            target.cura(cura)
            print(f"{self.get_nome()} cura {target.get_nome()} di {cura} punti. Salute: {target.get_salute()}")
        else:
            print(f"{self.get_nome()} non ha nessuno da curare.")

    def usa_abilità_speciale(self, alleati, nemici):
        if not self.abilità_usata():
            caduti = [a for a in alleati if not a.è_vivo() and a != self]
            if caduti:
                target = caduti[0]
                target.cura(target.max_salute // 2)
                print(f"{self.get_nome()} rianima {target.get_nome()} con metà salute!")
                self.segna_abilità_usata()
            else:
                print(f"{self.get_nome()} non trova alleati caduti.")

class SoldatoFantasma(Soldato):
    def __init__(self, nome):
        super().__init__(nome, attacco=50, difesa=0, salute=1, costo=0)

    def attacca(self, target):
        print(f"{self.get_nome()} (Fantasma) attacca con 50 danni!")
        target.difenditi(50)

    def usa_abilità_speciale(self, alleati, nemici):
        pass


def ha_combattenti_vivi(esercito):
     return any(not isinstance(s, Guaritore) and s.è_vivo() for s in esercito)

def crea_soldato(tipo, nome):
    if tipo == "1":
        return Cavaliere(nome)
    elif tipo == "2":
        return Arciere(nome)
    elif tipo == "3":
        return Mago(nome)
    elif tipo == "4":
        return Guaritore(nome)
    else:
        return None


def menu_acquisti(budget):
    esercito = []
    contatori = {"1": 1, "2": 1, "3": 1, "4": 1}
    tipi_possibili = ["1", "2", "3", "4"]

    print(f"\nBudget disponibile: {budget}")

    while True:
        print("\nTipi di soldati disponibili:")
        print("1 - Cavaliere (200 monete)")
        print("2 - Arciere (150 monete)")
        print("3 - Mago (180 monete)")
        print("4 - Guaritore (170 monete)")
        print("0 - Termina acquisti")

        scelta = input("Seleziona il tipo di soldato da acquistare (0 per terminare): ")
        if scelta == "0":
            break
        if scelta not in tipi_possibili:
            print("Scelta non valida.")
            continue

        costo_unitario = crea_soldato(scelta, "temp").get_costo()
        max_acquisti = budget // costo_unitario
        if max_acquisti == 0:
            print("Budget insufficiente per questo tipo di soldato.")
            continue

        quantita = input(f"Quante unità vuoi acquistare? (max {max_acquisti}): ")
        if not quantita.isdigit() or int(quantita) < 1 or int(quantita) > max_acquisti:
            print("Quantità non valida.")
            continue

        quantita = int(quantita)
        for _ in range(quantita):
            nome = f"{['Cavaliere','Arciere','Mago','Guaritore'][int(scelta)-1]}{contatori[scelta]}"
            contatori[scelta] += 1
            soldato = crea_soldato(scelta, nome)
            esercito.append(soldato)
            budget -= costo_unitario
        print(f"Acquistate {quantita} unità di tipo {['Cavaliere','Arciere','Mago','Guaritore'][int(scelta)-1]}.")
        print(f"Budget rimanente: {budget}")


    return esercito, budget


def acquisto_automatico(budget):
    esercito = []
    contatori = {"1": 1, "2": 1, "3": 1, "4": 1}
    tipi_possibili = ["1", "2", "3", "4"]

    while True:
        tipo = random.choice(tipi_possibili)
        soldato_prototipo = crea_soldato(tipo, "temp")
        costo = soldato_prototipo.get_costo()
        if costo <= budget:
            nome = f"IA_{['Cavaliere','Arciere','Mago','Guaritore'][int(tipo)-1]}{contatori[tipo]}"
            contatori[tipo] += 1
            nuovo_soldato = crea_soldato(tipo, nome)
            esercito.append(nuovo_soldato)
            budget -= costo
        else:
            if all(crea_soldato(t, "temp").get_costo() > budget for t in tipi_possibili):
                break
    return esercito

def scontro(esercito_giocatore, esercito_ia):
    print("\nInizia la battaglia!")

    if not ha_combattenti_vivi(esercito_giocatore) and not ha_combattenti_vivi(esercito_ia):
        print("La battaglia termina in pareggio: solo guaritori rimasti su entrambi i lati.")
        return
    elif not ha_combattenti_vivi(esercito_giocatore):
        print("La battaglia termina: il giocatore ha solo guaritori rimasti. Vittoria IA!")
        return
    elif not ha_combattenti_vivi(esercito_ia):
        print("La battaglia termina: l'IA ha solo guaritori rimasti. Vittoria Giocatore!")
        return

    for g in esercito_giocatore:
        if not esercito_ia:
            break
        bersaglio = random.choice(esercito_ia)

        if not g.abilità_usata() and random.random() < 0.3:
            g.usa_abilità_speciale(esercito_giocatore, esercito_ia)
        else:
            if isinstance(g, Arciere):
                g.attacca(bersaglio)
            elif isinstance(g, Guaritore):
                g.attacca(esercito_giocatore)
            else:
                g.attacca(bersaglio)

    for ia in esercito_ia:
        if not esercito_giocatore:
            break
        bersaglio = random.choice(esercito_giocatore)

        if not ia.abilità_usata() and random.random() < 0.3:
            ia.usa_abilità_speciale(esercito_ia, esercito_giocatore)
        else:
            if isinstance(ia, Arciere):
                ia.attacca(bersaglio)
            elif isinstance(ia, Guaritore):
                ia.attacca(esercito_ia)
            else:
                ia.attacca(bersaglio)

    esercito_giocatore[:] = [s for s in esercito_giocatore if s.è_vivo()]
    esercito_ia[:] = [s for s in esercito_ia if s.è_vivo()]



def main():
    budget_giocatore = 1000
    budget_ia = 1000
    round_num = 0

    print("Benvenuto a 'La Battaglia dei Regni'!\nInizia a reclutare il tuo esercito.")

    esercito_giocatore, budget_giocatore = menu_acquisti(budget_giocatore)
    esercito_ia = acquisto_automatico(budget_ia)

    while esercito_giocatore and esercito_ia:
        round_num += 1
        print(f"\n--- Round {round_num} ---")

        scontro(esercito_giocatore, esercito_ia)

        print("\nStato post battaglia:")
        print("Tuo esercito:")
        for s in esercito_giocatore:
            s.stato()
        print("Esercito IA:")
        for s in esercito_ia:
            s.stato()

        if not esercito_giocatore or not esercito_ia:
            break

        budget_giocatore += 300
        budget_ia += 300

        print("\nHai ricevuto 300 monete!")
        scelta = input("Vuoi acquistare nuovi soldati? (s/n): ")
        if scelta.lower() == "s":
            nuovi, budget_giocatore = menu_acquisti(budget_giocatore)
            esercito_giocatore.extend(nuovi)

        nuovi_ia = acquisto_automatico(budget_ia)
        esercito_ia.extend(nuovi_ia)
        budget_ia = 0

    print("\nFine del gioco!")
    if esercito_giocatore:
        print(f"Hai vinto in {round_num} round! Soldati sopravvissuti: {len(esercito_giocatore)}")
    else:
        print(f"L'IA ha vinto in {round_num} round. Soldati IA sopravvissuti: {len(esercito_ia)}")


if __name__ == "__main__":
    main()
