class UnitaMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati
    def muovi(self, destinazione):
        print(f"{self.nome} si sposta verso {destinazione} con {self.numero_soldati} soldati.")

    def attacca(self, obiettivo):
        print(f"{self.nome} attacca {obiettivo}!")

    def ritira(self, punto_raccolta):
        print(f"{self.nome} si ritira strategicamente verso {punto_raccolta}.")


class Fanteria(UnitaMilitare):
    def costruisci_trincea(self):
        print(f"{self.nome} sta costruendo trincee difensive.")


class Artiglieria(UnitaMilitare):
    def calibra_artiglieria(self):
        print(f"{self.nome} calibra i cannoni per la massima precisione.")


class Cavalleria(UnitaMilitare):
    def esplora_terreno(self):
        print(f"{self.nome} esplora rapidamente il terreno in cerca di informazioni.")


class SupportoLogistico(UnitaMilitare):
    def rifornisci_unita(self, unita: 'UnitaMilitare'):
        print(f"{self.nome} rifornisce {unita.nome} con viveri e munizioni.")


class Ricognizione(UnitaMilitare):
    def conduci_ricognizione(self):
        print(f"{self.nome} conduce una missione di ricognizione silenziosa.")


class ControlloMilitare(Fanteria,
                         Artiglieria,
                         Cavalleria,
                         SupportoLogistico,
                         Ricognizione):
    def __init__(self):
        self.unita_registrate: dict[str, UnitaMilitare] = {}

    # ----- gestione registro -----
    def registra_unita(self, unita: UnitaMilitare):
        self.unita_registrate[unita.nome] = unita
        print(f"Unità '{unita.nome}' registrata al comando.")

    def mostra_unita(self):
        print("\nElenco delle unità registrate:")
        if not self.unita_registrate:
            print("  (nessuna)")
            return
        for u in self.unita_registrate.values():
            print(f"• {u.nome} – soldati: {u.numero_soldati} – tipo: {u.__class__.__name__}")

    def dettagli_unita(self, nome: str):
        u = self.unita_registrate.get(nome)
        if not u:
            print(" Unità non trovata.")
            return
        print(f"\nDettagli unità '{u.nome}':")
        print(f"  Tipo: {u.__class__.__name__}")
        print(f"  Soldati: {u.numero_soldati}")


if __name__ == "__main__":
    # centro di comando
    hq = ControlloMilitare()

    # creiamo alcune unità specializzate
    alfa = Fanteria("Compagnia Alfa", 120)
    bravo = Artiglieria("Batteria Bravo", 40)
    charlie = Cavalleria("Squadrone Charlie", 60)
    delta = SupportoLogistico("Convoglio Delta", 25)

    # registrazione
    for unita in (alfa, bravo, charlie, delta):
        hq.registra_unita(unita)

    # visualizza tutte le unità
    hq.mostra_unita()

    # azioni di esempio
    alfa.muovi("Collina 213")
    alfa.costruisci_trincea()

    bravo.calibra_artiglieria()
    bravo.attacca("Posizione nemica")

    delta.rifornisci_unita(alfa)

    # dettagli unità specifica
    hq.dettagli_unita("Batteria Bravo")
