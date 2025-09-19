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
from urllib.parse import parse_qs
 
class MyHandle (SimpleHTTPRequestHandler):
    def list_directory(self, path):
        try:
            f = open(os.path.join(path,'index.html'), 'r')
 
            #Cabeçaho do header
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers    
            self.wfile.write(f.read().encode('utf-8'))
            f.close()
            return None
        except FileNotFoundError:
            pass
        return super().list_directory(path)
   

    #Verificação simples de usuário logado ou não logado
    def accont_user(login,password):
        loga = "leticiaroth@gmail.com"
        senha = 12345

        if login == loga and senha == password:
            return "Usuário logado"
        else:
            return "Usuário não existe "
    
    #Requisição do GET
    def do_GET(self):
        if self.path == "/login":
            try:
                with open(os.path.join(os.getcwd(), "login.html"), "r") as login:
                    content = login.read()
                self.send_response(200)
                self.send_header("Content-type","text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File not found")

        elif self.path == "/cadastro":
            try:
                with open(os.path.join(os.getcwd(), "cadastro.html"), "r") as cadastro:
                    content = cadastro.read()
                self.send_response(200)
                self.send_header("Content-type","text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File not found")

        elif self.path == "/listar_filmes":
            try:
                with open(os.path.join(os.getcwd(), "listar_filmes.html"), "r") as listar_filmes:
                    content = listar_filmes.read()
                self.send_response(200)
                self.send_header("Content-type","text/html")
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.send_error(404, "File not found")
        else:
            super().do_GET()
 

        #Método do POST
    def do_POST(self):
        if self.path == '/send_login':
            #Tamanho da requisição que está sendo mandada
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)

            login = form_data.get('email',[""])[0]
            password = form_data.get('senha',[""])[0]

            logou
            print("Data Form:")
            print("Email:", form_data.get('email',[""])[0])
            print("Senha:", form_data.get("senha",[""])[0])


            
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("Data Retrieving Sucess!".encode('utf-8'))
        else:
            super(MyHandle, self).do_POST()



def main():
    server_address =('',8000)
    httpd = HTTPServer (server_address,MyHandle)
    print("Server runing in http://localhost:8000")
    httpd.serve_forever()
 
main()