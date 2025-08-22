import os
import platform

class Tamaghosi:
    def __init__(self, nome:str):
        self.nome = nome
        self.fome = 10
        self.saude = 100
        self.idade = 0
        self.tedio = 0

    def alimentar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            reducao = self.fome * (quantidade / 100)
            self.fome -= reducao

    def brincar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            reducao = self.tedio * (quantidade / 100)
            self.tedio -= reducao

    def getHumor(self):
        humor = 100 - ((self.fome + self.tedio)/2)
        return int(humor) if humor > 0 else 0

    #Determina a saúde, quando a fome e o tédio aumenta, a saúde diminui
    def vida(self):
        if (self.fome > 90) or (self.tedio > 90):
            self.saude -= 40
        elif (self.fome > 80) or (self.tedio > 80):
            self.saude -= 20
        elif (self.fome > 60) or (self.tedio > 60):
            self.saude -= 10
        
        if self.saude <= 0:
            self.saude = 0
            print(f"{self.nome} Seu bichinho infelizmente morreu... :( ")

    def tempoPassando(self):
        self.vida()
        self.idade += 1
        self.tedio += 2.5
        self.fome += 5 # Fome aumenta com o tempo para criar desafio
        if self.fome > 100: self.fome = 100
        if self.tedio > 100: self.tedio = 100

    # Feedback da parte dois
    def status(self):
        print(f"\n--- Status de {self.nome} ---")
        print(f"Idade: {self.idade}")
        print(f"Saude: {self.saude}/100")
        print(f"Fome: {self.fome:.0f}/100")
        print(f"Tedio: {self.tedio:.0f}/100")
        print(f"Humor: {self.getHumor()}/100")


    #Loop de vida
    def esta_vivo(self):
        return self.saude > 0