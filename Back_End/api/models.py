from django.db import models #Caixa preta, não sei como funciona, mas está sendo executado

# 1 - API faz tudo dentro do django
#Cria a tabela 
class Autor(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    dataNascimento = models.DateField(null=True, blank=True)
    nacao = models.CharField(max_length=30, null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

#Cria a tabela Editora
class Editora(models.Model):
    editora = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    site = models.URLField(null=True, blank=True)

    #Como será visto os campos
    def __str__(self):
        return f"{self.editora} {self.cnpj} {self.endereco} {self.telefone} {self.email}{self.site}"


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE) #Pega da tabela Autor
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE) #Pega da tabela editora
    isbn = models.CharField(max_length=255)
    descricao = models.TextField()
    idioma = models.CharField(max_length=255, default="Português")
    ano_publicado = models.IntegerField()
    paginas = models.IntegerField()
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    estoque = models.IntegerField()
    desconto = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel =models.BooleanField(default=True)
    dimensoes = models.CharField(max_length=255)
    peso = models.DecimalField(max_digits=10, decimal_places=2)

    #Como será apresentado
    def __str__(self):
        return f"Título:{self.titulo} \nAutor{self.autor} \nAno:{self.ano_publicado}"