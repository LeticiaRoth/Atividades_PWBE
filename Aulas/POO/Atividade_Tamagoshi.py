from tamagoshi import Tamaghosi

#Classes filhas, polimorfismo

#Subclasse Dragão
class Dragao(Tamaghosi):
    def __init__(self, nome):
        super().__init__(nome)
        self.forcaFogo = 10 #Criação atributo da força do fogo

    # Método 1
    def treinarFogo(self):
        print(f"{self.nome} esta treinando suas chamas")
        self.forcaFogo += 15
        self.brincar(10) #treinar reduz tédio em 10%
        print(f"A Forca de Fogo agora é {self.forcaFogo}.")
        self.tempoPassando()

    # Método 2
    def voar(self):
        print(f"{self.nome} voou pelos céus! :) ")
        self.brincar(40) #voarr reduz o tédio em 40%
        self.tempoPassando()
        
    # Método 3
    def soltarFogo(self):
        if self.forcaFogo >= 20:
            print(f"{self.nome} soltou uma baforada de fogo!")
            self.forcaFogo -= 20
        else:
            print(f"{self.nome} tentou, mas não tem força suficiente.")
        self.tempoPassando()
    
    def status(self):
        super().status()
        print(f"Forca de Fogo: {self.forcaFogo}/100")


#Subclasse Planta
class Planta(Tamaghosi):
    def __init__(self, nome):
        super().__init__(nome)
        self.nivelAgua = 50 #nível da água, novo atributo

    # Método 1
    def regar(self):
        print(f"Você regou {self.nome}")
        self.nivelAgua += 25
        if self.nivelAgua > 100: self.nivelAgua = 100 #maior que 100, volta para 100
        self.saude += 10
        if self.saude > 100: self.saude = 100
        self.tempoPassando()

    # Método 2
    def tomarSol(self):
        print(f"{self.nome} fez fotossintese.")
        self.alimentar(50) #fotossíntese reduz a fome em 50%
        self.tempoPassando()

    # Método 3
    def adubar(self):
        print(f"{self.nome} foi adubado(a).")
        self.alimentar(80) # adubo reduz a fome em 80%
        self.tempoPassando()
        
    def status(self):
        super().status()
        print(f"Nível de Água: {self.nivelAgua}/100")


class Macaco(Tamaghosi):
    def __init__(self, nome):
        super().__init__(nome)
        self.bananas = 3 #Atributo da banana

    # Método 1
    def comerBanana(self):
        if self.bananas > 0:
            self.bananas -= 1
            print(f"{self.nome} comeu uma banana! Restam {self.bananas}.")
            self.alimentar(90) #comer reduz a fome em 90%
        else:
            print(f"{self.nome} procurou, mas não tem mais bananas! '-' ")
        self.tempoPassando()

    # Método 2
    def pularArvores(self):
        print(f"{self.nome} pulou entre as arvores!")
        self.brincar(60) #reduz tedio em 60%
        self.tempoPassando()

    # Método 3
    def procurarBananas(self):
        print(f"{self.nome} foi procurar e encontrou mais 2 bananas!")
        self.bananas += 2
        self.tempoPassando()
        
    def status(self):
        super().status()
        print(f"Bananas: {self.bananas}")


#Parte dois com as funcionalidade do mennu

def main():
    #uma lista para o historico
    historico = []

    print("************************************************")
    print(" BEM-VINDO AO TAMAGOSHI - SEU BICHINHO VIRTUAL! ")
    print("************************************************")
    
    bichinho = None
    while bichinho is None:
        try:
            escolha_str = input("\nEscolha seu bichinho:\n1 - Dragao\n2 - Planta\n3 - Macaco\nSua escolha: ")
            escolha = int(escolha_str)
            nome = input("Qual nome você quer dar ao seu bichinho? ")
            if escolha == 1:
                bichinho = Dragao(nome)
            elif escolha == 2:
                bichinho = Planta(nome)
            elif escolha == 3:
                bichinho = Macaco(nome)
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um numero.")
            
    print(f"\nParabéns! {bichinho.nome} nasceu ;)!")
    historico.append(f"{bichinho.nome} nasceu!")

    while bichinho.esta_vivo():
        bichinho.status()
        
        print(f"\nO que você quer fazer com o {bichinho.nome}?")
        print("1 - Alimentar")
        print("2 - Brincar")

        #Depende da escolha
        if isinstance(bichinho, Dragao):
            print("3 - Treinar Fogo")
            print("4 - Voar")
            print("5 - Soltar Fogo")
        elif isinstance(bichinho, Planta):
            print("3 - Regar")
            print("4 - Tomar Sol")
            print("5 - Adubar")
        elif isinstance(bichinho, Macaco):
            print("3 - Comer Banana")
            print("4 - Pular em Arvores")
            print("5 - Procurar Bananas")
        
        print("6 - Ver histórico de ações")
        print("0 - Sair do Jogo")
        
        opcao = input("Digite o número da sua ação: ")
        
        try:
            if opcao == '1':
                qtd = int(input("Qual a porcentagem de comida? "))
                bichinho.alimentar(qtd)
                historico.append(f"Alimentou com {qtd}%.")
            elif opcao == '2':
                qtd = int(input("Qual a porcentagem de brincadeira? "))
                bichinho.brincar(qtd)
                historico.append(f"Brincou por {qtd}%.")
            
            elif isinstance(bichinho, Dragao) and opcao == '3':
                bichinho.treinarFogo()
                historico.append("Treinou o fogo.")
            elif isinstance(bichinho, Dragao) and opcao == '4':
                bichinho.voar()
                historico.append("Voou pelos céus.")
            elif isinstance(bichinho, Dragao) and opcao == '5':
                bichinho.soltarFogo()
                historico.append("Soltou uma baforada de fogo.")
            
            elif isinstance(bichinho, Planta) and opcao == '3':
                bichinho.regar()
                historico.append("Foi regado(a).")
            elif isinstance(bichinho, Planta) and opcao == '4':
                bichinho.tomarSol()
                historico.append("Tomou sol.")
            elif isinstance(bichinho, Planta) and opcao == '5':
                bichinho.adubar()
                historico.append("Foi adubado(a).")
            
            elif isinstance(bichinho, Macaco) and opcao == '3':
                bichinho.comerBanana()
                historico.append("Comeu uma banana.")
            elif isinstance(bichinho, Macaco) and opcao == '4':
                bichinho.pularArvores()
                historico.append("Pulou nas árvores.")
            elif isinstance(bichinho, Macaco) and opcao == '5':
                bichinho.procurarBananas()
                historico.append("Procurou por bananas.")
            
            elif opcao == '6':
                print("\n--- Histórico de Ações ---")
                if not historico:
                    print("Nenhuma ação registrada ainda.")
                else:
                    #usado para contar cada item da lista do hsitorico
                    for i, acao in enumerate(historico):
                        print(f"{i+1}: {acao}")
                input("\nPressione Enter para voltar ao jogo...")
                continue
            
            elif opcao == '0':
                print(f"Atá mais, volte logo!")
                break
            else:
                print("Opçãoo inválida!")
        except ValueError:
            print("Entrada inválida. Por favor, digite um numero.")
        
        print("\n--------------------------------------")

    if not bichinho.esta_vivo():
        print("GAME OVER . . . . ")

# Inicia o programa
main()