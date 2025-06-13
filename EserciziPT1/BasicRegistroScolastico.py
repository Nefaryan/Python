alunni = {}
voti=[]

while True:
    name = input("Inserisci il nome dell'alunno o scrivi 'media' per la stampare la media, Esci per uscire")
    if name.lower == "esci":
        break
    
    if name.lower != "media":
     voto = input("Inserisci i voti separati da spazi: ")
    
     voti = voto.split(" ")
    
     for num in range(len(voti)):
        voti[num] = float(voti[num])
        
     alunni[name] = voti
    
    if name.lower == 'media':
        for ind in alunni:
         avg = sum(alunni[ind])/ alunni[ind]
         print(f"Nome: {ind} Media: {avg}")
            
print(alunni)

