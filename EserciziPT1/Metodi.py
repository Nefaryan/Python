# In python per avere più elementi in ingresso basta inserire *
# tutto quello che sarà passato al metodo diventera una tupla
# senza elementi satà vuota
def stampa (* ele):
    for el in ele: print(el)
    
# Si possono inserire più astereschi ovvero ** per trasformare tutti gli
#gli elemtni che vengono passati in ingresso al metodo vengono inseriti
#in un dizionario
def stampa2 (** ele):
    print(ele)

#Qualsiasi codice sotto il return è un errore perchè il return chiude la funziona
def somma (n1,n2):
    var =n1 + n2
    print(var)
    return var

v = somma(4,3)
print(v)  