-- Criação do banco de dados
CREATE DATABASE locadora;
USE locadora;

-- Criação da tabela diretor
CREATE TABLE diretor(
    id_diretor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    sobrenome VARCHAR(255),
    genero ENUM ("Feminino","Masculino","Outro")
);

-- Inserção de 20 diretores
INSERT INTO diretor (nome, sobrenome, genero) VALUES 
('Thiago', 'Lopes', 'Masculino'),
('Carla', 'Mota', 'Feminino'),
('Renato', 'Alves', 'Masculino'),
('Juliana', 'Pinto', 'Feminino'),
('Eduardo', 'Santos', 'Masculino'),
('Marina', 'Figueiredo', 'Feminino'),
('Rafael', 'Gomes', 'Masculino'),
('Bianca', 'Campos', 'Feminino'),
('Leonardo', 'Silveira', 'Masculino'),
('Camila', 'Nunes', 'Feminino'),
('Rodrigo', 'Teixeira', 'Masculino'),
('Aline', 'Freitas', 'Feminino'),
('Vinícius', 'Cardoso', 'Masculino'),
('Larissa', 'Moura', 'Feminino'),
('Gustavo', 'Ferreira', 'Masculino'),
('Priscila', 'Almeida', 'Feminino'),
('Diego', 'Costa', 'Masculino'),
('Sabrina', 'Ribeiro', 'Feminino'),
('Felipe', 'Barbosa', 'Masculino'),
('Ana', 'Torres', 'Outro');

-- Verifica os diretores cadastrados
SELECT * FROM diretor;

-- Criação da tabela filme
CREATE TABLE filme(
    id_filme INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    atores VARCHAR(255) NOT NULL,
    diretor VARCHAR(255) NOT NULL,
    ano YEAR NOT NULL,
    genero VARCHAR(255) NOT NULL,
    produtora VARCHAR(255) NOT NULL,
    sinopse TEXT NOT NULL
);

INSERT INTO filme (titulo, atores, diretor, ano, genero, produtora, sinopse) VALUES
('Interestelar', 'Matthew McConaughey', 'Christopher Nolan', 2014, 'Ficção Científica', 'Paramount Pictures', 'Uma equipe de exploradores viaja através de um buraco de minhoca em busca de um novo lar para a humanidade.'),
('O Grande Gatsby', 'Leonardo DiCaprio', 'Baz Luhrmann', 2013, 'Drama', 'Warner Bros', 'Um misterioso milionário se apaixona por uma mulher do passado enquanto vive na extravagância da década de 1920.'),
('Os Vingadores', 'Robert Downey Jr., Chris Evans', 'Joss Whedon', 2012, 'Ação', 'Marvel Studios', 'Super-heróis se unem para impedir que Loki conquiste a Terra com seu exército alienígena.'),
('O Lobo de Wall Street', 'Leonardo DiCaprio', 'Martin Scorsese', 2013, 'Biografia', 'Paramount Pictures', 'A história real de Jordan Belfort, um corretor da bolsa que viveu uma vida de excessos e crimes financeiros.'),
('Mad Max: Estrada da Fúria', 'Tom Hardy, Charlize Theron', 'George Miller', 2015, 'Ação', 'Warner Bros', 'Em um mundo pós-apocalíptico, Max e Furiosa lutam para escapar de um tirano em busca de liberdade.'),
('A Origem', 'Leonardo DiCaprio', 'Christopher Nolan', 2010, 'Ficção Científica', 'Warner Bros.', 'Um ladrão que rouba segredos corporativos através do uso da tecnologia de compartilhamento de sonhos recebe a tarefa inversa de plantar uma ideia na mente de um CEO.'),
('Coringa', 'Joaquin Phoenix', 'Todd Phillips', 2019, 'Suspense', 'Warner Bros.', 'Em Gotham City, o comediante mentalmente perturbado Arthur Fleck é marginalizado pela sociedade, levando-o a uma espiral de loucura e crimes sangrentos.'),
('Parasita', 'Song Kang-ho', 'Bong Joon-ho', 2019, 'Suspense', 'CJ Entertainment', 'A ganância e a discriminação de classe ameaçam o relacionamento simbiótico recém-formado entre a rica família Park e o pobre clã Kim.'),
('Django Livre', 'Jamie Foxx, Christoph Waltz', 'Quentin Tarantino', 2012, 'Faroeste', 'Columbia Pictures', 'Com a ajuda de um caçador de recompensas alemão, um escravo liberto parte para resgatar sua esposa de um brutal proprietário de uma plantação no Mississippi.'),
('O Regresso', 'Leonardo DiCaprio', 'Alejandro G. Iñárritu', 2015, 'Aventura', '20th Century Fox', 'Um caçador de peles luta pela sobrevivência depois de ser atacado por um urso e abandonado por sua própria equipe de caça.'),
('A Chegada', 'Amy Adams', 'Denis Villeneuve', 2016, 'Ficção Científica', 'Paramount Pictures', 'Uma linguista trabalha com os militares para se comunicar com formas de vida alienígenas depois que doze naves espaciais misteriosas aparecem em todo o mundo.'),
('Corra!', 'Daniel Kaluuya', 'Jordan Peele', 2017, 'Terror', 'Universal Pictures', 'Um jovem fotógrafo afro-americano descobre um segredo perturbador quando conhece os pais aparentemente liberais de sua namorada branca.'),
('La La Land: Cantando Estações', 'Ryan Gosling, Emma Stone', 'Damien Chazelle', 2016, 'Musical', 'Lionsgate', 'Enquanto perseguem seus sonhos em Los Angeles, um pianista de jazz e uma aspirante a atriz se apaixonam, mas enfrentam decisões que ameaçam separar seus mundos.'),
('O Cavaleiro das Trevas', 'Christian Bale, Heath Ledger', 'Christopher Nolan', 2008, 'Ação', 'Warner Bros.', 'Batman enfrenta seu maior desafio psicológico e físico ao combater a anarquia e o caos do Coringa, um novo tipo de criminoso que busca mergulhar Gotham na escuridão.'),
('Whiplash: Em Busca da Perfeição', 'Miles Teller, J.K. Simmons', 'Damien Chazelle', 2014, 'Drama', 'Sony Pictures Classics', 'Um jovem e promissor baterista de jazz se matricula em um conservatório de música de elite, onde seus sonhos de grandeza são orientados por um instrutor abusivo.'),
('A Rede Social', 'Jesse Eisenberg', 'David Fincher', 2010, 'Biografia', 'Columbia Pictures', 'A história de como o estudante de Harvard Mark Zuckerberg criou o site de rede social que se tornaria conhecido como Facebook, e os processos que se seguiram.'),
('Pulp Fiction: Tempo de Violência', 'John Travolta, Uma Thurman', 'Quentin Tarantino', 1994, 'Crime', 'Miramax', 'As vidas de dois assassinos de aluguel, um boxeador, a esposa de um gângster e um casal de assaltantes se entrelaçam em quatro contos de violência e redenção.'),
('Matrix', 'Keanu Reeves', 'Lana Wachowski, Lilly Wachowski', 1999, 'Ficção Científica', 'Warner Bros.', 'Um hacker de computador descobre que o mundo é uma simulação de realidade virtual e se junta a uma rebelião para libertar a humanidade.'),
('Forrest Gump: O Contador de Histórias', 'Tom Hanks', 'Robert Zemeckis', 1994, 'Drama', 'Paramount Pictures', 'As presidências de Kennedy e Johnson, a Guerra do Vietnã e outros eventos históricos se desenrolam através da perspectiva de um homem do Alabama com um QI baixo, mas cujo único desejo é se reunir com seu amor de infância.'),
('O Silêncio dos Inocentes', 'Jodie Foster, Anthony Hopkins', 'Jonathan Demme', 1991, 'Suspense', 'Orion Pictures', 'Uma jovem estagiária do FBI deve pedir a ajuda de um brilhante e manipulador assassino canibal para capturar outro assassino em série que tem um padrão de esfolar suas vítimas.');

SELECT * FROM filme;

