ct = ""
with open("loremIpsum.txt","r")as file:
    ct = file.read()

cat = ct.replace("\n","")
print(f"Numero di caratteri {len(cat)}")
parole = ct.split()
print(f"Numero di parole {len(parole)}")
righe = ct.split("\n")
print(f"Numero di righe {len(righe)}")