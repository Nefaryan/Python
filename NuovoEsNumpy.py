import numpy as np

# 1. Creazione dei due array di voti casuali tra 18 e 30
voti_classe1 = np.random.randint(18, 31, size=10)
voti_classe2 = np.random.randint(18, 31, size=10)

# 2. Concatenazione dei due array
tutti_voti = np.concatenate((voti_classe1, voti_classe2))

# 3. Suddivisione in 5 sottogruppi
gruppi = np.array_split(tutti_voti, 5)

# 4. Ordinamento di ciascun sottogruppo
gruppi_ordinati = [np.sort(gruppo) for gruppo in gruppi]

# 5. Stampa dei risultati
print("Array completo dei voti concatenati:\n", tutti_voti)
print("\nLista ordinata dei voti per ciascun gruppo:")

for i, gruppo in enumerate(gruppi_ordinati, start=1):
    print(f"  Gruppo {i}: {gruppo} (media: {np.mean(gruppo):.2f})")

# Media complessiva (opzionale)
media_totale = np.mean(tutti_voti)
print(f"\nMedia voto totale: {media_totale:.2f}")
