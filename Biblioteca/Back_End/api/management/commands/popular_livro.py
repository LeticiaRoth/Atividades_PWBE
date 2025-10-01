import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Livro, Autor, Editora

class Command(BaseCommand):
    help = "Popula a tabela Livro a partir de um arquivo CSV."

    def add_arguments(self, parser):
        parser.add_argument("--csv", default="population/livros.csv", help="Caminho para o arquivo CSV de livros.")
        parser.add_argument("--truncate", action="store_true", help="Limpa a tabela Livro antes de inserir os dados.")

    @transaction.atomic
    def handle(self, *args, **options):
        caminho_csv = options["csv"]
        self.stdout.write(self.style.SUCCESS(f"Lendo arquivo: {caminho_csv}"))

        df = pd.read_csv(caminho_csv, encoding="utf-8-sig")
        df.columns = [c.strip().lower().lstrip("\ufeff") for c in df.columns]

        if options["truncate"]:
            self.stdout.write(self.style.WARNING("Limpando a tabela Livro..."))
            Livro.objects.all().delete()

        # Cache de autores: Mapeia o nome completo (minúsculas) para o objeto Autor.
        autores_db = Autor.objects.all()
        autores_cache = {f"{autor.nome} {autor.sobrenome}".lower().strip(): autor for autor in autores_db}
        
        # Cache de editoras: Mapeia o nome (minúsculas) para o objeto Editora.
        editoras_cache = {e.editora.lower().strip(): e for e in Editora.objects.all()}

        livros_a_criar = []
        livros_pulados_autor = 0
        livros_pulados_existente = 0

        self.stdout.write(self.style.SUCCESS("Cache de autores e editoras criado. Validando e preparando os livros..."))

        for r in df.itertuples(index=False):
            autor_nome_csv = str(getattr(r, "autor", "")).lower().strip()
            editora_nome_csv = str(getattr(r, "editor", "")).lower().strip()
            isbn = str(getattr(r, "isbn", "")).strip()

            autor_obj = autores_cache.get(autor_nome_csv)
            if not autor_obj:
                self.stdout.write(self.style.ERROR(f"[PULANDO] Autor '{str(getattr(r, 'autor', '')).strip()}' não encontrado. Livro: {r.titulo}"))
                livros_pulados_autor += 1
                continue

            editora_obj = editoras_cache.get(editora_nome_csv)
            if not editora_obj:
                editora_nome_original = str(getattr(r, "editor", "")).strip()
                editora_obj, _ = Editora.objects.get_or_create(editora=editora_nome_original)
                editoras_cache[editora_nome_csv] = editora_obj
                self.stdout.write(self.style.NOTICE(f"[CRIADA] Nova editora '{editora_nome_original}' pois não existia."))

            if Livro.objects.filter(isbn=isbn).exists():
                self.stdout.write(self.style.WARNING(f"[EXISTE] Livro com ISBN {isbn} ({r.titulo}) já está no banco."))
                livros_pulados_existente += 1
                continue

            livros_a_criar.append(
                Livro(
                    isbn=isbn,
                    titulo=str(getattr(r, "titulo", "")).strip(),
                    subtitulo=str(getattr(r, "subtitulo", "")).strip(),
                    autor=autor_obj,
                    editor=editora_obj,  # <-- CORREÇÃO APLICADA AQUI
                    descricao=str(getattr(r, "descricao", "")).strip(),
                    idioma=str(getattr(r, "idioma", "Português")).strip(),
                    ano_publicacao=int(r.ano_publicacao) if pd.notna(r.ano_publicacao) else None,
                    paginas=int(r.paginas) if pd.notna(r.paginas) else None,
                    preco=float(r.preco) if pd.notna(r.preco) else 0.0,
                    estoque=int(r.estoque) if pd.notna(r.estoque) else 0,
                    desconto=float(r.desconto) if pd.notna(r.desconto) else 0.0,
                    disponivel=bool(getattr(r, 'disponivel', False)),
                    dimensoes=str(getattr(r, "dimensoes", "")).strip(),
                    peso=float(r.peso) if pd.notna(r.peso) else 0.0,
                )
            )

        if livros_a_criar:
            Livro.objects.bulk_create(livros_a_criar)

        self.stdout.write("-" * 50)
        self.stdout.write(self.style.SUCCESS(f"Operação concluída. Livros criados: {len(livros_a_criar)}"))
        self.stdout.write(self.style.WARNING(f"Livros pulados (autor não encontrado): {livros_pulados_autor}"))
        self.stdout.write(self.style.WARNING(f"Livros pulados (ISBN já existente): {livros_pulados_existente}"))