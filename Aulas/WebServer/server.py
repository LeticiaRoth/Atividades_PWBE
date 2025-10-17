'''
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Definindo a porta
port = 8000

# Definindo o gerenciador/manipulador de requisições
handler = SimpleHTTPRequestHandler

# Criando a instancia servidor
server = HTTPServer(("localhost", port), handler)

# Imprimindo mensagem de OK
print(f"Server Runing in http://localhost:{port}")

server.serve_forever()

'''
 


import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import json
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
    )


class MyHandler(SimpleHTTPRequestHandler):

    # Classe de carregamento
    def loadFilmes(self):
        #Conecta o python com o banco
        cursor = mydb.cursor()
        #Primeiro o nome do banco, após isso a da tablea
        cursor.execute("SELECT * FROM locadora.Diretor")

        result = cursor.fetchall()
        print("Funcionando",result)

        #Laço para chamar meus diretores
        for res in result:
            id_diretor = res[0]
            nome = res[1]
            sobrenome = res[2]
            genero = res[3]
            print(id_diretor,nome,sobrenome,genero)
        cursor.close()
        mydb.commit()


    # Usuário  para login fazendo a comparação
    def accont_user(self, login, password):
        loga = "leticiaroth@gmail.com"
        senha = "12345"
        
        if login == loga and password == senha:
            print("Usuário logado!") 
            # Redireciona para a página de cadastro após o login (LEMBRAR)
            self.send_response(303)
            self.send_header('Location', '/cadastro')
            self.end_headers()
        else:
            print("Usuário não existe!") 
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("Usuário não existe".encode('utf-8'))

    #INSERT
    def insertFilmes(self,nome,atores, diretor, ano, genero, produtora, sinopse, orcamento, duracao, poster):
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO  locadora.filme(titulo, atores, diretor, ano, genero, produtora, sinopse, orcamento, duracao, poster) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(nome,atores, diretor, ano, genero, produtora, sinopse, orcamento, duracao, poster))
        cursor.execute("SELECT id_filme FROM locadora.filme WHERE titulo = %s", (nome,))
        
        resultado = cursor.fetchall()
        print(resultado)
        #Vem uma lista de listas, primeira posicao das listas de listas
        cursor.execute("SELECT * from locadora.filme WHERE id_filme = %s", (resultado[0][0],))
        

        resultado = cursor.fetchall()
        print(resultado)
        cursor.close()
        return resultado

    
    
    # REQUISIÇÕES GET, para servir como API e páginas
    def do_GET(self):
        parsed_path = urlparse(self.path)
        #Apenas para mostrar

        self.loadFilmes()

        path = parsed_path.path
        
        # Rota para a API de todos os filmes
        if path == '/api/filmes':
            try:
                with open("filmes.json", "r", encoding="utf-8") as f:
                    data = f.read()
            except FileNotFoundError:
                data = "[]"
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(data.encode("utf-8"))
            return

        # O URL busca pelo indice do filme tambem
        if path.startswith('/api/filmes/'):
            try:
                # Extrai o índice do filme da URL
                movie_index = int(path.split('/')[-1])
                with open("filmes.json", "r", encoding="utf-8") as f:
                    movies = json.load(f)
                    if 0 <= movie_index < len(movies):
                        self.send_response(200)
                        self.send_header("Content-type", "application/json; charset=utf-8")
                        self.end_headers()
                        self.wfile.write(json.dumps(movies[movie_index], ensure_ascii=False).encode('utf-8'))
                    else:
                        # Se o índice não existir, retorna 404
                        self.send_error(404, "Filme não encontrado")
            except (ValueError, FileNotFoundError, json.JSONDecodeError):
                # Se a URL ou o arquivo for inválido, retorna 400
                self.send_error(400, "Requisição inválida")
            return

        # Rotas 
        routes = {
            "/login": "login.html",
            "/cadastro": "cadastro.html",
            "/listar_filmes": "listar_filmes.html",
            "/editar_filme": "editar_filme.html",
            "/style.css": "style.css",
        }
        
        if path in routes:
            file_path = os.path.join(os.getcwd(), routes[path])
            try:
                with open(file_path, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(content)
            except FileNotFoundError:
                self.send_error(404, "Arquivo não encontrado")
        else:
            super().do_GET()

    # REQUISIÇÕES POST
    def do_POST(self):
        if self.path == '/send_login':
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            login = form_data.get('email', [""])[0]
            password = form_data.get('senha', [""])[0]
            
            # Chama a função para verificar o login 
            self.accont_user(login, password)
            return
        elif self.path == '/send_cadastro':
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            nome = form_data.get('nomeFilme', [""])[0]
            atores = form_data.get('atores', [""])[0]
            diretor = form_data.get('diretor', [""])[0]
            ano = int(form_data.get('ano', ["0"])[0])  
            genero = form_data.get('genero', [""])[0]
            produtora = form_data.get('produtora', [""])[0]
            orcamento = (form_data.get('orcamento', ["0"])[0])  
            sinopse = form_data.get('sinopse', [""])[0]
            duracao = form_data.get('duracao', [""])[0]               
            poster = form_data.get('capa', [""])[0]

            resp = self.insertFilmes(nome,atores, diretor, ano, genero, produtora, sinopse, orcamento, duracao, poster)
            print("Funcionou")

            
            """
            # Cria um dicionário com os dados do novo filme
            new_movie = {
                'nomeFilme': form_data.get('nomeFilme', [""])[0],
                'atores': form_data.get('atores', [""])[0],
                'diretor': form_data.get('diretor', [""])[0],
                'ano': form_data.get('ano', [""])[0],
                'genero': form_data.get('genero', [""])[0],
                'produtora': form_data.get('produtora', [""])[0],
                'sinopse': form_data.get('sinopse', [""])[0],
            }
            
            # Lê o arquivo JSON existente e adiciona o novo filme
            try:
                with open("filmes.json", "r", encoding="utf-8") as f:
                    movies = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                movies = []
            
            movies.append(new_movie)

            with open("filmes.json", "w", encoding="utf-8") as f:
                json.dump(movies, f, indent=4, ensure_ascii=False)
            
            
            print("Novo Filme Cadastrado:")
            print(new_movie)
            """
            
            self.send_response(303)
            self.send_header('Location', '/listar_filmes')
            self.end_headers()
            
        else:
            super().do_POST()

    # REQUISIÇÕES DELETE
    def do_DELETE(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path.startswith('/api/filmes/'):
            try:
                # Pega o índice do filme a ser deletado
                movie_index = int(parsed_path.path.split('/')[-1])
                
                with open("filmes.json", "r+", encoding="utf-8") as f:
                    movies = json.load(f)
                    
                    if 0 <= movie_index < len(movies):
                        # Remove o filme da lista
                        deleted_movie = movies.pop(movie_index)
                        
                        # Volta para o início e reescreve
                        f.seek(0)
                        json.dump(movies, f, indent=4, ensure_ascii=False)
                        f.truncate()
                        
                        print(f"Filme deletado: {deleted_movie['nomeFilme']}")
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps({"message": "Filme deletado com sucesso"}).encode('utf-8'))
                    else:
                        self.send_error(404, "Índice de filme não encontrado")
            except (ValueError, FileNotFoundError, json.JSONDecodeError):
                self.send_error(400, "Requisição inválida ou arquivo não encontrado")
        else:
            self.send_error(404, "Recurso não encontrado")

    # REQUISIÇÕES PUT
    def do_PUT(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path.startswith('/api/filmes/'):
            try:
                # Pega pelo índice
                movie_index = int(parsed_path.path.split('/')[-1])
                content_length = int(self.headers['Content-Length'])
                body = self.rfile.read(content_length).decode('utf-8')
                updated_data = json.loads(body)
                
                with open("filmes.json", "r+", encoding="utf-8") as f:
                    movies = json.load(f)
                    
                    if 0 <= movie_index < len(movies):
                        # Atualiza os dados
                        movies[movie_index].update(updated_data)
                        
                        f.seek(0)
                        json.dump(movies, f, indent=4, ensure_ascii=False)
                        f.truncate()
                        
                        print(f"Filme atualizado: {movies[movie_index]['nomeFilme']}")
                        self.send_response(200)
                        self.send_header("Content-type", "application/json")
                        self.end_headers()
                        self.wfile.write(json.dumps({"message": "Filme atualizado com sucesso"}).encode('utf-8'))
                    else:
                        self.send_error(404, "Índice de filme não encontrado")
            except (ValueError, FileNotFoundError, json.JSONDecodeError):
                self.send_error(400, "Requisição inválida")
        else:
            self.send_error(404, "Recurso não encontrado, veja lista de filmes")

# Função para rodar o servidor 
def main():
    server_address =('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print("Server running at http://localhost:8000")
    httpd.serve_forever()

if __name__ == '__main__':
    main()