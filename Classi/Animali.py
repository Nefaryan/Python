class Animali:
    def __init__(self,nome,eta):
        self.nome = nome
        self.eta = eta
    
    def fai_suono(self):
        print("Suono")

class Pinguino(Animali):
    def __init__(self, nome, eta, isFeed):
        super().__init__(nome, eta, isFeed)        
    
    def fai_suono(self):
        print("Pinguino Verso")
        
class Leone(Animali):
    def __init__(self, nome, eta, haCacciato):
        super().__init__(nome, eta, haCacciato)
    
    def ha_cacciato(self):
        if self.ha_cacciato:
            print("Ha cacciato")
        else:
            print("Non ha cacciato")