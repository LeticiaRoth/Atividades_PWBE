#Classe simples

#ENCAPSULAMENTO
class Veiculo:
    #Starto as variaveis e seus tipos
    def __init__(self, marca: str, ano_fab: int, cor: str, qnt_portas: int, modelo:str):
        self.marca = marca
        self.ano_fab = ano_fab
        self.cor = cor
        self.qnt_portas = qnt_portas
        self.modelo = modelo
        
    #Método 1
    def andar(self):
        print(f"{self.modelo} andando!")
    
    #Método 2
    def imprimir(self):
        print(
            f"Marca: {self.marca}\n"
            f"Ano de Fabricação: {self.ano_fab}\n"
            f"Cor: {self.cor}\n"
            f"Tem {self.qnt_portas} portas"
        )


#Polimorfismo
class Carro(Veiculo):
    def __init__(self, marca, ano_fab, cor, qnt_portas, modelo, qnt_step:int, litros_porta_mala:int):
        super().__init__(marca, ano_fab, cor, qnt_portas, modelo)

        self.qnt_step = qnt_step
        self.litros_porta_mala =  litros_porta_mala

    def imprimir(self):
        super().imprimir()
        print(
            "Detalhes técnicos:\n"
            f"Quantidade de Steps: {self.qnt_step}\n"
            f"Tamanho do porta malas: {self.litros_porta_mala}\n"
        )

    
#Polimorfismo
class Moto(Veiculo):
    def __init__(self, marca, ano_fab, cor, modelo, qtd_rodas: int, tipo_moto: str):
        super().__init__(marca, ano_fab, cor, 0, modelo)  # Moto não tem portas
        self.qtd_rodas = qtd_rodas
        self.tipo_moto = tipo_moto

    #Chamo a função imprimir da classe Veiculo
    def imprimir(self):
        super().imprimir()
        print(
            f"Quantidade de rodas: {self.qtd_rodas}\n"
            f"Tipo da moto: {self.tipo_moto}"
        )

#Polimorfismo
class Caminhao(Veiculo):
    def __init__(self, marca, ano_fab, cor, qnt_portas, modelo, capacidade_carga:int, qtd_eixos:int):
        super().__init__(marca, ano_fab, cor, qnt_portas, modelo)
        self.capacidade_carga = capacidade_carga
        self.qtd_eixos = qtd_eixos

    #Chamo a função imprimir da classe Veiculo
    def imprimir(self):
        super().imprimir()
        print(
            f"Capacidade de carga: {self.capacidade_carga} toneladas\n"
            f"Quantidade de eixos: {self.qtd_eixos}"
        )


def main():
    print("\n------------------------ AULA REVISÃO ------------------------")
    veiculo2 = Carro("Toytoa", 2007, "Cinza", "4", "Corolla", 1, 10)
    veiculo2.imprimir()
    
    print("----------------------------------------------------------------------")
    moto1 = Moto("JTZ Motos", 2012, "Azul", "Master Ride 150", 2 ,"Cilindrada")
    moto1.imprimir()

    print("----------------------------------------------------------------------")
    caminhao1 = Caminhao("Scania", 2019, "Cinza", 2, "Scania R 450 A6x2NA", 74, 3 )
    caminhao1.imprimir()

main()