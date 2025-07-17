import numpy as np
print("-------------------------------------------------------")

arr = np.arange(10, 50)
print(arr.dtype)
print("Array:")
print(arr)
arr_f = arr.astype(np.float64)
print(arr_f.dtype)
print("Array convertito in float64:")
print(arr_f)
print(f"Array Shape: {arr.shape}")


print("-------------------------------------------------------")
print("-------------------Esercizio Slicing-------------------")

np.random.seed(42)                 
arr2 = np.random.randint(10, 51, 20)   

first10      = arr[:10]   
last5        = arr[-5:]     
mid_slice    = arr[5:15]    
every_third  = arr[::3]     

arr2_modified = arr.copy()   
arr2_modified[5:10] = 99     


print("Array originale:           ", arr2)
print("Primi 10 elementi:         ", first10)
print("Ultimi 5 elementi:         ", last5)
print("Indici 5–14 (escluso 15):  ", mid_slice)
print("Ogni terzo elemento:       ", every_third)
print("Array dopo la modifica:    ", arr2_modified)


print("-------------------------------------------------------")
print("-------------------Esercizio 3-------------------------")


# Imposta il seed per risultati riproducibili
np.random.seed(42)

# 1. Crea una matrice 6x6 di interi casuali tra 1 e 100
matrice = np.random.randint(1, 101, size=(6, 6))

# 2. Estrai la sotto-matrice centrale 4x4
submatrice = matrice[1:5, 1:5]

# 3. Inverti le righe della sotto-matrice
subm_invertita = submatrice[::-1]

# 5. Sostituisci i multipli di 3 con -1
modified_submatrix = subm_invertita.copy()
modified_submatrix[modified_submatrix % 3 == 0] = -1

# 6. Stampa tutti i risultati
print("Matrice originale:\n", matrice)
print("\nSotto-matrice centrale 4x4:\n", submatrice)
print("\nSotto-matrice con righe invertite:\n", subm_invertita)
print("\nMatrice invertita con multipli di 3 sostituiti da -1:\n", modified_submatrix)


# Lunghezza della diagonale (min tra righe e colonne)
n = subm_invertita.shape[0]

# Lista per contenere gli elementi della diagonale
diagonal_for = []

for i in range(n):
    diagonal_for.append(subm_invertita[i, i])

# Converti in array NumPy (opzionale)
diagonal_for = np.array(diagonal_for)

print("\nDiagonale principale (con for):", diagonal_for)

print("-------------------------------------------------------")
print("-------------------Esercizi pt2--------------------")


print("--------------------------1---------------------------")
array1 = np.random.randint(1, 101, 15)
print("Esercizio 1")
print("Array:", array1)
print("Somma:", array1.sum())
print("Media:", array1.mean())
print("-" * 50)


print("--------------------------2---------------------------")
matrix2 = np.arange(1, 26).reshape(5, 5)
second_col = matrix2[:, 1]      # seconda colonna (indice 1)
third_row  = matrix2[2, :]      # terza riga    (indice 2)
diag_sum   = np.trace(matrix2)  # somma diagonale

print("Esercizio 2")
print("Matrice 5×5:\n", matrix2)
print("Seconda colonna:", second_col)
print("Terza riga:     ", third_row)
print("Somma diagonale:", diag_sum)
print("-" * 50)

print("------------------------------3------------------------")

array3 = np.random.randint(10, 51, (4, 4))   # (4,4) casuale 10‑50
rows = np.array([0, 1, 2, 3])
cols = np.array([1, 3, 2, 0])

selected   = array3[rows, cols]     # (0,1) (1,3) (2,2) (3,0)
odd_rows   = array3[1::2]           # righe con indice dispari
array3[rows, cols] += 10            # modifica in‑place

print("Esercizio 3")
print("Array iniziale 4×4:\n", array3)         
print("Elementi selezionati (+10 applicato):", selected + 10)
print("Righe dispari:\n", odd_rows)
print("Array finale:\n", array3)

