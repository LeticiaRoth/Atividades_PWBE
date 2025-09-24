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

class MyHandler(SimpleHTTPRequestHandler):

    #Usuário teste
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
    
    #REQUISIÇÕES GET, para servir como API
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path

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

        routes = {
            "/login": "login.html",
            "/cadastro": "cadastro.html",
            "/listar_filmes": "listar_filmes.html",
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
                self.send_error(404, "File not found")
        else:
            super().do_GET()

    #REQUISIÇÕES POST
    def do_POST(self):
        if self.path == '/send_login':
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            login = form_data.get('email', [""])[0]
            password = form_data.get('senha', [""])[0]
            
            #Chama a função criada para verificar o login 
            self.accont_user(login, password)
            return

        elif self.path == '/send_cadastro':
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)
            
            #Cria um dicionário com os dados do novo filme
            new_movie = {
                'nomeFilme': form_data.get('nomeFilme', [""])[0],
                'atores': form_data.get('atores', [""])[0],
                'diretor': form_data.get('diretor', [""])[0],
                'ano': form_data.get('ano', [""])[0],
                'genero': form_data.get('genero', [""])[0],
                'produtora': form_data.get('produtora', [""])[0],
                'sinopse': form_data.get('sinopse', [""])[0],
            }
            
            #Lê o arquivo JSON existente E cria
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
            
            self.send_response(303)
            self.send_header('Location', '/listar_filmes')
            self.end_headers()
            
        else:
            super().do_POST()

def main():
    server_address =('',8000)
    httpd = HTTPServer(server_address,MyHandler)
    print("Server running at http://localhost:8000")
    httpd.serve_forever()

if __name__ == '__main__':
    main()