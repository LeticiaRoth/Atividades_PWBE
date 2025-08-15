from tamagoshi import Tamaghosi

class Dragao(Tamaghosi):
    def __init__(self, nome):
        super().__init__(nome)
        self.fome = 10
        self.saude = 100
        self.idade = 10
        self.tedio = 5
        self.forca_fogo = 0
    
    def alimentar(self, quantidade):
        resultado = super().alimentar(quantidade)
        self.aumentarForcaPorComida(quantidade)
        return resultado
    
    def aumentarForcaPorComida(self, quantidade):
        self.forca_fogo += quantidade
        if self.forca_fogo > 100:
            self.forca_fogo = 100
    
    def getHumor(self):
        return super().getHumor()
    
    def brincar(self, quantidade):
        return super().brincar(quantidade)
        


class PlantaCarnivora(Tamaghosi):
    def __init__(self, nome):
        super().__init__(nome)
        self.fome = 5
        self.saude = 100
        self.idade = 2
        self.tedio = 2
        self.sede = 110


    def alimentar(self, quantidade):
        return super().alimentar(quantidade)
    
    def brincar(self, quantidade):
        return super().brincar(quantidade)
    
    def getHumor(self):
        return super().getHumor()



class Macaco(Tamaghosi):
    def __init__(self, nome):
        super().__init__(nome)
        self.fome = 0
        self.saude = 100
        self.idade = 2
        self.tedio = 0
        self.pular = 0
        
    def alimentar(self, quantidade):
        return super().alimentar(quantidade)
    
    def brincar(self, quantidade):
        return super().brincar(quantidade)
    
    def getHumor(self):
        return super().getHumor()




def main():
    dragao1 = Dragao("LAYSLLE")
    
    # Alimenta o dragão e aumenta a força automaticamente
    dragao1.alimentar(80)
    dragao1.brincar(40)
    
    print(f"Força de Fogo: {dragao1.forca_fogo}")
    print(f"Humor: {dragao1.getHumor()}")
    print(f"Fome: {dragao1.brincar()}")
main()
