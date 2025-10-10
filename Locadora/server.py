import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import json
import mysql.connector

# Conecta-se ao banco de dados MySQL 'locadora'.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="locadora"
)

# Classe principal que manipula as requisições HTTP do servidor.
class MyHandle(SimpleHTTPRequestHandler):
    
    # Sobrescreve o método padrão para servir o 'index.html' de um diretório.
    def list_directory(self, path):
        try:
            with open(os.path.join(path, 'index.html'), 'r', encoding='utf-8') as f:
                self.send_response(200)
                self.send_header("Content-type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))
            return None
        except FileNotFoundError:
            return super().list_directory(path)

    # Exemplo de como carregar e imprimir dados da tabela 'diretor' no console.
    def loadFilminhos(self):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM locadora.diretor")
        result = cursor.fetchall()
        print("Testatando\n", result)
        for res in result:
            id_diretor, nome, sobrenome, genero = res
            print(id_diretor, nome, sobrenome, genero)

    # Verifica de forma estática se as credenciais de login estão corretas.
    def accont_user(self, login, password):
        loga = "leticiaroth@gmail.com"
        senha = "12345"
        return login == loga and senha == password

    # Trata requisições GET para servir páginas HTML e dados da API de filmes.
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if self.path == '/api/filmes':
            try:
                cursor = mydb.cursor(dictionary=True)
                cursor.execute(""" SELECT * FROM filme """)
                filmes = cursor.fetchall()
                if not filmes:
                    filmes = []
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps(filmes, ensure_ascii=False).encode("utf-8"))
            except mysql.connector.Error as err:
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(err)}).encode("utf-8"))
            return
        
        if path == '/editar_filme':
            query_params = parse_qs(parsed_path.query)
            titulo_para_editar = query_params.get('titulo', [None])[0]
            if not titulo_para_editar:
                self.send_error(400, "Título do filme não fornecido")
                return
            try:
                with open("filmes.json", "r", encoding="utf-8") as f:
                    filmes = json.load(f)
                filme_encontrado = next((f for f in filmes if f['titulo'] == titulo_para_editar), None)
                if not filme_encontrado:
                    self.send_error(404, "Filme não encontrado")
                    return
                with open("editar_filme.html", "r", encoding="utf-8") as f:
                    content = f.read()
                content = content.replace('name="titulo"', f'name="titulo" value="{filme_encontrado.get("titulo", "")}"')
                content = content.replace('name="atores"', f'name="atores" value="{filme_encontrado.get("atores", "")}"')
                content = content.replace('name="diretor"', f'name="diretor" value="{filme_encontrado.get("diretor", "")}"')
                content = content.replace('name="ano"', f'name="ano" value="{filme_encontrado.get("ano", "")}"')
                content = content.replace('name="genero"', f'name="genero" value="{filme_encontrado.get("genero", "")}"')
                content = content.replace('name="produtora"', f'name="produtora" value="{filme_encontrado.get("produtora", "")}"')
                content = content.replace('</textarea>', f'{filme_encontrado.get("sinopse", "")}</textarea>')
                content = content.replace('</form>', f'<input type="hidden" name="titulo_antigo" value="{titulo_para_editar}"></form>')
                self.send_response(200)
                self.send_header("Content-type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(content.encode("utf-8"))
            except FileNotFoundError:
                self.send_error(404, "Arquivo de filmes ou template de edição não encontrado")
            return

        routes = {
            "/login": "login.html", "/cadastro_filmes": "cadastro_filmes.html",
            "/listar_filmes": "listar_filmes.html", "/editar_filme": "editar_filme.html",
        }
        if self.path in routes:
            try:
                with open(routes[self.path], "r", encoding="utf-8") as f:
                    self.send_response(200)
                    self.send_header("Content-type", "text/html; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(f.read().encode("utf-8"))
            except FileNotFoundError:
                self.send_error(404, "File not found")
        else:
            super().do_GET()

    # Trata requisições POST para processar formulários de login e cadastro de filmes.
    def do_POST(self):
        if self.path == '/send_login':
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)
            login = form_data.get('email',[""])[0]
            password = form_data.get('senha',[""])[0]
            if self.accont_user(login, password):
                self.send_response(303)
                self.send_header("Location", "/cadastro")
                self.end_headers()
            else:
                self.send_response(401)
                self.send_header("Content-type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write("Usuário ou senha inválidos".encode('utf-8'))
            return

        elif self.path == '/cadastro':
            content_length = int(self.headers['Content-length'])
            body = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(body)
            titulo = form_data.get('titulo', [""])[0]
            atores = form_data.get('atores', [""])[0]
            diretor = form_data.get('diretor', [""])[0]
            ano = form_data.get('ano', [""])[0]
            genero = form_data.get('genero', [""])[0]
            produtora = form_data.get('produtora', [""])[0]
            sinopse = form_data.get('sinopse', [""])[0]
            cursor = mydb.cursor()
            sql = "INSERT INTO filme (titulo, atores, diretor, ano, genero, produtora, sinopse) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (titulo, atores, diretor, ano, genero, produtora, sinopse)
            cursor.execute(sql, val)
            mydb.commit()
            self.send_response(303)
            self.send_header("Location", "/listar_filmes")
            self.end_headers()
            return
        else:
            super(MyHandle, self).do_POST()
            return

# Configura e inicia o servidor HTTP na porta 8000.
def main():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandle)
    print("Servidor rodando em http://localhost:8000")
    httpd.serve_forever()

# Garante que a função main() seja executada ao iniciar o script.
if __name__ == "__main__":
    main()