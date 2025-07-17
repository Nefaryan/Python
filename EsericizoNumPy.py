import numpy as np
from numpy.linalg import LinAlgError, inv,det


#  Funzioni operative


def crea_matrice():
    """Chiede dimensioni all'utente e restituisce una matrice casuale di interi 1‑100."""
    while True:
        try:
            rows = int(input("Numero di righe: "))
            cols = int(input("Numero di colonne: "))
            if rows <= 0 or cols <= 0:
                print("Le dimensioni devono essere positive. Riprova.")
                continue
            matrix = np.random.randint(1, 101, size=(rows, cols))
            print("\nNuova matrice creata:\n", matrix)
            return matrix
        except ValueError:
            print("Input non valido. Inserisci numeri interi.")


def sottomatrice_centrale(mat: np.ndarray):
    if mat.shape[0] < 3 or mat.shape[1] < 3:
        print("La matrice è troppo piccola per avere una sotto‑matrice centrale.")
        return None
    sub = mat[1:-1, 1:-1]
    print("\nSotto‑matrice centrale:\n", sub)
    return sub


def transponi_matrice(mat: np.ndarray):
    transposed = mat.T
    print("\nMatrice trasposta:\n", transposed)
    return transposed


def somma_elementi(mat: np.ndarray):
    s = mat.sum()
    print("\nSomma di tutti gli elementi:", s)
    return s


def media_elementi(mat: np.ndarray):
    m = mat.mean()
    print("\nMedia di tutti gli elementi:", m)
    return m


def elementwise_multiply(mat: np.ndarray):
    second = np.random.randint(1, 101, size=mat.shape)
    result = mat * second
    print("\nSeconda matrice (casuale stessa dimensione):\n", second)
    print("\nRisultato della moltiplicazione elemento per elemento:\n", result)
    return result


def matrice_inversa(mat: np.ndarray):
    """Calcola l'inversa se quadrata e invertibile."""
    if mat.shape[0] != mat.shape[1]:
        print("La matrice non è quadrata; non può essere invertita.")
        return None
    try:
        inv_mat = inv(mat.astype(float))
        print("\nMatrice inversa:\n", inv_mat)
        return inv_mat
    except LinAlgError:
        print("La matrice non è invertibile (determinante = 0).")
        return None


def applica_funzioni(mat: np.ndarray):
    """Applica sin, cos o exp a tutti gli elementi."""
    funcs = {"sin": np.sin, "cos": np.cos, "exp": np.exp}
    print("\nFunzioni disponibili:")
    for f in funcs:
        print(" -", f)
    choice = input("Quale funzione applicare? (sin/cos/exp): ").strip().lower()
    if choice not in funcs:
        print("Funzione non valida.")
        return None
    result = funcs[choice](mat)
    print(f"\nMatrice dopo {choice}:\n", result)
    return result


def filtra_elementi(mat: np.ndarray):
    """Filtra elementi sulla base di una condizione (>, <, =)."""
    try:
        threshold = float(input("Valore soglia: "))
        op = input("Operatore (>, <, =): ").strip()
        if op == ">":
            mask = mat > threshold
        elif op == "<":
            mask = mat < threshold
        elif op == "=":
            mask = mat == threshold
        else:
            print("Operatore non riconosciuto.")
            return None
        filtered = mat[mask]
        print("\nElementi che soddisfano la condizione (array piatta):", filtered)
        return filtered
    except ValueError:
        print("Input non valido.")
        return None


def determinante(mat: np.ndarray):
    """Calcola il determinante se la matrice è quadrata."""
    if mat.shape[0] != mat.shape[1]:
        print("La matrice non è quadrata; determinante non definito.")
        return None
    d = det(mat.astype(float))
    print("\nDeterminante della matrice:", d)
    return d

#  Menu interattivo

def menu():
    matrice = None
    options = {
        "1": "Crea nuova matrice 2D",
        "2": "Estrai la sotto‑matrice centrale",
        "3": "Trasponi la matrice",
        "4": "Somma di tutti gli elementi",
        "5": "Media di tutti gli elementi",
        "6": "Moltiplicazione element‑wise con matrice casuale",
        "7": "Calcola l'inversa (se possibile)",
        "8": "Applica funzione matematica (sin/cos/exp)",
        "9": "Filtra elementi per condizione",
        "10": "Determinate della matrice",
        "0": "Esci"
    }

    actions = {
        "2": sottomatrice_centrale,
        "3": transponi_matrice,
        "4": somma_elementi,
        "5": media_elementi,
        "6": elementwise_multiply,
        "7": matrice_inversa,
        "8": applica_funzioni,
        "9": filtra_elementi,
        "10": determinante
    }

    while True:
        print("\n=== Menu Operazioni Matrice ===")
        for key, desc in options.items():
            print(f"{key}. {desc}")
        choice = input("Seleziona un'opzione: ")

        if choice == "1":
            matrice = crea_matrice()
        elif choice in actions:
            if matrice is not None:
                actions[choice](matrice)
            else:
                print("Devi prima creare una matrice (opzione 1).")
        elif choice == "0":
            print("Uscita dal programma. Arrivederci!")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    menu()
