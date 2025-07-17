import pandas as pd
import numpy as np

np.random.seed(42)               # per risultati replicabili

# ────────── Esercizio 1 ──────────
reparti = ['Libri', 'Giocattoli']
codici  = [1, 2, 3]

idx_prezzi = pd.MultiIndex.from_product(
    [reparti, codici], names=['Reparto', 'Codice'])

df_prezzi = pd.DataFrame(
    {'Prezzo': np.random.uniform(5, 50, len(idx_prezzi)).round(2)},
    index=idx_prezzi
)

# ────────── Esercizio 2 ──────────
categorie   = ['Elettronica', 'Alimentari', 'Abbigliamento']
codici_prod = [101, 102, 103]

idx_vendite = pd.MultiIndex.from_product(
    [categorie, codici_prod], names=['Categoria', 'Codice'])

df_vendite = pd.DataFrame({
    'Vendite': np.random.uniform(100, 1000, len(idx_vendite)).round(2),
    'Sconto' : np.random.uniform(0, 150,   len(idx_vendite)).round(2)
}, index=idx_vendite)

# Calcolo del valore netto per la categoria 'Elettronica'
elettronica = df_vendite.loc['Elettronica'].copy()
elettronica['Netto'] = elettronica['Vendite'] - elettronica['Sconto']

# ────────── Stampe riepilogative ──────────
print("----- DataFrame Prezzi -----")
print(df_prezzi)

print("\n----- DataFrame Vendite & Sconto -----")
print(df_vendite)

print("\n----- Dati Elettronica con Netto -----")
print(elettronica)

print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
#------------------------------Esercizio 3-----------------------------
gennaio = pd.DataFrame({
    'Giorno': [1, 2, 3],
    'Vendite': [100, 110, 105]
})

febbraio = pd.DataFrame({
    'Giorno': [1, 2, 3],
    'Vendite': [95, 120, 115]
})

marzo = pd.DataFrame({
    'Giorno': [1, 2, 3],
    'Vendite': [130, 125, 140]
})

# Unione dei tre DataFrame
vendite_trimestre = pd.concat([gennaio, febbraio, marzo])

# Stampa del risultato
print("DataFrame unito con concat:")
print(vendite_trimestre)
print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")

#-----------------------Esercizio 4-----------------------------------------

# Creazione dei DataFrame di esempio
studenti = pd.DataFrame({
    'ID': [1, 2, 3],
    'Nome': ['Alice', 'Bob', 'Charlie']
})

voti = pd.DataFrame({
    'ID': [1, 2, 3, 1],
    'Materia': ['Matematica', 'Storia', 'Matematica', 'Inglese'],
    'Voto': [8, 7, 9, 7]
})

# Unione dei due DataFrame sulla colonna 'ID'
studenti_voti = pd.merge(studenti, voti, on='ID')

# Stampa del risultato
print("DataFrame unito con merge:")
print(studenti_voti)