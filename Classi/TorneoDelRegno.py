from abc import ABC, abstractmethod
import random

# ───────── Costanti di configurazione ─────────
MAX_HEALTH = 100            # Salute massima di un combattente
BAR_LENGTH = 20             # Lunghezza della barra di salute visualizzata
HEAL_AFTER_FIGHT = 10       # Quantità di salute ripristinata dopo un duello


def health_bar(current: int, maximum: int = MAX_HEALTH) -> str:
    """Ritorna una barra grafica della salute con blocchi pieni e vuoti."""
    filled = int((current / maximum) * BAR_LENGTH)
    return "[" + "█" * filled + "-" * (BAR_LENGTH - filled) + "]"


# ───────── Classe astratta Combattente ─────────
class Combattente(ABC):
    def __init__(self, nome: str, atk_base: int, def_base: int):
        self.__nome = nome
        self.__salute = MAX_HEALTH
        self.__atk_base = atk_base
        self.__def_base = def_base
        self.saltare_turno = False  # Flag per saltare il turno (usato da incantesimi)

    # ----- getter / setter -----
    def get_nome(self):
        return self.__nome

    def get_salute(self):
        return self.__salute

    def set_salute(self, valore):
        # Impedisce che la salute vada sotto 0 o sopra il massimo
        self.__salute = max(0, min(valore, MAX_HEALTH))

    def get_attacco_base(self):
        return self.__atk_base

    def get_difesa_base(self):
        return self.__def_base

    # ----- Metodo astratto da implementare nelle classi figlie -----
    @abstractmethod
    def attacca(self, avversario: "Combattente", log: list[str]):
        pass

    # ----- Metodi comuni a tutti i combattenti -----
    def subisci_danno(self, danno):
        # Calcola danno effettivo sottraendo difesa base e aggiorna salute
        danno_effettivo = max(0, danno - self.get_difesa_base())
        self.set_salute(self.get_salute() - danno_effettivo)
        return danno_effettivo

    def e_vivo(self):
        return self.get_salute() > 0

    def ripristina_salute(self):
        # Cura una quantità fissa di salute dopo il duello
        self.set_salute(self.get_salute() + HEAL_AFTER_FIGHT)

    def stato(self):
        # Ritorna una stringa con nome, classe e barra salute
        return (
            f"{self.get_nome()} ({self.__class__.__name__}) - "
            f"Salute: {self.get_salute()} {health_bar(self.get_salute())}"
        )


# ───────── Classi derivate ─────────
class Cavaliere(Combattente):
    def __init__(self, nome):
        super().__init__(nome, 15, 10)
        self.turni_da_ultima_parata = 0  # Contatore per gestire la parata ogni 3 turni
        self.botte = False      # Flag che potenzia l'attacco dopo danni elevati subiti
        self.bonus_difesa_attivo = False  # Se salute sotto soglia, aumenta difesa

    def attacca(self, avversario: Combattente, log: list[str]):
        danno = self.get_attacco_base()

        if self.botte:
            danno = int(danno * 3)
            log.append(f"{self.get_nome()} è in cerca di sangue esegue Attacco potenziato!")
            self.botte = False

        if random.random() < 0.20:
            danno *= 2
            log.append(f"Colpo potente di {self.get_nome()}!")

        inflitto = avversario.subisci_danno(danno)
        log.append(f"{self.get_nome()} colpisce {avversario.get_nome()} infliggendo {inflitto} danni.")

        self.turni_da_ultima_parata += 1

    def subisci_danno(self, danno):
        if not self.bonus_difesa_attivo and self.get_salute() <= 30:
            self._Combattente__def_base += 10
            self.bonus_difesa_attivo = True

        if self.turni_da_ultima_parata >= 3:
            self.turni_da_ultima_parata = 0
            return 0

        danno_effettivo = max(0, danno - self.get_difesa_base())
        self.set_salute(self.get_salute() - danno_effettivo)

        if danno_effettivo > 30:
            self.botte = True

        return danno_effettivo


class Arciere(Combattente):
    def __init__(self, nome):
        super().__init__(nome, 15, 10)

    def attacca(self, avversario, log):
        # Primo attacco
        modificatore1 = 2.0 if random.random() < 0.5 else 1.0
        danno1 = int(self.get_attacco_base() * modificatore1)
        inflitto1 = avversario.subisci_danno(danno1)
        tipo1 = "doppio danno" if modificatore1 == 2.0 else "danno normale"
        log.append(f"{self.get_nome()} attacca {avversario.get_nome()} ({tipo1}) infliggendo {inflitto1} danni.")

        secondo_attacco_eseguito = False

        # Secondo attacco (30% probabilità)
        if random.random() < 0.3:
            secondo_attacco_eseguito = True
            modificatore2 = 0.5 if random.random() < 0.5 else 2.0
            danno2 = int(self.get_attacco_base() * modificatore2)
            inflitto2 = avversario.subisci_danno(danno2)
            tipo2 = "mezzo danno" if modificatore2 == 0.5 else "doppio danno"
            log.append(f"{self.get_nome()} effettua un secondo attacco ({tipo2}) infliggendo {inflitto2} danni.")

        # Terzo attacco bonus (10% probabilità solo se secondo attacco eseguito)
        if secondo_attacco_eseguito and random.random() < 0.1:
            danno3 = int(self.get_attacco_base() * 2.0)
            inflitto3 = avversario.subisci_danno(danno3)
            log.append(f"{self.get_nome()} esegue un attacco bonus! (doppio danno) infliggendo {inflitto3} danni.")


class Mago(Combattente):
    def __init__(self, nome):
        super().__init__(nome, 0, 5)
        self._scudo_attivo = False

    def attacca(self, avversario: Combattente, log: list[str]):
        incantesimi = ["blocca", "danno", "scudo", "palla_di_fuoco", "catena_di_fulmini",""]
        incantesimo = random.choice(incantesimi)

        if incantesimo == "blocca":
            tiro_salvezza = d20()
            log.append(f"{self.get_nome()} lancia 'Blocca'! {avversario.get_nome()} tira il dado salvezza: {tiro_salvezza}")
            if tiro_salvezza < 10:
                avversario.saltare_turno = True
                log.append(f"{avversario.get_nome()} è immobilizzato per un turno!")
            else:
                log.append(f"{avversario.get_nome()} resiste all'incantesimo!")

        elif incantesimo == "danno":
            danno = random.randint(10, 40)
            inflitto = avversario.subisci_danno(danno)
            log.append(f"{self.get_nome()} lancia un incantesimo di attacco infliggendo {inflitto} danni a {avversario.get_nome()}.")

        elif incantesimo == "scudo":
            self._scudo_attivo = True
            log.append(f"{self.get_nome()} lancia 'Scudo'! Il prossimo attacco subito sarà dimezzato.")

        elif incantesimo == "palla_di_fuoco":
            danno = random.randint(30, 60)
            inflitto = avversario.subisci_danno(danno)
            log.append(f"{self.get_nome()} scaglia una 'Palla di Fuoco' su {avversario.get_nome()}, infliggendo {inflitto} danni!")
            
            if random.random() < 0.15:
                autolesione = random.randint(5, 15)
                self.subisci_danno(autolesione)
                log.append(f"La palla di fuoco esplode troppo vicino! {self.get_nome()} subisce {autolesione} danni!")

        elif incantesimo == "catena_di_fulmini":
            danni = []
            for i in range(3):
                danno = random.randint(5, 15)
                inflitto = avversario.subisci_danno(danno)
                danni.append(inflitto)
                log.append(f"{self.get_nome()} lancia un fulmine n.{i+1} infliggendo {inflitto} danni!")
            totale = sum(danni)
            log.append(f"Totale danni inflitti da 'Catena di fulmini': {totale}")
        else:
            log.append("Magikarp usa Splash:\nNon succede nulla")


    def subisci_danno(self, danno):
        if self._scudo_attivo:
            danno = danno // 2
            self._scudo_attivo = False
        return super().subisci_danno(danno)


# ───────── Funzioni di utilità ─────────
def stampa_bracket(partecipanti):
    n = len(partecipanti)
    print(f"\nBracket con {n} partecipanti:")
    for i in range(0, n, 2):
        print("-" * 75)
        print(f"Match: {partecipanti[i].get_nome()} VS {partecipanti[i + 1].get_nome()}")
    print("-" * 75)


def d20():
    return random.randint(1, 20)


def scrivi_log_su_file(log, filename="log_torneo.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for riga in log:
            file.write(riga + "\n")


def crea_combattente() -> Combattente:
    mapping = {"1": Cavaliere, "2": Arciere, "3": Mago}
    while True:
        scelta = input("Scegli tipo (1=Cavaliere, 2=Arciere, 3=Mago): ")
        if scelta in mapping:
            break
        print("Scelta non valida.")
    nome = input("Nome del combattente: ")
    return mapping[scelta](nome)


def crea_partecipanti() -> list[Combattente]:
    while True:
        try:
            n = int(input("Numero di partecipanti (pari e >=2): "))
            if n >= 2 and n % 2 == 0:
                break
        except ValueError:
            pass
        print("Input non valido.")
    return [crea_combattente() for _ in range(n)]


# ───────── Logica di combattimento ─────────
def duello(c1, c2, round_n, log):
    log.append(f"\n=== Round {round_n}: {c1.get_nome()} vs {c2.get_nome()} ===")

    dado_c1 = d20()
    dado_c2 = d20()
    log.append(f"{c1.get_nome()} tira il dado: {dado_c1}")
    log.append(f"{c2.get_nome()} tira il dado: {dado_c2}")

    while dado_c1 == dado_c2:
        log.append("Pareggio nel tiro, si rilancia...")
        dado_c1 = d20()
        dado_c2 = d20()
        log.append(f"{c1.get_nome()} tira il dado: {dado_c1}")
        log.append(f"{c2.get_nome()} tira il dado: {dado_c2}")

    if dado_c1 > dado_c2:
        primo, secondo = c1, c2
    else:
        primo, secondo = c2, c1

    log.append(f"{primo.get_nome()} inizia per primo!")

    turno = 0
    while primo.e_vivo() and secondo.e_vivo():
        log.append(f"\nTurno {turno + 1}:")

        # Primo combattente attacca se non deve saltare turno
        if turno % 2 == 0:
            if not primo.saltare_turno:
                log.append(f"{primo.get_nome()} attacca.")
                primo.attacca(secondo, log)
            else:
                log.append(f"{primo.get_nome()} è immobilizzato e salta il turno!")
                primo.saltare_turno = False
        else:
            if not secondo.saltare_turno:
                log.append(f"{secondo.get_nome()} attacca.")
                secondo.attacca(primo, log)
            else:
                log.append(f"{secondo.get_nome()} è immobilizzato e salta il turno!")
                secondo.saltare_turno = False

        log.append(primo.stato())
        log.append(secondo.stato())

        turno += 1

    vincitore = primo if primo.e_vivo() else secondo
    log.append(f"\n{vincitore.get_nome()} vince il duello!\n")

    vincitore.ripristina_salute()
    return vincitore


def torneo_bracket(partecipanti):
    log = []

    round_n = 1
    while len(partecipanti) > 1:
        print(f"\n--- ROUND {round_n} ---")
        stampa_bracket(partecipanti)

        vincitori = []
        for i in range(0, len(partecipanti), 2):
            vincitore = duello(partecipanti[i], partecipanti[i + 1], round_n, log)
            vincitori.append(vincitore)

        partecipanti = vincitori
        round_n += 1

    campione = partecipanti[0]
    print(f"\nIl campione del torneo è {campione.get_nome()}!")

    print("\n--- Log completo del torneo ---")
    for riga in log:
        print(riga)

    scrivi_log_su_file(log)
    return campione


# ───────── Entrypoint ─────────
def main() -> None:
    print("Benvenuto al Torneo del Regno!")
    partecipanti = crea_partecipanti()

    n = len(partecipanti)
    if (n & (n - 1)) != 0:
        print("Attenzione: il numero di partecipanti non è un multiplo di 2, il torneo potrebbe non funzionare correttamente.")

    vincitore = torneo_bracket(partecipanti)
    print(f"\nIl campione del torneo è {vincitore.get_nome()}")


if __name__ == "__main__":
    main()
