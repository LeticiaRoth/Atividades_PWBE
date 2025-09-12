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
 
def main():
    server_address =('',8000)
    httpd = HTTPServer (server_address,MyHandle)
    print("Server runing in http://localhost:8000")
    httpd.serve_forever()
 
main()