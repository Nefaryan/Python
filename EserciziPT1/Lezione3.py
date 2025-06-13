l = ["albero","anatra","gatto","topo","bici"]
l2 = []

for e in l:
    if"a" in e:
        l2.append(e)
print("normale")        
print(l2)
print ("lsit comp")
#ogni elemento in lista che contiene a nella parola
#con end si possono usare più condizioni 
l3 = [par for par in l if "a" in par ]
print(l3)
#Altre collection diversa dalle lista 
#Tupla collection = gli elementi sono racchiuse tra tonde ma non ha metodi per eleiminare ed aggiungere elementi è immutabile
tupla = (1,2,3,4)
#Set sono racchiuse dentro le graffe 
s1 = {1,2,3,"ciao",4,4}

#Fare in modo di avere un solo elemento "albero nella lista"
l4 = ["albero","anatra","gatto","topo","bici","albero"]
#Con list compresion
l5 = [el for el in l4 if el != "albero"]
#Con normale for
for el in l4:
    if el == "albero":
        l4.remove("albero")

#rimuovi spazi e caratteri speciali 
s = "ciao ragazzi, l'altro giorno abbiamo letto dante:'nel mezzo..'!!!"
s2 = ",':.! "
for c in s :
    if c in s2:
      s = s.replace(c,"")
print(s)

#DIZIONARI IN PYTHON
#Snon racchiusi dentro parentesi gaffe e ogni elemento ha una chiave
#Le chiavi possono essere int o stringhe e qualsiasi formato di valore
diz  = {"nome":"Giuseppe", "cognome":"Roberti", "età":29}
clienti = {"id1":diz}

for el in diz:
    print(el)

for el in diz.values():
    print(el)

#.values recupera i valori, .items prende chave e valore, .keys mi fa tornare le chiavi

for c in clienti.values():
    print(c["nome"])

for c in clienti:
    print(clienti[c]["nome"])

# Funzioni sugli iterabili in puthon
ls = [1,2,3,4,5]
print(max(ls))
print(sum(ls))
print(sorted(ls)) 
# per le tuple per ordinarle si può usare il 
# sorted ma la trasforma in lista


#enumerate una funzione built-in che ti permette di iterare su un
# oggetto iterabile (come una lista, una stringa, un dizionario, ecc.) 
# ottenendo sia l'indice che il valore di ogni elemento.